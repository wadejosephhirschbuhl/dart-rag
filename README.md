# dart-rag

Tiny local RAG in the terminal using:

- Ollama
- Gemma 3 4B
- LangChain
- Chroma
- local `.txt` and `.md` documents in `dart-rag-docs/`

## Supported document types

Only these file types are supported:

| Type | Extension |
|---|---|
| Plain text | `.txt` |
| Markdown | `.md` |

PDF, Word, and other file types are ignored.

## Setup

```bash
git clone https://github.com/wadejosephhirschbuhl/dart-rag.git
cd dart-rag

python3 -m venv v
. v/bin/activate
python -m pip install -r requirements.txt

ollama pull gemma3:4b
ollama pull nomic-embed-text
```

## Add documents

Put `.txt` or `.md` files into:

```bash
dart-rag-docs/
```

Example:

```text
dart-rag-docs/
├── notes.txt
└── policy.md
```

## Run

```bash
python r.py
```

Quit with:

```text
q
```

## Re-index after changing documents

```bash
python r.py --reindex
```

## How it works

```text
.txt / .md documents
→ split into chunks
→ embed with nomic-embed-text
→ store/search in Chroma
→ retrieve relevant chunks
→ answer with gemma3:4b
```

Private documents and the local vector database are ignored by git. The demo document is included.
