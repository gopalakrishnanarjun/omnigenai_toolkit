
from omnigenai_toolkit.data_handling import extract_text_from_file
from omnigenai_toolkit.rag import generate_embeddings

def summarize_document(file_path):
    text = extract_text_from_file(file_path)
    embedding = generate_embeddings(text)
    return embedding

if __name__ == "__main__":
    file_path = "sample.pdf"
    summary = summarize_document(file_path)
    print("Document Summary Embeddings:", summary)
