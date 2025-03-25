# Extended Version

As of Feb 4, 2025, there is a new version of the benchmark. The standard NYT Connections benchmark is nearing saturation, with o1 scoring 90.7 and o3, along with other reasoning models, expected this year. The current rules require knowing only three categories, letting the fourth fall into place. To increase difficulty, Extended Connections adds up to four extra trick words to each puzzle. We double-check that none of the added words fit into any category used in the corresponding puzzle.  New puzzles have expanded the total from 436 to 601. Rankings changed little, but the benchmark is now ready for o3. 

### Chart: Extended Version

![nyt_connections_chart](https://github.com/user-attachments/assets/3b626f23-5d44-43af-ad70-55a1935be0e4)

### Leaderboard: Extended Version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1-pro (medium reasoning)|82.3|
|2|o1 (medium reasoning)|70.8|
|3|o3-mini-high|61.4|
|4|Gemini 2.5 Pro Exp 03-25|54.1|
|5|o3-mini (medium reasoning)|53.6|
|6|DeepSeek R1|38.6|
|7|GPT-4.5 Preview|34.2|
|8|Claude 3.7 Sonnet Thinking 16K|33.6|
|9|Qwen QwQ-32B 16K|31.4|
|10|o1-mini|27.0|
|11|Gemini 2.0 Flash Think Exp 01-21|23.1|
|12|GPT-4o Feb 2025|22.7|
|13|Gemini 2.0 Pro Exp 02-05|21.7|
|14|Grok 2 12-12|19.2|
|15|Gemini 1.5 Pro (Sept)|19.2|
|16|Claude 3.7 Sonnet|19.2|
|17|Claude 3 Opus|19.2|
|18|Gemini 2.0 Flash|18.8|
|19|GPT-4o 2024-11-20|18.7|
|20|Qwen 2.5 Max|18.0|
|21|GPT-4o 2024-08-06|17.8|
|22|Claude 3.5 Sonnet 2024-10-22|17.7|
|23|DeepSeek V3-0324|17.4|
|24|Llama 3.1 405B|16.2|
|25|DeepSeek V3|15.1|
|26|Llama 3.3 70B|15.1|
|27|MiniMax-Text-01|14.6|
|28|Cohere Command A|13.6|
|29|Mistral Large 2|12.6|
|30|Gemma 2 27B|12.2|
|31|Gemma 3 27B|11.8|
|32|Mistral Small 3.1|11.4|
|33|Qwen 2.5 72B|11.1|
|34|Claude 3.5 Haiku|10.3|
|35|Microsoft Phi-4|10.2|
|36|Amazon Nova Pro|10.1|
|37|GPT-4o mini|9.9|
|38|Mistral Small 3|8.9|
|39|Claude 3 Haiku|2.2|

---
### Correlation of puzzle-level results: heatmap

![llm_puzzle_corr](https://github.com/user-attachments/assets/c33b674c-4c5d-4b6a-8a20-9ece06c8b2a7)

---
## Newest 100 puzzles. 

To counteract the possibility of an LLM's training data including the solutions, we have also tested only the 100 latest puzzles. Note that lower scores do not necessarily indicate that NYT Connections solutions are in the training data, as the difficulty of the first puzzles was lower.

---
### Chart: Newest 100 puzzles, extended version

![nyt_connections_chart_latest100](https://github.com/user-attachments/assets/6663a3e1-ee17-421d-bf7e-af89fa0224b8)


### Leaderboard: Newest 100 puzzles, extended version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1-pro (medium reasoning)|80.4|
|2|o1 (medium reasoning)|70.2|
|3|o3-mini-high|60.2|
|4|o3-mini (medium reasoning)|53.2|
|5|Gemini 2.5 Pro Exp 03-25|49.8|
|6|DeepSeek R1|37.8|
|7|Qwen QwQ-32B 16K|34.8|
|8|GPT-4.5 Preview|33.2|
|9|Claude 3.7 Sonnet Thinking 16K|31.2|
|10|o1-mini|27.5|
|11|Gemini 2.0 Flash Think Exp 01-21|23.5|
|12|Qwen 2.5 Max|21.5|
|13|Gemini 2.0 Pro Exp 02-05|20.8|
|14|GPT-4o Feb 2025|20.0|
|15|DeepSeek V3-0324|19.5|
|16|Llama 3.1 405B|18.8|
|17|Claude 3.7 Sonnet|18.2|
|18|Claude 3 Opus|18.2|
|19|Gemini 2.0 Flash|18.0|
|20|Llama 3.3 70B|17.2|
|21|Claude 3.5 Sonnet 2024-10-22|16.8|
|22|DeepSeek V3|15.8|
|23|Grok 2 12-12|15.2|
|24|MiniMax-Text-01|14.0|
|25|Cohere Command A|13.2|
|26|Gemini 1.5 Pro (Sept)|12.5|
|27|GPT-4o 2024-08-06|12.0|
|28|GPT-4o 2024-11-20|12.0|
|29|Gemma 3 27B|11.8|
|30|Qwen 2.5 72B|11.2|
|31|Gemma 2 27B|10.8|
|32|Mistral Large 2|10.8|
|33|Mistral Small 3.1|10.8|
|34|Microsoft Phi-4|10.8|
|35|GPT-4o mini|10.5|
|36|Claude 3.5 Haiku|10.5|
|37|Amazon Nova Pro|10.0|
|38|Mistral Small 3|5.0|
|39|Claude 3 Haiku|1.5|

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

