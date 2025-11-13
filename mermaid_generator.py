import subprocess
import webbrowser
import os

def generate_mermaid_image(mermaid_code, output_file="diagram.png"):
    with open("diagram.mmd", "w", encoding="utf-8") as f:
        f.write(mermaid_code)

    subprocess.run([
        r"C:\Users\Srushti\AppData\Roaming\npm\mmdc.cmd",  # update if needed
        "-i", "diagram.mmd",
        "-o", output_file,
        "--quiet"
    ], check=True)

    return output_file

def render_browser_fallback(mermaid_code, output_file="diagram.html"):
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Mermaid Diagram</title>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <script>mermaid.initialize({{ startOnLoad:true }});</script>
</head>
<body>
  <div class="mermaid">
{mermaid_code}
  </div>
</body>
</html>"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    webbrowser.open(f"file://{os.path.abspath(output_file)}")
    print(f"\n🌐 Opened browser with: {output_file}")
