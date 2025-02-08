
from omnigenai_toolkit.rag import generate_embeddings

def track_news():
    headlines = [
        "AI Revolutionizes Healthcare",
        "New Advancements in Renewable Energy",
        "AI Powers Real-Time Translations"
    ]
    embeddings = [generate_embeddings(headline) for headline in headlines]
    return embeddings

if __name__ == "__main__":
    news_embeddings = track_news()
    for idx, embedding in enumerate(news_embeddings):
        print(f"Embedding for Headline {idx + 1}:", embedding)
