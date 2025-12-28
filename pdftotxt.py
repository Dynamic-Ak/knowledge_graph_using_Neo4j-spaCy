# pdf_to_text.py
import PyPDF2

def extract_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

text = extract_text("research_paper.pdf")

with open("data.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text extracted successfully!")
