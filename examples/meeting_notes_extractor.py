
from omnigenai_toolkit.data_handling import clean_text
from omnigenai_toolkit.rag import generate_embeddings

def extract_meeting_notes(audio_transcript):
    cleaned_text = clean_text(audio_transcript)
    embedding = generate_embeddings(cleaned_text)
    return embedding

if __name__ == "__main__":
    audio_transcript = "Meeting notes on project updates and deadlines."
    notes_embedding = extract_meeting_notes(audio_transcript)
    print("Meeting Notes Embedding:", notes_embedding)
