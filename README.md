# Extended Version

This benchmark evaluates large language models (LLMs) using 940 NYT Connections puzzles, with additional words included to increase difficulty.

To increase difficulty compared to standard NYT Connections puzzles, Extended Connections adds up to four extra trick words to each puzzle. We check that none of the added words fit into any category used in the corresponding puzzle.

It is a focused test of verbal associative reasoning under combinatorial
ambiguity: models need lexical and cultural knowledge, wordplay recognition,
global constraint solving, and resistance to plausible decoys. It can reflect
broader reasoning ability, but it is not a comprehensive measure of general
intelligence and does not directly test skills such as software engineering.

Headline results use quadratic-v1 scoring: a puzzle with `g` exact groups
contributes `(g / 4)²`, so 0, 1, 2, 3, and 4 groups earn 0%, 6.25%, 25%,
56.25%, and 100%, respectively. The leaderboard score is the mean of those
per-puzzle values.

### Chart: Extended Version

![Leaderboard](images/nyt_connections_chart_highlighted.png)

Scoreboard and model-comparison charts apply the current chart-suppression
policy. The leaderboard tables retain every full-coverage result, including
models omitted from charts, so historical results remain available for
comparison. The all-history family-progress chart includes models suppressed
from other charts.

### Leaderboard: Extended Version

The main board includes only models that completed all 940 puzzles.

|Rank|Model|Score %|#Puzzles|
|---:|-----|----------------:|-------:|
|1|Gemini 4 Carbon (high reasoning)|99.3|940|
|2|Gemini 4 Argon (high reasoning)|98.6|940|
|3|GPT-6 Astra (max reasoning)|98.4|940|
|4|GPT-6.2 Astra (high reasoning)|98.2|940|
|5|GPT-6 Astra (xhigh reasoning)|98.1|940|
|6|GPT-6.1 Sol (max reasoning)|97.8|940|
|7|GPT-6 Astra (high reasoning)|97.7|940|
|8|Gemini 3.1 Pro Preview|97.4|940|
|9|Gemini 3.8 Flash (high reasoning)|97.4|940|
|10|Claude Fable 5.2 (high reasoning)|97.3|940|
|11|GPT-5.5 (xhigh reasoning)|96.2|940|
|12|GPT-6.1 Sol (high reasoning)|95.5|940|
|13|GPT-5.5 (high reasoning)|95.2|940|
|14|Gemini 3 Pro Preview|94.4|940|
|15|Claude Opus 5 (xhigh reasoning)|94.3|940|
|16|GPT-6.2 Sol (high reasoning)|94.1|940|
|17|Gemini 3.7 Flash|94.0|940|
|18|GPT-5.6 Sol (xhigh reasoning)|93.8|940|
|19|Kimi K3|93.6|940|
|20|Kimi K3.1 Pro (high reasoning)|93.4|940|
|21|Muse Wonder 1.0 (high reasoning)|93.4|940|
|22|DeepSeek V4.1 Flash 1017 (high reasoning)|92.8|940|
|23|Claude Fable 5 (high reasoning)|92.7|940|
|24|Gemini 3.5 Flash|92.6|940|
|25|GPT-5.5 (medium reasoning)|92.4|940|
|26|Claude Opus 5 (high reasoning)|92.2|940|
|27|Claude Opus 4.6 (high reasoning)|92.1|940|
|28|DeepSeek V4 Pro (high reasoning)|91.3|940|
|29|GPT-5.4 (xhigh reasoning)|91.3|940|
|30|Claude Opus 4.8 (xhigh reasoning)|91.1|940|
|31|GPT-5.6 Sol (high reasoning)|91.0|940|
|32|Qwen 4 Max (high)|90.8|940|
|33|GPT-5.4 (high reasoning)|90.6|940|
|34|GPT-6 Sol (high reasoning)|90.1|940|
|35|Claude Fable 5.1 (high reasoning)|90.0|940|
|36|Grok 4.20 Multi-Agent Exp Beta 0304|89.6|940|
|37|DeepSeek V4 Flash|89.6|940|
|38|DeepSeek V4.1 Flash (high reasoning)|89.6|940|
|39|Gemini 3.6 Flash|89.0|940|
|40|Claude Opus 5.5 (high reasoning)|88.5|940|
|41|Claude Opus 4.8 (high reasoning)|88.3|940|
|42|Qwen 3.8 Max|88.3|940|
|43|Claude Opus 5.5 (medium reasoning)|87.8|940|
|44|GPT-5.4 (medium reasoning)|87.8|940|
|45|Grok 4.1 Fast Reasoning|87.4|940|
|46|Kimi K2.6|87.2|940|
|47|GPT-6.1 Terra (high reasoning)|86.8|940|
|48|Grok 4.20 0309 (Reasoning)|85.4|940|
|49|Qwen 3.7 Max|85.1|940|
|50|Muse Spark 1.3 (high reasoning)|85.1|940|
|51|Muse Spark 1.1 (high reasoning)|84.9|940|
|52|Grok 4.20 Reasoning Exp Beta 0304|83.7|940|
|53|GPT-5.2 (xhigh reasoning)|83.6|940|
|54|Tencent Hy4 (high)|83.5|940|
|55|Gemini 3 Flash Preview|83.1|940|
|56|Claude Sonnet 4.6 (high reasoning)|80.9|940|
|57|Claude Sonnet 5.5 (high reasoning)|80.5|940|
|58|Grok 4.6 (xhigh reasoning)|80.0|940|
|59|Grok 4.5 (high reasoning)|79.9|940|
|60|GPT-5.2 Pro|79.3|940|
|61|Muse Spark 1.2 (high reasoning)|79.2|940|
|62|Grok 4.6 (high reasoning)|79.0|940|
|63|GPT-5.6 Terra (high reasoning)|78.4|940|
|64|Muse Spark Open (high reasoning)|78.4|940|
|65|GLM-5.1|77.7|940|
|66|ByteDance Seed2.1 Pro|77.5|940|
|67|Grok 4.7 (high reasoning)|76.8|940|
|68|Step 5 Preview (high reasoning)|76.6|940|
|69|Claude Sonnet 4.6 Thinking 32K|76.4|940|
|70|Claude Opus 4.6 Thinking 16K|76.4|940|
|71|Claude Sonnet 5 (high reasoning)|75.1|940|
|72|GLM-5|74.8|940|
|73|Qwen 3.7 Plus|74.8|940|
|74|GLM-5.2 (high reasoning)|74.3|940|
|75|GLM-5.3 (high reasoning)|74.2|940|
|76|Qwen 3.6 Max Preview|74.1|940|
|77|Gemma 4 31B Reasoning|70.6|940|
|78|Kimi K2.5 Thinking|69.9|940|
|79|GPT-5.6 Luna (high reasoning)|69.4|940|
|80|GPT-6 Luna (high reasoning)|68.7|940|
|81|Tencent Hy4 Preview|68.2|940|
|82|GPT-5.2 (high reasoning)|68.1|940|
|83|DeepSeek V4 Pro Preview|67.3|940|
|84|Claude Haiku 5.5 (high reasoning)|65.7|940|
|85|MiniMax-M3|65.1|940|
|86|GPT-5.4 Mini (xhigh reasoning)|61.8|940|
|87|GPT-5.2 (medium reasoning)|60.6|940|
|88|Gemini 3.5 Flash-Lite (high reasoning)|60.4|940|
|89|Qwen 3.6 Plus|60.3|940|
|90|Qwen3.5-397B-A17B|58.9|940|
|91|Grok 4.3|55.2|940|
|92|Qwen3.8-27B|54.5|940|
|93|GPT-5.2 (low reasoning)|54.2|940|
|94|Claude Opus 4.5 Thinking 16K|52.5|940|
|95|Qwen3.5-122B-A10B|51.7|940|
|96|Claude Opus 4.5 (no reasoning)|49.4|940|
|97|Claude Sonnet 4.6 Thinking 16K|48.0|940|
|98|Qwen3.5-27B|47.9|940|
|99|Claude Sonnet 4.6 (no reasoning)|44.8|940|
|100|Qwen 3.7 Flash|43.8|940|
|101|Claude Opus 4.6 (no reasoning)|43.2|940|
|102|Qwen3.6-35B-A3B|41.6|940|
|103|Tencent Hy3 (high)|41.2|940|
|104|Step 3.7 Flash (high reasoning)|39.7|940|
|105|Claude Opus 4.7 (high reasoning)|39.0|940|
|106|Claude Sonnet 4.5 Thinking 16K|37.3|940|
|107|DeepSeek V3.2|36.7|940|
|108|Claude Sonnet 4.5 (no reasoning)|35.8|940|
|109|Xiaomi MiMo V2.5 Pro|34.4|940|
|110|Qwen3 Max (2026-01-23)|30.1|940|
|111|Step 3.5 Flash|28.4|940|
|112|ByteDance Seed2.0 Pro|28.4|940|
|113|MiniMax M3.1 Flash (high reasoning)|28.3|940|
|114|Mistral Large 4 (high)|27.4|940|
|115|Xiaomi MiMo V2 Pro|25.8|940|
|116|MiniMax-M2.7|24.7|940|
|117|Baidu Ernie 5.1|23.4|940|
|118|GPT-5.5 (no reasoning)|22.0|940|
|119|GPT-5.4 (no reasoning)|17.8|940|
|120|LongCat Flash Thinking|17.7|940|
|121|Tencent Hy3 Preview|17.2|940|
|122|MiniMax-M2.5|16.8|940|
|123|Arcee Trinity Large Thinking|16.5|940|
|124|Gemma 4 31B IT|15.7|940|
|125|Nemotron 3 Super|15.4|940|
|126|MiniMax-M2|14.8|940|
|127|GPT-5.2 (no reasoning)|14.5|940|
|128|Claude 4.5 Haiku|14.3|940|
|129|Mistral Medium 3.5 (high)|12.9|940|
|130|Grok 4.1 Fast Non-Reasoning|12.3|940|
|131|Qwen 3 Max Thinking|11.8|940|
|132|MiniMax-M2.1|11.2|940|
|133|Claude Opus 4.7 (no reasoning)|10.8|940|
|134|Baidu Ernie 5.0|10.3|940|
|135|Grok 4.20 0309 (Non-Reasoning)|8.6|940|
|136|DeepSeek V3.2 (no reasoning)|8.2|940|
|137|Gemini 3.1 Flash-Lite Preview|8.2|940|
|138|Llama 4 Maverick|8.0|940|
|139|Grok 4.20 Non-Reasoning Exp Beta 0304|7.6|940|
|140|Mistral Large 3|7.5|940|
|141|Tencent Hy3 (non-thinking)|6.9|940|
|142|Mistral Medium 3.1|6.5|940|
|143|Ling 2.6 1T|4.1|940|

