# Extended Version

As of Feb 4, 2025, there is a new version of the benchmark. The standard NYT Connections benchmark is nearing saturation, with o1 scoring 90.7 and o3, along with other reasoning models, expected this year. The current rules require knowing only three categories, letting the fourth fall into place. To increase difficulty, Extended Connections adds up to four extra trick words to each puzzle. We double-check that none of the added words fit into any category used in the corresponding puzzle.  New puzzles have expanded the total from 436 to 601. Rankings changed little, but the benchmark is now ready for o3. 

### Chart: Extended Version

![nyt_connections_chart](https://github.com/user-attachments/assets/b06f9b61-80fd-4c43-937c-e3a09a7659aa)

### Leaderboard: Extended Version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1 (medium reasoning)|69.7|
|2|o3-mini (medium reasoning)|52.5|
|3|DeepSeek R1|37.7|
|4|GPT-4.5 Preview|33.7|
|5|Claude 3.7 Sonnet Thinking 16K|33.5|
|6|Qwen QwQ-32B 16K|30.3|
|7|o1-mini|26.4|
|8|Gemini 2.0 Flash Think Exp 01-21|22.5|
|9|GPT-4o Feb 2025|22.4|
|10|Gemini 2.0 Pro Exp 02-05|21.2|
|11|Grok 2 12-12|19.3|
|12|Gemini 1.5 Pro (Sept)|19.2|
|13|Claude 3.7 Sonnet|18.9|
|14|Claude 3 Opus|18.9|
|15|GPT-4o 2024-11-20|18.7|
|16|Gemini 2.0 Flash|18.3|
|17|GPT-4o 2024-08-06|17.8|
|18|Claude 3.5 Sonnet 2024-10-22|17.6|
|19|Qwen 2.5 Max|17.3|
|20|Llama 3.1 405B|15.7|
|21|DeepSeek-V3|14.9|
|22|Llama 3.3 70B|14.7|
|23|MiniMax-Text-01|14.4|
|24|Cohere Command A|13.2|
|25|Mistral Large 2|12.5|
|26|Gemma 2 27B|12.0|
|27|Gemma 3 27B|11.6|
|28|Mistral Small 3.1|11.2|
|29|Qwen 2.5 72B|10.9|
|30|Claude 3.5 Haiku|10.0|
|31|Amazon Nova Pro|9.9|
|32|Microsoft Phi-4|9.8|
|33|GPT-4o mini|9.6|
|34|Mistral Small 3|8.9|
|35|Claude 3 Haiku|2.2|


### Correlation of puzzle-level results: heatmap

![llm_puzzle_corr](https://github.com/user-attachments/assets/dfd673ec-eb3b-42b9-9249-5724e9a52acd)


## Newest 100 puzzles. 

To counteract the possibility of an LLM's training data including the solutions, we have also tested only the 100 latest puzzles. Note that lower scores do not necessarily indicate that NYT Connections solutions are in the training data, as the difficulty of the first puzzles was lower.

### Chart: Newest 100 puzzles, extended version

![nyt_connections_chart_latest100](https://github.com/user-attachments/assets/1274547d-3cb0-4ea9-a484-4a1d91371293)


### Leaderboard: Newest 100 puzzles, extended version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1 (medium reasoning)|60.0|
|2|o3-mini (medium reasoning)|42.8|
|3|DeepSeek R1|29.2|
|4|Claude 3.7 Sonnet Thinking 16K|27.0|
|5|GPT-4.5 Preview|24.2|
|6|Qwen QwQ-32B 16K|24.2|
|7|o1-mini|18.8|
|8|Gemini 2.0 Flash Think Exp 01-21|15.2|
|9|GPT-4o Feb 2025|14.8|
|10|Qwen 2.5 Max|13.8|
|11|Llama 3.1 405B|13.5|
|12|Gemini 2.0 Flash|12.8|
|13|Claude 3 Opus|12.8|
|14|GPT-4o 2024-11-20|12.5|
|15|Claude 3.7 Sonnet|12.2|
|16|DeepSeek-V3|12.2|
|17|Gemini 2.0 Pro Exp 02-05|12.2|
|18|GPT-4o 2024-08-06|12.0|
|19|MiniMax-Text-01|11.2|
|20|Claude 3.5 Sonnet 2024-10-22|11.2|
|21|Gemini 1.5 Pro (Sept)|11.0|
|22|Grok 2 12-12|11.0|
|23|Llama 3.3 70B|10.8|
|24|Cohere Command A|8.8|
|25|Gemma 2 27B|8.2|
|26|Qwen 2.5 72B|8.0|
|27|Gemma 3 27B|7.2|
|28|Mistral Large 2|7.0|
|29|Mistral Small 3.1|7.0|
|30|Claude 3.5 Haiku|6.5|
|31|Amazon Nova Pro|6.5|
|32|Microsoft Phi-4|6.0|
|33|GPT-4o mini|5.2|
|34|Mistral Small 3|3.5|
|35|Claude 3 Haiku|1.2|

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


## Notes
- A temperature setting of 0 was used
- Partial credit is awarded if the puzzle isn't completely solved. 
- Only one attempt is allowed per puzzle. Humans solving puzzles on the NYT website get four attempts and a notification when they're one step away from the solution.
- Multi-turn ensemble is my unpublished system. It utilizes multiple LLMs, multi-turn dialogues, and other proprietary techniques. It is slower and more costly to run but it does very well. It [outperforms](https://x.com/LechMazur/status/1828804485033992514/photo/1) non-o1 LLMs on MMLU-Pro and GPQA.
- This benchmark is not affiliated with the New York Times

## Updates and Other Benchmarks
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
- Also check out the [Multi-Agent Elimination Game LLM Benchmark](https://github.com/lechmazur/elimination_game/), [LLM Public Goods Game](https://github.com/lechmazur/goods), [LLM Step Game](https://github.com/lechmazur/step_game), [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization), [LLM Creative Story-Writing Benchmark](https://github.com/lechmazur/writing), [LLM Confabulations Benchmark](https://github.com/lechmazur/confabulations/),  [LLM Deceptiveness and Gullibility Benchmark](https://github.com/lechmazur/deception), and [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent).
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.

