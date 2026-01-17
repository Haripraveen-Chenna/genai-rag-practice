from pypdf import PdfReader
from pathlib import Path

def load_all_pdfs(data_dir: Path) -> str:
    text = ""
    for pdf in data_dir.glob("*.pdf"):
        reader = PdfReader(pdf)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text
