import os
import re
from pathlib import Path
from weasyprint import HTML, CSS



def convert_html_to_pdf(input_dir, output_filename):
    
    base_path = Path(input_dir).resolve()
    files = sorted([f for f in os.listdir(input_dir) if f.endswith('.html')])
    master_html = "<html><head><style>"
    master_html += "@page { size: A4; margin: 20mm; }"
    master_html += "div { page-break-after: always; }"
    master_html += "</style></head><body>"
    
    for filename in files:
        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
            content = re.sub(r'src="[^"]*/([^/]+\.(jpg|jpeg|png|gif))"', r'src="../images/\1"', content)
            master_html += f"<div>{content}</div>"
            
    master_html += "</body></html>"
    
    print(f"Generating PDF: {output_filename}...")
    HTML(string=master_html, base_url=str(base_path)).write_pdf(output_filename)
    print("Done!")


convert_html_to_pdf('lectures', 'Combined_Lectures.pdf')