---
## Model comparison scatter charts

### GPT-6.2 Astra and Sol vs. their predecessors

At high reasoning effort, GPT-6.2 Astra improves by 0.51 percentage points
over GPT-6 Astra and fully solves eight more puzzles. GPT-6.2 Sol scores
1.37 points below GPT-6.1 Sol and fully solves 20 fewer puzzles. The newest
100 puzzles show the same direction for each comparison.

|Model (high reasoning)|Score, all 940|Fully solved|Score, newest 100|Standard-price cost/puzzle|
|---|---:|---:|---:|---:|
|GPT-6 Astra|97.73%|901|97.81%|$0.02807|
|GPT-6.2 Astra|98.23%|909|98.25%|$0.01462|
|GPT-6.1 Sol|95.49%|861|95.63%|$0.00686|
|GPT-6.2 Sol|94.12%|841|92.94%|$0.00507|

Counting unsolved lines (groups) across all 940 puzzles, Astra 6.2 misses
**42**, versus **54** for GPT-6 Astra. Sol 6.2 misses **144**, versus **108**
for GPT-6.1 Sol. For every 100 predecessor mistakes, that is **77.8** for
Astra (22.2% fewer) and **133.3** for Sol (33.3% more). Each run has 3,760
lines; the comparison is `100 × new unsolved lines / predecessor unsolved lines`.

All cost comparisons use standard list prices for every model. Each GPT estimate
covers 940 saved answers. Cost per puzzle falls 47.9% for Astra and
26.0% for Sol. The estimated run totals fall from $26.39 to $13.74
for Astra, and from $6.45 to $4.77 for Sol. These estimates apply the
same pricing basis regardless of Batch, Flex, priority, or fast execution.
They are token-usage estimates rather than billed totals and exclude failed
requests. Execution-tier costs are retained separately in the run audits.

