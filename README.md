# Extended Version

This benchmark evaluates large language models (LLMs) using 651 NYT Connections puzzles, with additional words included to increase difficulty.

As of Feb 4, 2025, there is a new version of the benchmark. The standard NYT Connections benchmark is nearing saturation, with o1 scoring 90.7 and o3, along with other reasoning models, expected this year. The current rules require knowing only three categories, letting the fourth fall into place. To increase difficulty, Extended Connections adds up to four extra trick words to each puzzle. We double-check that none of the added words fit into any category used in the corresponding puzzle. New puzzles have expanded the total from 436 to 651. Rankings changed little, but the benchmark is now ready for o3. 

### Chart: Extended Version

![Leaderboard](images/nyt_connections_chart.png)

### Leaderboard: Extended Version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1-pro (medium reasoning)|82.5|
|2|o3 (high reasoning)|79.5|
|3|o4-mini (high reasoning)|74.7|
|4|o3 (medium reasoning)|74.0|
|5|o1 (medium reasoning)|70.8|
|6|o4-mini (medium reasoning)|68.8|
|7|o3-mini (high reasoning)|61.4|
|8|Qwen 3 235B A22B|55.7|
|9|Gemini 2.5 Pro Exp 03-25|54.1|
|10|o3-mini (medium reasoning)|53.6|
|11|Gemini 2.5 Pro Preview 05-06|42.5|
|12|DeepSeek R1|38.6|
|13|Qwen 3 30B A3B|38.1|
|14|GPT-4.5 Preview|34.2|
|15|Claude 3.7 Sonnet Thinking 16K|33.6|
|16|Qwen QwQ-32B 16K|31.4|
|17|Grok 3 Mini Beta (high)|30.9|
|18|o1-mini|27.0|
|19|Grok 3 Mini Beta (low)|26.0|
|20|Gemini 2.5 Flash Preview (24k)|25.8|
|21|Quasar Alpha|25.4|
|22|GPT-4o Mar 2025|25.2|
|23|GPT-4.1|23.6|
|24|Gemini 2.0 Flash Think Exp 01-21|23.1|
|25|GPT-4o Feb 2025|22.7|
|26|Gemini 2.0 Pro Exp 02-05|21.7|
|27|Grok 3 Beta (no reasoning)|20.3|
|28|Grok 2 12-12|19.2|
|29|Gemini 1.5 Pro (Sept)|19.2|
|30|Claude 3.7 Sonnet|19.2|
|31|Claude 3 Opus|19.2|
|32|Llama 4 Maverick|19.1|
|33|Gemini 2.0 Flash|18.8|
|34|GPT-4o 2024-11-20|18.7|
|35|Qwen 2.5 Max|18.0|
|36|Llama 4 Scout|17.9|
|37|GPT-4o 2024-08-06|17.8|
|38|Claude 3.5 Sonnet 2024-10-22|17.7|
|39|DeepSeek V3-0324|17.4|
|40|Llama 3.1 405B|16.2|
|41|DeepSeek V3|15.1|
|42|Llama 3.3 70B|15.1|
|43|GPT-4.1 mini|15.1|
|44|MiniMax-Text-01|14.6|
|45|Cohere Command A|13.6|
|46|Mistral Medium 3|12.9|
|47|Mistral Large 2|12.6|
|48|Gemma 2 27B|12.2|
|49|Gemma 3 27B|11.8|
|50|Mistral Small 3.1|11.4|
|51|Qwen 2.5 72B|11.1|
|52|Claude 3.5 Haiku|10.3|
|53|Microsoft Phi-4|10.2|
|54|Amazon Nova Pro|10.1|
|55|GPT-4o mini|9.9|
|56|Mistral Small 3|8.9|
|57|GPT-4.1 nano|8.6|
|58|Claude 3 Haiku|2.2|


---
### Correlation of puzzle-level results: heatmap

![Correlations](images/llm_puzzle_corr.png)

---
## Newest 100 puzzles. 

To counteract the possibility of an LLM's training data including the solutions, we have also tested only the 100 latest puzzles. Note that lower scores do not necessarily indicate that NYT Connections solutions are in the training data, as the difficulty of the first puzzles was lower.

---
### Chart: Newest 100 puzzles, extended version

![Newest 100 puzzles](images/nyt_connections_chart_latest100.png)


