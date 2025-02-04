# NYT Connections LLM Benchmark

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

# Extended Version

As of Feb 4, 2025, there is a new version of the benchmark. The standard NYT Connections benchmark is nearing saturation, with o1 scoring 90.7 and o3, along with other reasoning models, expected this year. The current rules require knowing only three categories, letting the fourth fall into place. To increase difficulty, Extended Connections adds up to four extra trick words to each puzzle. We double-check that none of the added words fit into any category used in the corresponding puzzle.  New puzzles have expanded the total from 436 to 601. Rankings changed little, but the benchmark is now ready for o3. 

### Chart: Extended Version

![nyt_connections_chart](https://github.com/user-attachments/assets/0205091e-b980-4c7d-8cb4-54afeac231ac)

### Leaderboard: Extended Version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1|69.7|
|2|o3-mini|52.5|
|3|DeepSeek R1|37.6|
|4|o1-mini|26.4|
|5|Gemini 2.0 Flash Think Exp 01-21|22.5|
|6|Grok 2 12-12|19.3|
|7|Gemini 1.5 Pro (Sept)|19.2|
|8|Gemini 1.5 Flash|19.1|
|9|Claude 3 Opus|18.9|
|10|GPT-4o|17.8|
|11|Gemini 2.0 Flash Exp|17.6|
|12|Claude 3.5 Sonnet 2024-10-22|17.6|
|13|Qwen 2.5 Max|17.3|
|14|Llama 3.1 405B|15.6|
|15|DeepSeek-V3|14.9|
|16|Llama 3.3 70B|14.7|
|17|MiniMax-Text-01|14.4|
|18|Mistral Large 2|12.5|
|19|Gemma 2 27B|12.0|
|20|Qwen 2.5 72B|10.9|
|21|Claude 3.5 Haiku|10.0|
|22|Amazon Nova Pro|9.9|
|23|Microsoft Phi-4|9.8|
|24|GPT-4o mini|9.6|
|25|Mistral Small 3|8.9|
|26|Claude 3 Haiku|2.2|

### Correlation of puzzle-level results: heatmap

![llm_puzzle_corr](https://github.com/user-attachments/assets/f8d1211e-4cae-4a67-9ca6-46bc6f100cb5)

## Newest 100 puzzles. 

To counteract the possibility of an LLM's training data including the solutions, we have also tested only the 100 latest puzzles. Note that lower scores do not necessarily indicate that NYT Connections solutions are in the training data, as the difficulty of the first puzzles was lower.

### Chart: Newest 100 puzzles, extended version

![nyt_connections_chart_latest100](https://github.com/user-attachments/assets/281c72c1-d96a-4e39-b7a2-f81abc7e5e7d)

### Leaderboard: Newest 100 puzzles, extended version

|Rank|Model|Score(%)|
|---:|-----|-------:|
|1|o1|60.0|
|2|o3-mini|42.8|
|3|DeepSeek R1|28.7|
|4|o1-mini|18.8|
|5|Gemini 2.0 Flash Think Exp 01-21|15.2|
|6|Qwen 2.5 Max|13.8|
|7|Gemini 2.0 Flash Exp|13.5|
|8|Llama 3.1 405B|13.2|
|9|Claude 3 Opus|12.8|
|10|DeepSeek-V3|12.2|
|11|GPT-4o|12.0|
|12|Gemini 1.5 Flash|11.5|
|13|MiniMax-Text-01|11.2|
|14|Claude 3.5 Sonnet 2024-10-22|11.2|
|15|Gemini 1.5 Pro (Sept)|11.0|
|16|Grok 2 12-12|11.0|
|17|Llama 3.3 70B|10.8|
|18|Gemma 2 27B|8.2|
|19|Qwen 2.5 72B|8.0|
|20|Mistral Large 2|7.0|
|21|Claude 3.5 Haiku|6.5|
|22|Amazon Nova Pro|6.5|
|23|Microsoft Phi-4|6.0|
|24|GPT-4o mini|5.2|
|25|Mistral Small 3|3.5|
|26|Claude 3 Haiku|1.2|


## Notes
- A temperature setting of 0 was used
- Partial credit is awarded if the puzzle isn't completely solved. 
- Only one attempt is allowed per puzzle. Humans solving puzzles on the NYT website get four attempts and a notification when they're one step away from the solution.
- Multi-turn ensemble is my unpublished system. It utilizes multiple LLMs, multi-turn dialogues, and other proprietary techniques. It is slower and more costly to run but it does very well. It [outperforms](https://x.com/LechMazur/status/1828804485033992514/photo/1) non-o1 LLMs on MMLU-Pro and GPQA.
- This benchmark is not affiliated with the New York Times

## Updates and Other Benchmarks
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
- Also check out the [LLM Step Game](https://github.com/lechmazur/step_game), [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization), [LLM Creative Story-Writing Benchmark](https://github.com/lechmazur/writing), [LLM Confabulations ](https://github.com/lechmazur/confabulations/),  [LLM Deceptiveness and Gullibility Benchmark](https://github.com/lechmazur/deception), and [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent).
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.