GPT-6.2 Astra, GPT-6.2 Sol, and Seed2.1 Pro are the highlighted models. Orange
arrows connect Astra and Sol to their high-effort predecessors in the cost chart.

### Seed2.1 Pro vs. Seed2.0 Pro

ByteDance Seed2.1 Pro completes all 940 puzzles, improving the score by
49.12 percentage points over Seed2.0 Pro and fully solving 483 more puzzles.

|Metric|Seed2.0 Pro|Seed2.1 Pro|
|---|---:|---:|
|Score, all 940 puzzles|28.36%|77.49%|
|Fully solved, all 940 puzzles|122|605|
|Score, newest 100 puzzles|28.00%|77.38%|
|Fully solved, newest 100 puzzles|13|60|
|Estimated cost per puzzle|$0.00755|$0.21437|
|Estimated total cost|$7.10|$201.51|

The estimated cost per puzzle is 28.4 times higher. Seed2.1 Pro costs use
recorded usage for all 940 saved answers. Seed2.0 Pro has exact usage for 938
answers; its estimate covers the remaining two using a 50-puzzle cost sample.
These are usage-based estimates, not billed totals. Seed2.1 Pro's failed
provider streams and interrupted attempts have unavailable usage and are
excluded from its cost estimate.

### Qwen 4 Max vs. Qwen 3.8 Max

Qwen 4 Max (high) improves the full-benchmark score over its predecessor,
Qwen 3.8 Max, at substantially lower estimated cost. The newest-100 score
decreases, so the improvement does not hold across both evaluation sets.

|Metric|Qwen 3.8 Max|Qwen 4 Max (high)|Change|
|---|---:|---:|---:|
|Score, all 940 puzzles|88.33%|90.81%|+2.48 percentage points|
|Fully solved, all 940 puzzles|762|799|+37|
|Score, newest 100 puzzles|88.94%|86.63%|−2.31 percentage points|
|Fully solved, newest 100 puzzles|83|80|−3|
|Estimated cost per priced response|$0.20237|$0.02840|86.0% lower|
|Mean output tokens per priced response|33,645|6,627|80.3% fewer|

Costs use recorded token usage and registered standard list prices for 938
Qwen 3.8 Max responses and 929 Qwen 4 Max responses. Their estimated usage
totals are $189.82 and $26.38, respectively; these are not billed totals.
Refusals count as zero in the 940-puzzle scores and are excluded from these
cost estimates. Qwen 4 Max costs about one-seventh as much per priced response,
reflecting both fewer output tokens and lower registered token prices: $1.413 input and
$4.24 output per million tokens, versus $2.00 input and $6.00 output.
Qwen 3.8 Max is retained in the leaderboard history and suppressed from current charts.

### Model family progress

This chart shows score progress over time within each model family on a shared
601-puzzle comparison set. Unlike the current-cohort charts, it includes every
tested model with score and release-date data, including models evaluated on
older versions of the benchmark and models suppressed from other charts.

![Model family progress](images/model_intro_date_vs_score_family_progress_common601.png)

### Introduction date vs. score

This chart compares benchmark score against model introduction date on the
same shared 601-puzzle comparison set.

![Introduction date vs. score](images/model_intro_date_vs_score_common601.png)

### Cost vs. performance

This chart compares estimated average cost per puzzle with the full
940-puzzle benchmark score for current full-coverage models. Costs use recorded
token usage and standard list prices for every model, regardless of the
execution tier. They are estimates rather than billed totals.
Time-varying prices are averaged over their full pricing cycle.

![Cost vs. performance](images/model_cost_vs_performance_highlighted.png)

---
### Correlation of puzzle-level results: heatmap

![Correlations](images/llm_puzzle_corr_quadratic.png)

---
## Newest 100 puzzles.

To counteract the possibility of an LLM's training data including the solutions, we have also tested only the 100 latest puzzles. Note that lower scores do not necessarily indicate that NYT Connections solutions are in the training data, as the difficulty of the first puzzles was lower.

---
### Chart: Newest 100 puzzles, extended version

![Newest 100 puzzles](images/nyt_connections_chart_latest100_highlighted.png)

This scoreboard chart applies the same chart-suppression policy as the full
benchmark chart.

### Leaderboard: Newest 100 puzzles, extended version

This view applies the same scoring rule to the newest 100 puzzles for every full-coverage model.

