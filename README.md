# JobFit

Local agent that reads a job description and a resume, searches the company, and scores fit.

No paid API. The model is Llama 3.2 through Ollama on the same machine.

## What it does

1. Extract skills that appear in the job text.
2. Search the web for the company.
3. Score the resume 0–100 and draft 5 bullets.

## Run

uv run python jobfit.py

Requires Ollama running and `ollama pull llama3.2`.

## Files

- data.py — sample job and resume
- search.py — DuckDuckGo company search
- llm.py — one call to the local model
- jobfit.py — prompts and the run order

## What failed

Llama 3.2 does not follow every rule on every run.

- It sometimes scores 70 after being told to stay at 45 or below when skills are missing.
- It changes "Finishing" to "Completed".
- It copies resume lines instead of rewriting them.
- Company search sometimes returns a different company with the same name.

Those slips are why the next step is a check in code, not a longer prompt.