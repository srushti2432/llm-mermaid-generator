import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_mermaid_code(user_prompt, prompt_type):
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    prompt_templates = {
        "ER": f"""Generate a Mermaid.js ER diagram. Use:
erDiagram
Entity {{
  int id
  string name
}}
Use only types: string, int, float, boolean, date.
Avoid commas, SQL keywords, and PRIMARY KEY.
Relationships must be like:
EntityA ||--o{{ EntityB : label_with_underscores
\"\"\"{user_prompt}\"\"\"
""",
        "Sequence": f"""Generate a Mermaid.js sequence diagram using:
sequenceDiagram
  participant A
  participant B
  A ->> B: message
Do not generate any other diagram type.
\"\"\"{user_prompt}\"\"\"
""",
        "Flowchart": f"""Generate a Mermaid.js flowchart using graph TD and arrows A --> B.
\"\"\"{user_prompt}\"\"\"
""",
        "Class": f"""Generate a Mermaid.js class diagram with:
classDiagram
  class ClassName {{
    +type property
    +method()
  }}
\"\"\"{user_prompt}\"\"\"
""",
        "Gantt": f"""Generate a valid Mermaid.js Gantt chart with:
gantt
  title Project Title
  dateFormat YYYY-MM-DD
\"\"\"{user_prompt}\"\"\"
""",
        "State": f"""Generate a Mermaid.js state diagram using:
stateDiagram
  [*] --> State1
\"\"\"{user_prompt}\"\"\"
""",
        "Journey": f"""Generate a Mermaid.js journey diagram with:
journey
  title Experience
  section Phase
    Actor -> System : score
\"\"\"{user_prompt}\"\"\"
""",
        "Requirement": f"""Generate a Mermaid.js requirement diagram:
requirementDiagram
  requirement R1 {{
    id: 1
    text: ...
  }}
\"\"\"{user_prompt}\"\"\"
""",
        "Pie": f"""Generate a Mermaid.js pie chart:
pie
  title Example
  "Label A" : 10
  "Label B" : 20
\"\"\"{user_prompt}\"\"\"
""",
        "Git": f"""Generate a Mermaid.js gitGraph:
gitGraph
  commit
  branch feature
  commit
  checkout main
  merge feature
\"\"\"{user_prompt}\"\"\"
""",
        "Generic": f"""Generate the best-fitting Mermaid.js diagram for:
\"\"\"{user_prompt}\"\"\"
Return only Mermaid code inside a code block.
"""
    }

    prompt = prompt_templates.get(prompt_type, prompt_templates["Generic"])
    response = model.generate_content(prompt)
    code = response.text.strip()

    if "```mermaid" in code:
        code = code.split("```mermaid")[1].split("```")[0].strip()
    elif "```" in code:
        code = code.split("```")[1].strip()

    lines = code.splitlines()
    cleaned = []

    for line in lines:
        line = line.strip()

        if line.endswith(","):
            line = line[:-1]

        if any(x in line.upper() for x in ["VARCHAR", "INTEGER", "PRIMARY KEY", "FOREIGN KEY", "TEXT"]):
            continue

        if "||" in line and ":" in line:
            parts = line.split(":")
            entity_part = parts[0].strip()
            label = parts[1].strip().replace(" ", "_") or "related_to"
            line = f"{entity_part} : {label}"

        if "||" in line and ":" not in line:
            continue

        cleaned.append(line)

    return "\n".join(cleaned)