|Rank|Model|Score %|#Puzzles|
|---:|-----|----------------:|-------:|
|1|Gemini 4 Carbon (high reasoning)|99.6|100|
|2|GPT-6 Astra (xhigh reasoning)|98.7|100|
|3|Gemini 4 Argon (high reasoning)|98.7|100|
|4|GPT-6.1 Sol (max reasoning)|98.7|100|
|5|GPT-6.2 Astra (high reasoning)|98.2|100|
|6|GPT-6 Astra (max reasoning)|97.9|100|
|7|GPT-6 Astra (high reasoning)|97.8|100|
|8|Claude Fable 5.2 (high reasoning)|96.9|100|
|9|Gemini 3.8 Flash (high reasoning)|96.5|100|
|10|Gemini 3.1 Pro Preview|96.1|100|
|11|GPT-5.5 (xhigh reasoning)|96.1|100|
|12|GPT-6.1 Sol (high reasoning)|95.6|100|
|13|GPT-5.5 (high reasoning)|95.2|100|
|14|Claude Opus 5 (xhigh reasoning)|94.5|100|
|15|GPT-5.6 Sol (xhigh reasoning)|94.4|100|
|16|Claude Fable 5 (high reasoning)|93.6|100|
|17|GPT-5.4 (xhigh reasoning)|93.4|100|
|18|GPT-6.2 Sol (high reasoning)|92.9|100|
|19|Muse Wonder 1.0 (high reasoning)|92.8|100|
|20|GPT-5.6 Sol (high reasoning)|92.7|100|
|21|Gemini 3 Pro Preview|92.3|100|
|22|Gemini 3.7 Flash|92.2|100|
|23|Claude Opus 4.8 (high reasoning)|92.1|100|
|24|Kimi K3|92.1|100|
|25|Claude Opus 5 (high reasoning)|91.9|100|
|26|DeepSeek V4.1 Flash 1017 (high reasoning)|91.3|100|
|27|Gemini 3.5 Flash|90.8|100|
|28|Claude Opus 4.8 (xhigh reasoning)|90.6|100|
|29|Claude Opus 5.5 (high reasoning)|90.6|100|
|30|Kimi K3.1 Pro (high reasoning)|90.2|100|
|31|GPT-6.1 Terra (high reasoning)|90.2|100|
|32|Qwen 3.8 Max|88.9|100|
|33|GPT-6 Sol (high reasoning)|88.8|100|
|34|Claude Fable 5.1 (high reasoning)|88.5|100|
|35|Gemini 3.6 Flash|88.5|100|
|36|DeepSeek V4 Pro (high reasoning)|88.4|100|
|37|GPT-5.4 (high reasoning)|88.4|100|
|38|Claude Opus 4.6 (high reasoning)|88.1|100|
|39|GPT-5.5 (medium reasoning)|87.3|100|
|40|DeepSeek V4 Flash|87.2|100|
|41|Qwen 4 Max (high)|86.6|100|
|42|DeepSeek V4.1 Flash (high reasoning)|86.1|100|
|43|Tencent Hy4 (high)|86.0|100|
|44|Grok 4.20 Multi-Agent Exp Beta 0304|85.2|100|
|45|Muse Spark 1.1 (high reasoning)|84.8|100|
|46|GPT-5.4 (medium reasoning)|84.4|100|
|47|Muse Spark 1.3 (high reasoning)|83.6|100|
|48|Claude Opus 5.5 (medium reasoning)|83.4|100|
|49|Kimi K2.6|80.2|100|
|50|Claude Sonnet 5.5 (high reasoning)|79.1|100|
|51|Qwen 3.7 Max|78.9|100|
|52|GPT-5.2 (xhigh reasoning)|78.6|100|
|53|Claude Opus 4.6 Thinking 16K|78.4|100|
|54|GLM-5.1|77.6|100|
|55|Grok 4.20 0309 (Reasoning)|77.4|100|
|56|ByteDance Seed2.1 Pro|77.4|100|
|57|Muse Spark 1.2 (high reasoning)|77.2|100|
|58|Grok 4.5 (high reasoning)|77.2|100|
|59|Grok 4.20 Reasoning Exp Beta 0304|77.1|100|
|60|Grok 4.6 (xhigh reasoning)|77.1|100|
|61|Step 5 Preview (high reasoning)|75.4|100|
|62|Grok 4.1 Fast Reasoning|75.2|100|
|63|Grok 4.6 (high reasoning)|74.6|100|
|64|Muse Spark Open (high reasoning)|74.3|100|
|65|Claude Sonnet 4.6 (high reasoning)|74.1|100|
|66|GLM-5.2 (high reasoning)|72.8|100|
|67|Grok 4.7 (high reasoning)|72.8|100|
|68|GPT-5.6 Terra (high reasoning)|72.4|100|
|69|GLM-5.3 (high reasoning)|72.2|100|
|70|GPT-5.2 Pro|71.8|100|
|71|Qwen 3.7 Plus|70.9|100|
|72|Claude Sonnet 5 (high reasoning)|69.9|100|
|73|Claude Sonnet 4.6 Thinking 32K|69.4|100|
|74|Qwen 3.6 Max Preview|69.4|100|
|75|GLM-5|67.5|100|
|76|GPT-5.2 (high reasoning)|66.2|100|
|77|GPT-5.6 Luna (high reasoning)|66.1|100|
|78|Gemma 4 31B Reasoning|65.9|100|
|79|GPT-6 Luna (high reasoning)|65.8|100|
|80|Claude Haiku 5.5 (high reasoning)|64.9|100|
|81|Tencent Hy4 Preview|64.2|100|
|82|Kimi K2.5 Thinking|63.7|100|
|83|MiniMax-M3|63.4|100|
|84|GPT-5.4 Mini (xhigh reasoning)|62.5|100|
|85|Gemini 3 Flash Preview|61.8|100|
|86|Gemini 3.5 Flash-Lite (high reasoning)|60.7|100|
|87|DeepSeek V4 Pro Preview|59.9|100|
|88|Qwen 3.6 Plus|57.1|100|
|89|GPT-5.2 (medium reasoning)|55.8|100|
|90|Qwen3.8-27B|52.0|100|
|91|Claude Opus 4.5 Thinking 16K|51.6|100|
|92|Qwen3.5-397B-A17B|47.1|100|
|93|GPT-5.2 (low reasoning)|46.4|100|
|94|Grok 4.3|45.6|100|
|95|Qwen3.5-122B-A10B|45.4|100|
|96|Claude Sonnet 4.6 Thinking 16K|45.3|100|
|97|Qwen3.5-27B|44.6|100|
|98|Claude Sonnet 4.5 (no reasoning)|43.6|100|
|99|Claude Sonnet 4.5 Thinking 16K|43.0|100|
|100|Claude Opus 4.5 (no reasoning)|42.0|100|
|101|Tencent Hy3 (high)|40.6|100|
|102|Claude Sonnet 4.6 (no reasoning)|40.4|100|
|103|Claude Opus 4.7 (high reasoning)|39.3|100|
|104|Claude 4.5 Haiku|37.5|100|
|105|Claude Opus 4.6 (no reasoning)|37.2|100|
|106|Qwen3.6-35B-A3B|35.5|100|
|107|Qwen 3.7 Flash|35.4|100|
|108|Step 3.7 Flash (high reasoning)|34.2|100|
|109|Qwen3 Max (2026-01-23)|31.6|100|
|110|Xiaomi MiMo V2.5 Pro|31.4|100|
|111|DeepSeek V3.2|29.7|100|
|112|MiniMax M3.1 Flash (high reasoning)|29.2|100|
|113|MiniMax-M2.7|28.6|100|
|114|ByteDance Seed2.0 Pro|28.0|100|
|115|Mistral Large 4 (high)|27.2|100|
|116|Step 3.5 Flash|22.8|100|
|117|Xiaomi MiMo V2 Pro|22.0|100|
|118|Baidu Ernie 5.1|20.0|100|
|119|GPT-5.4 (no reasoning)|19.8|100|
|120|GPT-5.5 (no reasoning)|19.1|100|
|121|Tencent Hy3 Preview|18.9|100|
|122|LongCat Flash Thinking|17.3|100|
|123|Arcee Trinity Large Thinking|16.9|100|
|124|MiniMax-M2.5|16.2|100|
|125|GPT-5.2 (no reasoning)|15.8|100|
|126|Gemma 4 31B IT|15.7|100|
|127|Mistral Medium 3.5 (high)|14.6|100|
|128|MiniMax-M2.1|12.8|100|
|129|Nemotron 3 Super|12.4|100|
|130|Claude Opus 4.7 (no reasoning)|11.9|100|
|131|MiniMax-M2|11.9|100|
|132|Qwen 3 Max Thinking|11.6|100|
|133|Baidu Ernie 5.0|10.7|100|
|134|Grok 4.20 0309 (Non-Reasoning)|9.4|100|
|135|Mistral Large 3|8.9|100|
|136|Gemini 3.1 Flash-Lite Preview|8.9|100|
|137|Grok 4.1 Fast Non-Reasoning|8.8|100|
|138|Tencent Hy3 (non-thinking)|8.2|100|
|139|Llama 4 Maverick|8.1|100|
|140|Grok 4.20 Non-Reasoning Exp Beta 0304|7.7|100|
|141|Mistral Medium 3.1|7.1|100|
|142|DeepSeek V3.2 (no reasoning)|6.8|100|
|143|Ling 2.6 1T|5.5|100|

