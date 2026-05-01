from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    reader = PdfReader(str(path))
    extracted_text = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            extracted_text.append(f"\n--- Page {page_number} ---\n{text}")

    final_text = "\n".join(extracted_text).strip()

    if not final_text:
        raise ValueError("No readable text found in the PDF.")

    return final_text