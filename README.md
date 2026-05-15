# PDF-question-answering
Here are simple starter files for your GitHub project.

## `README.md`

```md id="yq9m3w"
# AI PDF Question Answering System

An AI-powered PDF Question Answering System built using Python, Streamlit, and Groq API.

Users can upload PDF documents and chat with them using an AI assistant.

---

## Features

- Upload PDF documents
- Extract text from PDFs
- Ask questions about uploaded documents
- AI-generated responses using Groq + Llama 3
- Chat interface with Streamlit
- Conversation history support

---

## Tech Stack

- Python
- Streamlit
- Groq API
- PDFPlumber
- Llama 3

---

## Project Structure

```

project/
│
├── app.py
├── requirements.txt
└── README.md

````

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
````

### 2. Open Project Folder

```bash
cd your-repo-name
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

### 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
streamlit run app.py
```

---

## API Key

Get your free Groq API key from:

[https://console.groq.com/keys](https://console.groq.com/keys)

Paste the API key inside the Streamlit sidebar.

---

## Future Improvements

* Better RAG pipeline
* Semantic search with FAISS
* Embeddings-based retrieval
* Voice interaction
* Multi-PDF support

---

## Author

Premchandh


