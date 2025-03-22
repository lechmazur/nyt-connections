# Extended Version

As of Feb 4, 2025, there is a new version of the benchmark. The standard NYT Connections benchmark is nearing saturation, with o1 scoring 90.7 and o3, along with other reasoning models, expected this year. The current rules require knowing only three categories, letting the fourth fall into place. To increase difficulty, Extended Connections adds up to four extra trick words to each puzzle. We double-check that none of the added words fit into any category used in the corresponding puzzle.  New puzzles have expanded the total from 436 to 601. Rankings changed little, but the benchmark is now ready for o3. 

### Chart: Extended Version

![nyt_connections_chart](https://github.com/user-attachments/assets/9e44e8bf-8d2f-4ec9-8187-5bea974ccfa5)

### Leaderboard: Extended Version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1-pro (medium reasoning)|81.7|
|2|o1 (medium reasoning)|69.7|
|3|o3-mini (medium reasoning)|52.5|
|4|DeepSeek R1|37.7|
|5|GPT-4.5 Preview|33.7|
|6|Claude 3.7 Sonnet Thinking 16K|33.5|
|7|Qwen QwQ-32B 16K|30.3|
|8|o1-mini|26.4|
|9|Gemini 2.0 Flash Think Exp 01-21|22.5|
|10|GPT-4o Feb 2025|22.4|
|11|Gemini 2.0 Pro Exp 02-05|21.2|
|12|Grok 2 12-12|19.3|
|13|Gemini 1.5 Pro (Sept)|19.2|
|14|Claude 3.7 Sonnet|18.9|
|15|Claude 3 Opus|18.9|
|16|GPT-4o 2024-11-20|18.7|
|17|Gemini 2.0 Flash|18.3|
|18|GPT-4o 2024-08-06|17.8|
|19|Claude 3.5 Sonnet 2024-10-22|17.6|
|20|Qwen 2.5 Max|17.3|
|21|Llama 3.1 405B|15.7|
|22|DeepSeek-V3|14.9|
|23|Llama 3.3 70B|14.7|
|24|MiniMax-Text-01|14.4|
|25|Cohere Command A|13.2|
|26|Mistral Large 2|12.5|
|27|Gemma 2 27B|12.0|
|28|Gemma 3 27B|11.6|
|29|Mistral Small 3.1|11.2|
|30|Qwen 2.5 72B|10.9|
|31|Claude 3.5 Haiku|10.0|
|32|Amazon Nova Pro|9.9|
|33|Microsoft Phi-4|9.8|
|34|GPT-4o mini|9.6|
|35|Mistral Small 3|8.9|
|36|Claude 3 Haiku|2.2|


### Correlation of puzzle-level results: heatmap

![llm_puzzle_corr](https://github.com/user-attachments/assets/f5e8a982-807a-4268-b644-e0fc606597ca)


## Newest 100 puzzles. 

To counteract the possibility of an LLM's training data including the solutions, we have also tested only the 100 latest puzzles. Note that lower scores do not necessarily indicate that NYT Connections solutions are in the training data, as the difficulty of the first puzzles was lower.

### Chart: Newest 100 puzzles, extended version

![nyt_connections_chart_latest100](https://github.com/user-attachments/assets/3f148bdd-e658-4c8a-991f-1971231e2b75)



### Leaderboard: Newest 100 puzzles, extended version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1-pro (medium reasoning)|72.2|
|2|o1 (medium reasoning)|60.0|
|3|o3-mini (medium reasoning)|42.8|
|4|DeepSeek R1|29.2|
|5|Claude 3.7 Sonnet Thinking 16K|27.0|
|6|GPT-4.5 Preview|24.2|
|7|Qwen QwQ-32B 16K|24.2|
|8|o1-mini|18.8|
|9|Gemini 2.0 Flash Think Exp 01-21|15.2|
|10|GPT-4o Feb 2025|14.8|
|11|Qwen 2.5 Max|13.8|
|12|Llama 3.1 405B|13.5|
|13|Gemini 2.0 Flash|12.8|
|14|Claude 3 Opus|12.8|
|15|GPT-4o 2024-11-20|12.5|
|16|Claude 3.7 Sonnet|12.2|
|17|DeepSeek-V3|12.2|
|18|Gemini 2.0 Pro Exp 02-05|12.2|
|19|GPT-4o 2024-08-06|12.0|
|20|MiniMax-Text-01|11.2|
|21|Claude 3.5 Sonnet 2024-10-22|11.2|
|22|Gemini 1.5 Pro (Sept)|11.0|
|23|Grok 2 12-12|11.0|
|24|Llama 3.3 70B|10.8|
|25|Cohere Command A|8.8|
|26|Gemma 2 27B|8.2|
|27|Qwen 2.5 72B|8.0|
|28|Gemma 3 27B|7.2|
|29|Mistral Large 2|7.0|
|30|Mistral Small 3.1|7.0|
|31|Claude 3.5 Haiku|6.5|
|32|Amazon Nova Pro|6.5|
|33|Microsoft Phi-4|6.0|
|34|GPT-4o mini|5.2|
|35|Mistral Small 3|3.5|
|36|Claude 3 Haiku|1.2|

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
- Mar 21, 2025: o1-pro added.
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

