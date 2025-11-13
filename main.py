from gemini_utils import get_mermaid_code
from mermaid_generator import generate_mermaid_image, render_browser_fallback

def detect_diagram_type(user_prompt: str):
    if user_prompt.lower().startswith("sequence diagram"):
        return "Sequence"
    if user_prompt.lower().startswith("er diagram") or "er diagram" in user_prompt.lower():
        return "ER"
    if user_prompt.lower().startswith("flowchart"):
        return "Flowchart"
    if user_prompt.lower().startswith("class diagram"):
        return "Class"
    if user_prompt.lower().startswith("gantt chart"):
        return "Gantt"
    if user_prompt.lower().startswith("state diagram"):
        return "State"
    if user_prompt.lower().startswith("journey diagram"):
        return "Journey"
    if user_prompt.lower().startswith("requirement diagram"):
        return "Requirement"
    if user_prompt.lower().startswith("pie chart"):
        return "Pie"
    if user_prompt.lower().startswith("git graph"):
        return "Git"

    types = {
        "ER": ["er", "entity", "relational"],
        "Sequence": ["sequence", "participant", "message", "actor"],
        "Flowchart": ["flow", "process"],
        "Class": ["class", "inheritance"],
        "Gantt": ["gantt", "timeline"],
        "Pie": ["pie", "portion"],
        "State": ["state", "transition"],
        "Journey": ["journey", "experience"],
        "Requirement": ["requirement", "specification"],
        "Git": ["git", "commit", "branch"]
    }

    for key, keywords in types.items():
        if any(kw in user_prompt.lower() for kw in keywords):
            return key
    return "Generic"

def main():
    user_prompt = input("📝 Describe the diagram you want: ").strip()
    prompt_type = detect_diagram_type(user_prompt)
    print(f"\n📌 Detected Diagram Type: {prompt_type}")

    mermaid_code = get_mermaid_code(user_prompt, prompt_type)

    print("\n🧠 Generated Mermaid Code:\n")
    print(mermaid_code)

    filename_base = f"{prompt_type.lower()}_diagram"

    if prompt_type in ["Pie", "Journey", "Requirement"]:
        render_browser_fallback(mermaid_code, f"{filename_base}.html")
    else:
        try:
            output_file = generate_mermaid_image(mermaid_code, f"{filename_base}.png")
            print(f"\n✅ Diagram saved as: {output_file}")
        except Exception as e:
            print("\n❌ Failed to generate PNG diagram. Please check the Mermaid syntax.")
            print(e)

if __name__ == "__main__":
    main()
