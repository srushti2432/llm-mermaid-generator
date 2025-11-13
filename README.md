**🧠 Mermaid.js AI Diagram Generator**

This project converts natural language prompts into Mermaid.js diagrams, automatically generating a .png image using an LLM (Gemini). It detects the correct diagram type (Flowchart, Sequence, ER, Class, Gantt, State, Journey, Pie, etc.) and renders the corresponding visual diagram.


**🚀 Features**

Converts plain text prompts into diagrams

Automatically detects diagram type

Generates and saves high-quality .png output

**⚙️ Setup**

git clone https://github.com/srushti2432/llm-mermaid-generator.git

cd llm-mermaid-generator

pip install -r requirements.txt

Create a .env file in the root directory:

GEMINI_API_KEY=your_gemini_api_key


**▶️ Run**

python main.py


Then send a prompt :

{"prompt": ""}

**✅ Output**

The backend will generate and save:

output/flowchart_login.png


**🧰 Tech Stack**

Python 

Gemini API (LLM)

Mermaid.js + Mermaid CLI