---
# Humans vs. LLMs

To explore how top language models (LLMs) compare to humans in the New York Times Connections puzzle, we used official NYT performance data from December 2024 to February 2025, as analyzed by u/Bryschien1996, alongside a simulated gameplay setup that mirrors the human experience. This setup involves a multi-step process where solvers iteratively propose groups, receive feedback ("correct," "one away," "incorrect"), and are allowed up to four mistakes before failing. According to NYT data, the average human player solved approximately 71% of puzzles over the three-month period from December 2024 to February 2025, with solve rates ranging from 39% on the toughest days (e.g., February 2, 2025) to 98% on the easiest (e.g., February 26, 2025). It's worth noting that NYT Connections players are self-selected and likely perform better than the general population. We collected data from nine LLMs spanning a range of scores in the Extended Connections benchmark.

![nyt_connections_chart_basic](https://github.com/user-attachments/assets/137e02c0-dbd0-45a8-ac21-9f32856a5048)

The results reveal that top reasoning LLMs from OpenAI consistently outperform the average human player. DeepSeek R1 performs closest to the level of an average NYT Connections player.

Elite human players, however, set a higher standard, achieving a 100% win rate during the same period:

<img width="1150" alt="ex" src="https://github.com/user-attachments/assets/27307501-7ff6-4965-8f87-659c84d2fe3f" />

o1, with a 98.9% win rate, comes close to this elite level. o1-pro, which has not yet been tested in this gameplay simulation setup, might be able to match these top humans. Thus, directly determining whether AI achieves superhuman performance on NYT Connections could hinge on comparing the number of mistakes made before fully solving each puzzle.

---

# Original NYT Connections LLM Benchmark

This benchmark evaluates large language models (LLMs) using 436 NYT Connections puzzles. Three different prompts, not optimized for LLMs through prompt engineering, are used. Both uppercase and lowercase puzzles are assessed. Easier - no extra words added.

### Chart: Original Version

![nyt_connections_chart](https://github.com/user-attachments/assets/05adf945-c791-474b-8fe2-0b95b8008bcc)

### Leaderboard: Original Version

| Model | Score |
| --- | --- |
| o1 | 90.7
| o1-preview | 87.1
| o3-mini | 72.4
| DeepSeek R1 | 54.4
| o1-mini | 42.2
| Multi-turn ensemble | 37.8
| Gemini 2.0 Flash Thinking Exp 01-21 | 37.0
| GPT-4 Turbo | 28.3
| GPT-4o 2024-11-20 | 27.9
| GPT-4o 2024-08-06 | 26.5
| Llama 3.1 405B | 26.3
| Claude 3.5 Sonnet (2024-10-22) | 25.9
| Claude 3 Opus | 24.8
| Grok Beta | 23.7
| Llama 3.3 70B | 23.7
| Gemini 1.5 Pro (Sept) | 22.7
| Deepseek-V3 | 21.0
| Gemini 2.0 Flash Exp | 20.0
| Gemma 2 27B | 18.8
| Qwen 2.5 Max | 18.6
| Gemini 2.0 Flash Thinking Exp	| 18.6
| Mistral Large 2 | 17.4
| Qwen 2.5 72B | 14.8
| Claude 3.5 Haiku | 13.7
| MiniMax-Text-01 | 13.6
| Nova Pro | 12.5
| Phi-4 | 11.6
| Mistral Small 3 | 10.5
| DeepSeek-V2.5 | 9.9

### Leaderboard: Older models

These legacy or incomplete runs use the same scoring rule but are excluded from the main board because they ran fewer than 940 total puzzles.

|Rank|Model|Score %|#Puzzles (window)|Total Coverage|
|---:|-----|----------------:|-----------------:|-------------:|
|1|GLM-5.2 (max reasoning)|89.5|194|194/940|
|2|Sherlock Think Alpha|89.0|759|759/940|
|3|Qwen 3.8 Max 0902|88.8|919|919/940|
|4|Grok 4 Fast Reasoning|88.0|759|759/940|
|5|Inkling (high reasoning)|88.0|136|136/940|
|6|Grok 4|87.8|759|759/940|
|7|Sonoma Sky Alpha|86.5|759|759/940|
|8|Xiaomi MiMo V2.6 Pro (thinking)|84.0|27|27/940|
|9|o3-pro (medium reasoning)|81.7|759|759/940|
|10|GPT-5 Pro|77.0|759|759/940|
|11|GLM-5.2 (max reasoning)|75.9|211|211/940|
|12|o1-pro (medium reasoning)|74.6|651|651/940|
|13|o3 (high reasoning)|70.5|759|759/940|
|14|GPT-5 (high reasoning)|67.8|759|759/940|
|15|o4-mini (high reasoning)|64.0|759|759/940|
|16|Ox Alpha (max reasoning)|63.5|217|217/940|
|17|o3 (medium reasoning)|63.0|759|759/940|
|18|GPT-5 (medium reasoning)|61.8|759|759/940|
|19|o1 (medium reasoning)|60.1|651|651/940|
|20|GPT-5.1 (high reasoning)|59.7|759|759/940|
|21|o4-mini (medium reasoning)|58.4|651|651/940|
|22|GPT-5 mini (medium reasoning)|54.9|759|759/940|
|23|GPT-5 (low reasoning)|53.2|759|759/940|
|24|GPT-5.1 (medium reasoning)|51.2|759|759/940|
|25|o3-mini (high reasoning)|49.0|651|651/940|
|26|GLM-4.7|47.2|767|767/940|
|27|Claude Opus 4.1 Thinking 16K|45.3|759|759/940|
|28|Gemini 2.5 Pro|44.9|759|759/940|
|29|Kimi K2 Thinking 64K|44.6|924|924/940|
|30|DeepSeek V4 Flash (thinking)|43.9|759|759/940|
|31|o3-mini (medium reasoning)|40.1|651|651/940|
|32|Gemini 2.5 Pro Exp 03-25|40.1|651|651/940|
|33|Qwen 3 235B A22B|39.8|759|759/940|
|34|Claude Opus 4 Thinking 16K|35.2|759|759/940|
|35|DeepSeek R1 05/28|33.6|759|759/940|
|36|Qwen 3 235B A22B 25-07 Think|31.6|759|759/940|
|37|Gemini 2.5 Pro Preview 05-06|28.1|651|651/940|
|38|Claude Sonnet 4 Thinking 16K|26.4|759|759/940|
|39|Claude Sonnet 4 Thinking 64K|26.0|651|651/940|
|40|DeepSeek R1|24.4|651|651/940|
|41|GPT-OSS-120B|24.1|759|759/940|
|42|Claude Opus 4.1 (no reasoning)|21.7|759|759/940|
|43|Qwen 3 30B A3B|21.2|759|759/940|
|44|Qwen 3 32B|21.0|759|759/940|
|45|Qwen 3 30B A3B 25-07 Thinking|20.9|759|759/940|
|46|Claude 3.7 Sonnet Thinking 16K|19.7|651|651/940|
|47|Claude Opus 4 (no reasoning)|19.7|759|759/940|
|48|GPT-4.5 Preview|19.2|651|651/940|
|49|Qwen 3 Next 80B A3B Thinking|18.5|759|759/940|
|50|Qwen QwQ-32B 16K|17.8|651|651/940|
|51|Grok 3 Mini Beta (high)|17.2|759|759/940|
|52|GLM-4.5|17.0|759|759/940|
|53|o1-mini|14.1|651|651/940|
|54|Grok 3 Mini Beta (low)|14.0|651|651/940|
|55|GPT-5 (minimal reasoning)|13.9|759|759/940|
|56|Claude Sonnet 4 (no reasoning)|13.7|759|759/940|
|57|Claude Opus 4.6 Thinking 32K|13.6|98|98/940|
|58|Cohere Command A Reasoning|13.3|759|759/940|
|59|Gemini 2.5 Flash|12.8|759|759/940|
|60|Grok 4 Fast Non-Reasoning|12.5|759|759/940|
|61|GLM-4.6|12.5|759|759/940|
|62|Sherlock Dash Alpha|12.2|759|759/940|
|63|Quasar Alpha|12.1|651|651/940|
|64|Gemini 2.0 Flash Think Exp 01-21|12.0|649|649/940|
|65|Cohere Command A+|12.0|898|898/940|
|66|GPT-4o Mar 2025|11.8|759|759/940|
|67|Qwen 3 Max Preview|11.6|759|759/940|
|68|Gemini 2.0 Pro Exp 02-05|11.2|651|651/940|
|69|Kimi K2-0905|11.0|759|759/940|
|70|GPT-4.1|10.8|759|759/940|
|71|Sonoma Dusk Alpha|10.6|759|759/940|
|72|MiniMax-M1|10.5|688|688/940|
|73|GPT-4o Feb 2025|10.3|651|651/940|
|74|Polaris Alpha|10.2|759|759/940|
|75|DeepSeek V3.1 Non-Think|10.1|759|759/940|
|76|GPT-5.1 (no reasoning)|10.0|759|759/940|
|77|Grok 3 Beta (no reasoning)|9.0|759|759/940|
|78|Kimi K2|8.9|759|759/940|
|79|Claude 3.7 Sonnet|8.7|651|651/940|
|80|Gemini 1.5 Pro (Sept)|8.7|601|601/940|
|81|Qwen 3 235B A22B 25-07 Instruct|8.6|759|759/940|
|82|GPT-4o 2024-11-20|8.6|601|601/940|
|83|Grok 2 12-12|8.5|651|651/940|
|84|Gemini 2.0 Flash|8.3|651|651/940|
|85|Claude 3 Opus|8.2|650|650/940|
|86|Claude 3.5 Sonnet 2024-10-22|8.1|651|651/940|
|87|GPT-4o 2024-08-06|7.6|601|601/940|
|88|Llama 4 Scout|7.6|759|759/940|
|89|Qwen 2.5 Max|7.6|651|651/940|
|90|DeepSeek V3-0324|7.4|759|759/940|
|91|Llama 3.1 405B|6.7|651|651/940|
|92|Baidu Ernie 4.5 300B A47B|6.5|759|759/940|
|93|DeepSeek V4 Flash|6.2|651|651/940|
|94|GPT-4.1 mini|6.1|759|759/940|
|95|Llama 3.3 70B|5.9|651|651/940|
|96|MiniMax-Text-01|5.9|759|759/940|
|97|Mistral Medium 3.1|5.5|759|759/940|
|98|LongCat Flash|5.2|660|660/940|
|99|Cohere Command A|5.0|759|759/940|
|100|Mistral Large 3|4.8|759|759/940|
|101|Mistral Small 3.2|4.3|759|759/940|
|102|Gemma 2 27B|4.3|651|651/940|
|103|Mistral Small 3.1|4.2|651|651/940|
|104|Gemma 3 27B|4.2|759|759/940|
|105|Amazon Nova Pro|4.1|759|759/940|
|106|Qwen 2.5 72B|4.0|759|759/940|
|107|Claude 3.5 Haiku|3.8|759|759/940|
|108|Microsoft Phi-4|3.4|759|759/940|
|109|GPT-4o mini|3.4|759|759/940|
|110|Mistral Small 3|3.0|601|601/940|
|111|GPT-4.1 nano|2.8|759|759/940|
|112|GLM4-32B-0414|2.7|759|759/940|
|113|Claude 3 Haiku|0.7|601|601/940|
---

## Notes
- Claude Opus 4.7, Claude Opus 4.8 xhigh, MiMo v2.5 Pro, Qwen 3.7 Max, and Step 3.7 Flash high have counted refusals/content blocks; refused or blocked puzzles are scored as 0/4.
- Tencent Hy4 high includes five operator-stopped requests scored as 0/4 after repeated reasoning-only responses failed to produce final answers. Its cost estimate averages the 935 saved responses and excludes the unfinished requests.
- GLM-5.1 is the provider-default thinking run; GLM-5.2 entries with parenthetical reasoning labels use the stated reasoning setting.
- Partial credit follows the scoring rule above, which more heavily rewards complete solves.
- Only one attempt is allowed per puzzle. Humans solving puzzles on the NYT website get four attempts and a notification when they're one step away from the solution.
- This benchmark is not affiliated with the New York Times

---

## Other multi-agent benchmarks
- [PACT - Benchmarking LLM negotiation skill in multi-round buyer-seller bargaining](https://github.com/lechmazur/pact)
- [BAZAAR - Evaluating LLMs in Economic Decision-Making within a Competitive Simulated Market](https://github.com/lechmazur/bazaar)
- [Public Goods Game (PGG) Benchmark: Contribute & Punish](https://github.com/lechmazur/pgg_bench/)
- [Elimination Game: Social Reasoning and Deception in Multi-Agent LLMs](https://github.com/lechmazur/elimination_game/)
- [Step Race: Collaboration vs. Misdirection Under Pressure](https://github.com/lechmazur/step_game/)

## Other benchmarks
- [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization/)
- [LLM Creative Story-Writing Benchmark](https://github.com/lechmazur/writing/)
- [LLM Round‑Trip Translation Benchmark](https://github.com/lechmazur/translation/)
- [Mapping LLM Style and Range in Flash Fiction](https://github.com/lechmazur/writing_styles)
- [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/)
- [LLM Deceptiveness and Gullibility](https://github.com/lechmazur/deception/)
- [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent/)

---

## Updates

- November 17, 2026: ByteDance Seed2.1 Pro added.
- November 17, 2026: GPT-6.2 Astra (high) and GPT-6.2 Sol (high) added.
- November 15, 2026: Qwen 4 Max (high) added.
- November 10, 2026: Gemini 4 Carbon (high reasoning) added.
- November 10, 2026: Claude Fable 5.2 (high reasoning) added.
- November 10, 2026: GPT-6.1 Terra (high reasoning) added.
- November 10, 2026: Tencent Hy4 (high) added.
- November 10, 2026: Step 5 Preview (high reasoning) added.
- November 10, 2026: Muse Spark Open (high reasoning) added.
- October 23, 2026: Kimi K3.1 Pro (high reasoning) added.
- October 20, 2026: GPT-6 Astra and GPT-6.1 Sol (max reasoning) added.
- October 19, 2026: MiniMax M3.1 Flash and DeepSeek V4.1 Flash 1017 (high reasoning) added.
- October 13, 2026: Gemini 4 Argon (high reasoning) added.
- October 12, 2026: Muse Wonder 1.0 (high reasoning) added.
- October 8, 2026: Claude Haiku 5.5 (high reasoning) added.
- October 7, 2026: Claude Sonnet 5.5 (high reasoning) added.
- October 6, 2026: Mistral Large 4 (high reasoning) and GPT-6.1 Sol (high reasoning) added.
- September 22, 2026: GPT-6 Sol and Luna (high reasoning) added.
- September 22, 2026: Claude Opus 5.5 (high reasoning) added.
- September 22, 2026: Grok 4.7 (high reasoning) added.
- September 10, 2026: DeepSeek V4.1 Flash high added.
- September 4, 2026: GPT-6 Astra high and xhigh added.
- September 2, 2026: Gemini 3.8 Flash high and Muse Spark 1.3 high added.
- September 1, 2026: Claude Fable 5.1 high and Tencent Hy4 Preview added.
- August 22, 2026: Muse Spark 1.2 high, GLM-5.3 high, Qwen3.8-27B, and Tencent Hy3 high and non-thinking added.
- August 14, 2026: Gemini 3.7 Flash added.
- August 13, 2026: Grok 4.6 high/xhigh and DeepSeek V4 Pro high added.
- August 4, 2026: Qwen 3.8 Max added with verified pricing.
- August 1, 2026: Gemini 3.6 Flash, Gemini 3.5 Flash-Lite high, Qwen 3.7 Flash, Qwen 3.7 Plus, and Qwen3.6-35B-A3B added; DeepSeek V4 Flash refreshed for V4-Flash-0731.
- July 24, 2026: Claude Opus 5 high and xhigh added; headline scoring changed to quadratic-v1.
- July 17, 2026: Kimi K3 added.
- July 9, 2026: GPT-5.6 high/xhigh/Luna/Terra and Muse Spark 1.1 high added.
- June 30, 2026: Claude Sonnet 5 high reasoning added.
- June 19, 2026: GLM-5.2 high reasoning, Claude Fable 5, and MiniMax-M3 added.
- May 29, 2026: Step 3.7 Flash added.
- May 28, 2026: Claude Opus 4.8 added.
- May 22, 2026: Qwen 3.7 Max added.
- May 19, 2026: Gemini 3.5 Flash added.
- May 12, 2026: Baidu ERNIE 5.1 added
- May 1, 2026: Grok 4.3 added
- April 29, 2026: Mistral Medium 3.5, Nemotron 3 Super added
- April 25, 2026: GPT-5.5, Kimi K2.6, Ling 2.6 1T, Tencent Hy3 Preview, DeepSeek V4 Pro, DeepSeek V4 Flash, Qwen 3.6 Max Preview added.
- April 16, 2026: Claude Opus 4.7 added.
- April 15, 2026: GLM-5.1, Step 3.5 Flash, Qwen3.5-27B added.
- April 6, 2026: GPT 5.4 (high), Gemma 4 31B Reasoning, Qwen3.5-122B-A10B added.
- April 4, 2026: MiniMax-M2.7 added.
- April 3, 2026: Arcee Trinity Large Thinking, Qwen 3.6 Plus, Gemma 4 31B added.
- Mar 6, 2026: Grok 4.20 Beta Experminatal, Gemini 3.1 Flash-Lite Preview added.
- Mar 5, 2026: GPT-5.4 added.
- Feb 23, 2026: GLM-5 added.
- Feb 20, 2026: Gemini 3.1 Pro Preview, ByteDance Seed2.0 Pro, Baidu Ernie 5.0 added.
- Feb 17, 2026: Claude Sonnet 4.6, Qwen3.5-397B-A17B, MiniMax-M2.5 added.
- Feb 6, 2026: Claude Opus 4.6 added.
- Feb 2, 2026: 940 total puzzles. Kimi K2.5 Thinking, Qwen3 Max (2026-01-23), MiniMax-M2.1, DeepSeek V3.2 added.
- Dec 17, 2025: Gemini 3 Flash Preview added.
- Dec 12, 2025: GPT 5.2 xhigh, GPT 5.2 Pro added.
- Dec 11, 2025: GPT 5.2 added.
- Dec 2, 2025: Mistral Large 3 added.
- Nov 24, 2025: Claude Opus 4.5 added.
- Nov 21, 2025: Grok 4.1 Fast added.
- Nov 18, 2025: Gemini 3 Pro Preview, GPT 5.1 added
- Nov 12, 2025: Kimi K2 Thinking added.
- Oct 15, 2025: Claude Haiku 4.5 added.
- Oct 14, 2025: Claude Sonnet 4.5, Deepseek V3.2 Exp, GLM-4.6 added.
- Sep 19, 2025: Grok 4 Fast, Qwen 3 Next 80B A3B Thinking, LongCat Flash Chat added.
- Sep 6, 2025: Kimi K2-0905 added.
- Sep 5, 2025: Qwen 3 Max Preview, Qwen 3 235B A22B 25-07 Instruct added.
- Aug 23, 2025: GPT-5 high reasoning and Cohere Command A Reasoning (16K) added.
- Aug 22, 2025: DeepSeek 3.1, Qwen 3 30B A3B 25-07, Mistral Medium 3.1, GPT-5 minimal and low reasoning added.
- Aug 7, 2025: GPT-5 added.
- Aug 5, 2025: Claude Opus 4.1, GPT-OSS-120B added.
- July 28, 2025: GLM-4.5, Qwen 3 235B A22B 25-07 Thinking added.
- July 14, 2025: 108 new puzzles added. Kimi K2 added.
- July 10, 2025: Grok 4 added.
- July 3, 2025: Qwen 3 32B, GLM4-32B-0414 added.
- July 2, 2025: Baidu Ernie 4.5 300B A47B, MiniMax-M1, Mistral Small 3.2 added.
- June 10, 2025: o3-pro added.
- June 5, 2025: Gemini 2.5 Pro Preview 06-05 added.
- May 28, 2025: DeepSeek R1 05/28 added.
- May 22, 2025: Claude 4 models added.
- May 7, 2025: Gemini 2.5 Pro Preview 05-06 added. Mistral Medium 3 added.
- Apr 30, 2025: Qwen 3 added.
- Apr 18, 2025: o3, o4-mini, Gemini 2.5 Flash Preview added.
- Apr 15, 2025: GPT-4.1 added.
- Apr 10, 2025: Grok 3 added.
- Apr 5, 2025: Llama 4 Maverick, Llama 4 Scout added.
- Mar 28, 2025: GPT-4o March 2025 added.
- Mar 25, 2025: 50 new questions added. Gemini 2.5 Pro Exp 03-25 and DeepSeek V3-0324 added.
- Mar 23, 2025: Humans vs. LLMs section added.
- Mar 21, 2025: o1-pro added. o3-mini-high added.
- Mar 17, 2025: Cohere Command A and Mistral Small 3.1 added.
- Mar 12, 2025: Gemma 3 27B added.
- Mar 7, 2025: Qwen QwQ added.
- Feb 27, 2025: GPT-4.5 Preview added.
- Feb 24, 2025: Claude 3.7 Sonnet Thinking, Clade 3.7 Sonnet, GPT-4o Feb 2025, Qwen 2.5 Max, GPT-4o 2024-11-20 added.
- Feb 6, 2025: Gemini 2.0 Pro Exp 02-05 added.
- Feb 4, 2025: A new, more challenging version with extra words in each puzzle. Separate scoring for the 100 newest questions. Correlation heatmap.
- Jan 31, 2025: o3-mini (72.4) added.
- Jan 30, 2025: Mistral Small 3 (10.5) added.
- Jan 29, 2025: DeepSeek R1 (54.5) added.
- Jan 28, 2025: Qwen 2.5 Max (18.6) added.
- Jan 22, 2025: Phi-4 (11.6), Nova Pro (12.5), Gemini 2.0 Flash Thinking Exp 01-21 (37.0) added.
- Jan 16, 2025: Gemini 2.0 Flash Thinking Exp, o1, MiniMax-Tex-o1 added. Gemini 2.0 Flash Thinking Exp sometimes hits the output token limit.
- Dec 27, 2024: GPT-4o 2024-11-20, Llama 3.3 70B, Gemini 2.0 Flash Exp, Deepseek-V3 added. Gemini 2.0 Flash Thinking Exp could not be benchmarked because its output gets cut off for some puzzles.
- Claude 3.5 Haiku added. 13.7.
- Claude 3.5 Sonnet (2024-10-22) added. Improves from 25.9 from 24.4.
- Grok Beta added. Improves from 21.3 to 23.7. It's described as "experimental language model with state-of-the-art reasoning capabilities, best for complex and multi-step use cases. It is the successor of Grok 2 with enhanced context length."
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.
