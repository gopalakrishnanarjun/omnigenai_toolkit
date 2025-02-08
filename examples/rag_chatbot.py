
from omnigenai_toolkit.rag import rag_pipeline

def chatbot_response(query, documents):
    response = rag_pipeline(query, documents)
    return response

if __name__ == "__main__":
    query = "What are the latest advancements in AI?"
    documents = ["AI is advancing rapidly in healthcare.", "AI is powering renewable energy solutions."]
    response = chatbot_response(query, documents)
    print("Chatbot Response:", response)