### Leaderboard: Newest 100 puzzles, extended version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1-pro (medium reasoning)|81.5|
|2|o3 (high reasoning)|80.0|
|3|o3 (medium reasoning)|76.8|
|4|o4-mini (high reasoning)|75.5|
|5|o1 (medium reasoning)|70.2|
|6|o4-mini (medium reasoning)|69.8|
|7|o3-mini (high reasoning)|60.2|
|8|Qwen 3 235B A22B|55.2|
|9|o3-mini (medium reasoning)|53.2|
|10|Gemini 2.5 Pro Exp 03-25|49.8|
|11|DeepSeek R1|37.8|
|12|Gemini 2.5 Pro Preview 05-06|36.2|
|13|Qwen 3 30B A3B|35.2|
|14|Qwen QwQ-32B 16K|34.8|
|15|GPT-4.5 Preview|33.2|
|16|Claude 3.7 Sonnet Thinking 16K|31.2|
|17|Grok 3 Mini Beta (high)|31.0|
|18|Grok 3 Mini Beta (low)|27.5|
|19|o1-mini|27.5|
|20|Gemini 2.5 Flash Preview (24k)|25.5|
|21|Gemini 2.0 Flash Think Exp 01-21|23.5|
|22|GPT-4.1|23.0|
|23|Quasar Alpha|23.0|
|24|GPT-4o Mar 2025|22.2|
|25|Qwen 2.5 Max|21.5|
|26|Gemini 2.0 Pro Exp 02-05|20.8|
|27|Grok 3 Beta (no reasoning)|20.8|
|28|Llama 4 Maverick|20.5|
|29|GPT-4o Feb 2025|20.0|
|30|DeepSeek V3-0324|19.5|
|31|Llama 4 Scout|19.0|
|32|Llama 3.1 405B|18.8|
|33|Claude 3.7 Sonnet|18.2|
|34|Claude 3 Opus|18.2|
|35|Gemini 2.0 Flash|18.0|
|36|Llama 3.3 70B|17.2|
|37|Claude 3.5 Sonnet 2024-10-22|16.8|
|38|GPT-4.1 mini|16.2|
|39|DeepSeek V3|15.8|
|40|Grok 2 12-12|15.2|
|41|MiniMax-Text-01|14.0|
|42|Cohere Command A|13.2|
|43|Gemini 1.5 Pro (Sept)|12.5|
|44|GPT-4o 2024-08-06|12.0|
|45|GPT-4o 2024-11-20|12.0|
|46|Gemma 3 27B|11.8|
|47|Mistral Medium 3|11.5|
|48|Qwen 2.5 72B|11.2|
|49|Gemma 2 27B|10.8|
|50|Mistral Large 2|10.8|
|51|Mistral Small 3.1|10.8|
|52|Microsoft Phi-4|10.8|
|53|GPT-4o mini|10.5|
|54|Claude 3.5 Haiku|10.5|
|55|Amazon Nova Pro|10.0|
|56|GPT-4.1 nano|8.2|
|57|Mistral Small 3|5.0|
|58|Claude 3 Haiku|1.5|




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

This benchmark evaluates large language models (LLMs) using 436 NYT Connections puzzles. Three different prompts, not optimized for LLMs through prompt engineering, are used. Both uppercase and lowercase puzzles are assessed.

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

---

## Notes
- A temperature setting of 0 was used
- Partial credit is awarded if the puzzle isn't completely solved. 
- Only one attempt is allowed per puzzle. Humans solving puzzles on the NYT website get four attempts and a notification when they're one step away from the solution.
- Multi-turn ensemble is my unpublished system. It utilizes multiple LLMs, multi-turn dialogues, and other proprietary techniques. It is slower and more costly to run but it does very well. It [outperforms](https://x.com/LechMazur/status/1828804485033992514/photo/1) non-o1 LLMs on MMLU-Pro and GPQA.
- This benchmark is not affiliated with the New York Times

---

## Other multi-agent benchmarks
- [Public Goods Game (PGG) Benchmark: Contribute & Punish](https://github.com/lechmazur/pgg_bench/)
- [Elimination Game: Social Reasoning and Deception in Multi-Agent LLMs](https://github.com/lechmazur/elimination_game/)
- [Step Race: Collaboration vs. Misdirection Under Pressure](https://github.com/lechmazur/step_game/)

## Other benchmarks
- [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization/)
- [LLM Creative Story-Writing Benchmark](https://github.com/lechmazur/writing/)
- [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/)
- [LLM Deceptiveness and Gullibility](https://github.com/lechmazur/deception/)
- [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent/)

---

## Updates
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

