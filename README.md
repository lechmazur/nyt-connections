# NYT Connections LLM Benchmark

This benchmark evaluates large language models (LLMs) using 436 NYT Connections puzzles. Three different prompts, not optimized for LLMs through prompt engineering, are used. Both uppercase and lowercase puzzles are assessed.

# Chart

![NYT Connections (436 puzzles)_ (7)](https://github.com/user-attachments/assets/58b0eee2-6e5e-4493-a96e-4dc9949d506e)

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
| Grok Beta | 23.7
| Gemini 1.5 Pro (Sept) | 22.7
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
- Grok Beta added. Improves from 21.3 to 23.7. It's described as "experimental language model with state-of-the-art reasoning capabilities, best for complex and multi-step use cases. It is the successor of Grok 2 with enhanced context length."
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.

