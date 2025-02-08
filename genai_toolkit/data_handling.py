
# data_handling.py
import PyPDF2
import re

def clean_text(text: str) -> str:
    """
    Cleans and normalizes text.
    """
    return re.sub(r'\s+', ' ', text).strip()

def extract_text_from_file(file_path: str) -> str:
    """
    Extracts text from a PDF file.
    """
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''.join(page.extract_text() for page in reader.pages)
    return clean_text(text)
