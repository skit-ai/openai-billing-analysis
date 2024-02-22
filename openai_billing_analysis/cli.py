"""
Usage:
  openai_billing_analysis <activity-export> [--date=<date>]

Arguments:
  <activity-export>   JSON export file for Open AI monthly activity. Download
                      from activity tab here https://platform.openai.com/usage

Options:
  --date=<date>       Date to analyze in yyyy-MM-dd format. Defaults to today.
"""

import datetime
import json
import warnings

from docopt import docopt
from gpt_cost_estimator import CostEstimator
from pydash import py_
from tabulate import tabulate

PRICES = CostEstimator.PRICES


def activity_cost(activity: dict) -> float:
    if activity["usage_type"] != "text":
        raise ValueError(f"Unsupported usage type {activity['usage_type']}.")

    try:
        price = PRICES[activity["model"]]
    except KeyError:
        warnings.warn(f"Unsupported model {activity['model']} found. Skipping. "
                      "Know that your actual price might be higher than shown value.")
        return 0

    return (price["input"] * activity["n_context_tokens_total"] / 1000) + \
        (price["output"] * activity["n_generated_tokens_total"] / 1000)


def activity_date(activity: dict) ->  datetime.date:
    tz = datetime.datetime.now().astimezone().tzinfo

    return datetime.datetime.fromtimestamp(activity["timestamp"], tz=tz).date()


def print_breakdown(data: list[dict]):
    table = []

    def _group_fn(activity) -> str:
        return activity["api_key_name"] or activity["user"]

    for name, group in py_.group_by(data, _group_fn).items():
        table.append([name, sum([activity_cost(activity) for activity in group])])

    table = sorted(table, key=lambda it: it[1], reverse=True)

    print(tabulate(table, headers=["Key / User", "$"], tablefmt="fancy_grid"))


def main():
    args = docopt(__doc__)

    with open(args["<activity-export>"]) as fp:
        data = json.load(fp)["data"]

    warnings.warn("Please ensure that the data dump is freshly downloaded")
    print()

    total_cost = sum([activity_cost(activity) for activity in data])
    print(f":: Total cost ${total_cost}")
    print(":: Monthly breakdown")
    print_breakdown(data)

    print("\n")

    if args["--date"]:
        asked_date = datetime.datetime.strptime(args["--date"], "%Y-%m-%d").date()
    else:
        asked_date = datetime.datetime.now().date()

    daily_data = [activity for activity in data if activity_date(activity) == asked_date]

    daily_cost = sum([activity_cost(activity) for activity in daily_data])
    print(f":: Day's ({asked_date} your tz) cost ${daily_cost}")

    print(f":: Daily breakdown")
    print_breakdown(daily_data)
