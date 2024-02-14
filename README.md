# OpenAI Billing Analysis

![GitHub Tag](https://img.shields.io/github/v/tag/skit-ai/openai-billing-analysis)

Command line tool to provide per key $ usage of OpenAI API keys on daily and
monthly level.

> [!NOTE]
> Open AI's dashboard will have this feature directly in some time. In
> that case, we will archive this repository and use the dashboard itself.

> [!CAUTION]
> Pricing for tokens is coming from
> [gpt-cost-estimator](https://github.com/michaelachmann/gpt-cost-estimator/)
> with updates (see `cli.py` in our repository) that were done on 13th Feb 2024.
> The pricing information might need to be refreshed so be careful while
> interpreting anything.

Install the package using:

```shell
pip install https://github.com/skit-ai/openai-billing-analysis/releases/download/0.1.0/openai_billing_analysis-0.1.0-py3-none-any.whl
```

For using, download JSON billing data from the activity tab of [the usage
dashboard](https://platform.openai.com/usage) and run the following:

```shell
openai_billing_analysis activity-2024-02-01-2024-03-01.json --date=2024-02-13
```
