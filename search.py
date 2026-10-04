from ddgs import DDGS


def search_company(company: str) -> str:
    query = f"{company} company what they build"
    try:
        rows = list(DDGS().text(query, max_results=3))
    except Exception as error:
        return f"(search failed: {error})"
    if not rows:
        return "(no search results)"
    lines = []
    for row in rows:
        title = row.get("title", "")
        body = row.get("body", "")[:200]
        lines.append(f"- {title}: {body}")
    return "\n".join(lines)