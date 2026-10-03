import json
import ollama

JD = """
Company: Northstar Robotics
Role: Agentic AI Engineer
We need Python, tool calling, and a way to measure whether the agent is right.
Nice to have: a small web frontend.
"""

RESUME = """
Solo developer. Built web apps with Next.js.
Finishing Andrew Ng's Machine Learning Specialization.
Learning agents. Comfortable with Python and APIs.
Freelance web work. No full-time engineering job yet.
"""

def ask(prompt: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]

def extract_skills(jd: str) -> dict:
    prompt = (
        "Read the job description. Reply with JSON only, no markdown.\n"
        'Shape: {"company": "...", "skills": ["...", "..."]}\n'
        "Rules:\n"
        "- 4 to 8 skills\n"
        "- every skill must be copied from the job text\n"
        "- do not add skills from the company name\n"
        "- do not add robotics, vision, or learning methods unless the text says them\n\n"
        f"JOB TEXT:\n{jd}"
    )
    raw = ask(prompt)
    return json.loads(raw)

if __name__ == "__main__":
    skills = extract_skills(JD)
    print(skills)