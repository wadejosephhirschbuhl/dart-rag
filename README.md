# dart-rag

Tiny local RAG in the terminal using:

- Ollama
- Gemma 3 4B
- LangChain
- Chroma
- local documents in `dart-rag-docs/`

## Supported document types

Put any of these file types into `dart-rag-docs/`:

| Type | Extension |
|---|---|
| Plain text | `.txt` |
| Markdown | `.md` |
| PDF | `.pdf` |
| Word document | `.docx` |

Unsupported files are ignored.

## Setup

```bash
git clone https://github.com/YOUR-USERNAME/dart-rag.git
cd dart-rag

python3 -m venv v
. v/bin/activate
python -m pip install -r requirements.txt

ollama pull gemma3:4b
ollama pull nomic-embed-text
```

## Add documents

Put your `.txt`, `.md`, `.pdf`, or `.docx` files into:

```bash
dart-rag-docs/
```

Example:

```text
dart-rag-docs/
├── notes.txt
├── policy.md
├── article.pdf
└── report.docx
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
.txt / .md / .pdf / .docx documents
→ split into chunks
→ embed with nomic-embed-text
→ store/search in Chroma
→ retrieve relevant chunks
→ answer with gemma3:4b
```

Documents and the local vector database are ignored by git.
