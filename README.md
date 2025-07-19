# 🧠 AI Lawyer Chatbot using RAG

This project is a Retrieval-Augmented Generation (RAG)-based AI Lawyer chatbot built using **LangChain**, **FAISS**, **Hugging Face embeddings**, and **Groq's DeepSeek-R1-Distill-LLaMA-70B** model. Users can upload legal PDFs and ask natural language questions to receive accurate, context-aware answers.

---

## 🚀 Features

- 📄 Upload any legal PDF document
- 🔍 Semantic search using FAISS vector store
- 🧠 Answers powered by DeepSeek-R1-Distill-LLaMA-70B on Groq
- ⚡ Fast, streaming responses
- 🛠️ Simple and interactive UI with Streamlit

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: LangChain + FAISS + Hugging Face Transformers
- **Embedding Model**: Hugging Face Sentence Transformers
- **LLM**: DeepSeek-R1-Distill-LLaMA-70B (via [Groq](https://console.groq.com/))
- **Vector Store**: FAISS

---

## 📦 Installation

```bash
git clone https://github.com/RITIKA-01A/ai-lawyer-chatbot.git
cd ai-lawyer-chatbot
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
## 🔐 Environment Variables
- Create a .env file in the root directory with the following:
```
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```
## ▶️ Run the App
```
streamlit run app.py
```
## ✅ Use Cases
- Lawyers analyzing legal documents or contracts

- Law students studying case files

- Clients seeking clarification from complex legal texts
