# OpenAI Billing Analysis

![GitHub Tag](https://img.shields.io/github/v/tag/skit-ai/openai-billing-analysis)

Command line tool to provide per key $ usage of OpenAI API keys on daily and
monthly level.

> [!NOTE]
> Open AI's dashboard will have this feature directly in some time. In
> that case, we will archive this repository and use the dashboard itself.

For using, download JSON billing data from the activity tab of [the usage
dashboard](https://platform.openai.com/usage) and run the following:

```shell
# Assuming you have installed the package
openai_billing_analysis activity-2024-02-01-2024-03-01.json --date=2024-02-13
```
