# Work Flow

```
[ Upload PDF ] 
       │
       ↓
[ Extract Text ]
       │
       ↓
[ Chunk Text ]
       │
       ↓
[ Generate Embeddings using Hugging Face ]
       │
       ↓
[ Store in FAISS Vector Store ]
       │
       ↓
[ User asks for a Quiz ]
       │
       ↓
[ Retrieve Relevant Chunks ]
       │
       ↓
[ Pass context to LLM via LangChain ]
       │
       ↓
[ Display Quiz Questions ]

```

# Project Structure

```
genai_quiz_app/
│
├── main.py               # Main backend script
├── utils/
│   ├── pdf_utils.py      # PDF reading & text extraction
│   ├── embedding_utils.py# HuggingFace embeddings
│   └── vector_utils.py   # FAISS vector store operations
│
├── requirements.txt
└── data/
    └── uploads/

```