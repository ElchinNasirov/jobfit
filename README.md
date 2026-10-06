# JobFit

Local agent that reads job descriptions and a resume, searches each company, scores fit, and prints a ranking.

No paid API. The model is Llama 3.2 through Ollama on the same machine.

## What it does

1. Extract skills that appear in the job text.
2. Search the web for the company.
3. Score the resume 0–100 and draft 5 bullets.
4. Repeat for three sample jobs and print a rank by score.

Sample jobs live in `data.py`: a robotics agent role, a frontend role, and an AI engineer role. The resume is one string.

## Run

uv run python jobfit.py

Requires Ollama running and `ollama pull llama3.2`.

## Files

- data.py — resume and three sample jobs
- search.py — DuckDuckGo company search
- llm.py — one call to the local model
- jobfit.py — prompts, loop, and ranking
- index.html — static explanation page, no model call

## What failed

Llama 3.2 does not follow every rule on every run. The rank is a demo, not a decision.

- Scores drift. A thin resume has scored 55, 75, and 85 on jobs where required skills were missing.
- It changes "Finishing" to "Completed".
- It invents experience, including "developed learning agents".
- It can mark Python missing when the resume lists Python.
- Company search sometimes returns a different company with the same name.

Those slips are why the next step is a check in code, not a longer prompt.