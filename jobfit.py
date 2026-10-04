import json
from search import search_company
from llm import ask
from data import JD, RESUME

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

def score_fit(jd: str, resume: str, skills: dict, notes: str) -> dict:
    prompt = (
        "Compare the resume to the job. Reply with JSON only, no markdown.\n"
        'Shape: {"score": 0, "summary": "...", "missing": ["..."], "bullets": ["..."]}\n'
        "Rules:\n"
        "- score is an integer from 0 to 100 for this person, not for the company\n"
        "- if 2 or more required skills are missing, score must be 45 or lower\n"
        "- summary is 1 or 2 sentences about the candidate\n"
        "- summary must not describe the company\n"
        "- missing comes only from SKILLS, never from COMPANY NOTES\n"
        "- Next.js web apps count as a small web frontend\n"
        "- bullets is exactly 5 different lines\n"
        "- each bullet rewrites a resume fact toward this job\n"
        "- do not copy a resume sentence unchanged\n"
        "- Finishing stays Finishing, Learning stays Learning\n"
        "- do not invent jobs, employers, years, or skills\n\n"
        f"SKILLS:\n{skills}\n\n"
        f"COMPANY NOTES:\n{notes}\n\n"
        f"RESUME:\n{resume}\n\n"
        f"JOB:\n{jd}"
    )
    raw = ask(prompt)
    return json.loads(raw)

if __name__ == "__main__":
    skills = extract_skills(JD)
    print("SKILLS")
    print(skills)

    notes = search_company(skills["company"])
    print("\nCOMPANY NOTES")
    print(notes)

    fit = score_fit(JD, RESUME, skills, notes)
    print("\nFIT")
    print(json.dumps(fit, indent=2))