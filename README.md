# NYT Connections LLM Benchmark

This benchmark evaluates large language models (LLMs) using 436 NYT Connections puzzles. Three different prompts, not optimized for LLMs through prompt engineering, are used. Both uppercase and lowercase puzzles are assessed.

# Chart

![bab3e552d42c8a0ca10fa5665e02cad6b4b15e2fcb259e3ee86ae493bf4792fc](https://github.com/user-attachments/assets/f17b50fd-8160-459a-ac11-8777848670c5)

## Leaderboard

| Model | Score |
| --- | --- |
| o1-preview | 87.1
| o1-mini | 42.2
| Multi-turn ensemble | 37.8
| GPT-4 Turbo | 28.3
| GPT-4o | 26.5
| Llama 3.1 405B | 26.3
| Claude 3 Opus | 24.8
| Claude 3.5 Sonnet | 24.4
| Gemini 1.5 Pro (Sept) | 22.7
| Grok 2 | 21.3
| Gemma 2 27B | 18.8
| Mistral Large 2 | 17.4
| Qwen 2.5 72B | 14.8
| DeepSeek-V2.5 | 9.9

## Notes
- A temperature setting of 0 was used
- Partial credit is awarded if the puzzle isn't completely solved. 
- Only one attempt is allowed per puzzle. Humans solving puzzles on the NYT website get four attempts and a notification when they're one step away from the solution.
- Multi-turn ensemble is my unpublished system. It utilizes multiple LLMs, multi-turn dialogues, and other proprietary techniques. It is slower and more costly to run but it does very well. It [outperforms](https://x.com/LechMazur/status/1828804485033992514/photo/1) non-o1 LLMs on MMLU-Pro and GPQA.

## Updates and Other Benchmarks
Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.

