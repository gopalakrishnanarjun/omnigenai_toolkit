# OmniGenAI Toolkit

**OmniGenAI Toolkit** is a lightweight, rule-based AI chatbot written entirely in Python. It requires no external model downloads, making it perfect for educational use, rapid prototyping, or extending into more advanced AI tools.

---

## 🔧 Features

- ✅ Regex-based pattern matching chatbot
- ✅ Customizable responses
- ✅ Fallback logic with keyword detection
- ✅ 100% Python Standard Library — no downloads or external dependencies
- ✅ Unit tested and modular structure

---

## 📦 Installation

Clone and install the package locally:

```bash
git clone https://github.com/gopalakrishnanarjun/omnigenai_toolkit.git
cd omnigenai-toolkit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install .
```

---

## 🚀 Usage

To run the example chatbot:

```bash
python examples/run_chat.py
```

### 💬 Example Session

```
You: hello
Bot: Hi there!

You: what is your name
Bot: I'm SmartAI, your simple Python chatbot.

You: what time is it?
Bot: The current time is 14:32:08.

You: bye
Bot: Goodbye! 👋
```

---

## 🗂 Project Structure

```
omnigenai-toolkit/
├── docs/                   # Documentation (optional)
├── examples/               # Example usage scripts
│   └── run_chat.py
├── omnigenai_toolkit/      # Main module code
│   └── chatbot.py
├── tests/                  # Unit tests
│   └── test_chatbot.py
├── .gitignore
├── LICENSE
├── README.md
└── setup.py
```

---

## 🧠 How It Works

- Uses `re` to match user input against predefined patterns.
- Returns randomized responses for variety.
- If no match is found, falls back to simple keyword checks like `"time"` or `"weather"`.

---

## 🌱 Future Enhancements

### 🔹 Short-Term
- Store patterns and responses in external JSON/YAML
- Add chatbot personality profiles (e.g., sarcastic, friendly)

### 🔹 Medium-Term
- Add memory/context support for ongoing conversations
- Create web interface using Flask or FastAPI

### 🔹 Long-Term
- Integrate voice input/output
- Use cloud APIs (optional) for GPT-style responses
- Add multilingual support and translation layer

---

## 🤝 Contributing

1. Fork the repo
2. Create a new feature branch
3. Push your changes and open a Pull Request

All contributions are welcome — from typo fixes to new features!

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## ✨ Author

Built with ❤️ by Gopalakrishnan Arjunan (https://github.com/gopalakrishnanarjun)

---

## 🙌 Acknowledgments

Inspired by early rule-based AI bots like ELIZA and built for offline-friendly simplicity.
