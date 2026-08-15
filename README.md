# 🎬 AI Movie Production using LangChain

An AI-powered **Movie Production Team** built using **Python, LangChain, RAG, LLMs, and FastAPI**. The project uses multiple AI agents to automate different stages of movie production.

## 🚀 Features

* 🎬 Script Generation
* 🎭 Casting Suggestions
* 💰 Budget Planning
* 📍 Location Suggestions
* ✂️ Editing Recommendations
* 📢 Promotion Strategy
* 🚀 Release Strategy

## 🛠️ Technologies

* Python
* LangChain
* RAG
* LLM
* FAISS
* Hugging Face Embeddings
* FastAPI
* Pydantic

## 🔄 Workflow

```text
User Input
    ↓
FastAPI
    ↓
LangChain Agents
    ↓
RAG + FAISS
    ↓
LLM
    ↓
Movie Production Response
```

## 📂 Project Structure

```text
AI_Movie_Production/
│
├── app.py
├── main.py
├── agents.py
├── tasks.py
├── llm.py
├── rag.py
├── prompts.py
├── requirements.txt
│
└── tools/
    ├── script_tool.py
    ├── casting_tool.py
    ├── budget_tool.py
    ├── location_tool.py
    ├── editing_tool.py
    ├── promotion_tool.py
    └── release_strategy_tool.py
```

## ▶️ Run the Project

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## 📌 Example Input

```json
    query: str

```

## 👩‍💻 My Role

* Developed LangChain-based AI agents and tools.
* Implemented RAG using FAISS and embeddings.
* Integrated LLMs with FastAPI.
* Designed prompts and tested the complete workflow.

## 🔮 Future Enhancements

* AI movie poster generation
* AI trailer generation
* Voice interaction
* Web UI using Streamlit/React
* Cloud deployment

⭐ **Built with Python, LangChain, RAG and Generative AI.**
