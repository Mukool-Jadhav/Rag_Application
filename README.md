# 📖 RAG Application

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using:

- **ChromaDB** as the vector database for storing and retrieving embeddings.  
- **Gemini Embedding Model** for converting documents into dense vector representations.  
- **Gemini Chat Model** for generating natural language responses grounded on retrieved context.  

The goal is to enable **context-aware Q&A** by combining document retrieval with LLM reasoning.

---

## 🚀 Features
- 🔎 Store and search documents using **ChromaDB**.  
- 🧠 Use **Gemini embeddings** to represent documents and queries in vector space.  
- 💬 Answer user queries with **Gemini chat model**, enriched by retrieved context.  
- 📂 Modular code structure for embeddings, vector storage, and chat pipeline.  
- ⚡ Lightweight and extendable for custom datasets or other vector DBs.  

---

## 📂 Project Structure
# 📂 Rag_Application
Rag_Application/
│── main.py – Entry point to run the RAG pipeline
│── embedding.py – Handles Gemini embeddings for text/documents
│── VectorStore.py – Manages ChromaDB vector database
│── chatModel.py – Chat model integration with Gemini
│── requirements.txt – Python dependencies
│── .gitignore – Ignored files (venv, cache, etc.)
│── README.md – Project documentation


---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Mukool-Jadhav/Rag_Application.git
cd Rag_Application
```

### 2. Set up a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

- **You’ll need API access to Google Gemini models.
- **Store your API key as an environment variable:
```bash
# Linux/Mac
export GEMINI_API_KEY="your_api_key_here"

# Windows
setx GEMINI_API_KEY "your_api_key_here"
```

##▶️ Usage
- Run the RAG pipeline:
```bash
python main.py
```

- **Then interact with the system:
- Documents are embedded using Gemini embeddings and stored in ChromaDB.
- User queries are converted into embeddings.
- Relevant documents are retrieved from ChromaDB.
- The Gemini chat model generates a response using retrieved context.

