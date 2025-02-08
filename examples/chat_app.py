import streamlit as st
from omnigenai_toolkit.interactive_interfaces import create_chat_interface

def main():
    st.title("Chat App with OmniGenAI Toolkit")
    model_name = "gpt-3.5-turbo"
    create_chat_interface(model_name, title="Interactive Chatbot")

if __name__ == "__main__":
    main()
