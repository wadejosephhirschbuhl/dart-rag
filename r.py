import os,glob,re,shutil
from pathlib import Path
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings,ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCS="dart-rag-docs";DB="db"

def clean(s):return re.sub(r"\n{3,}","\n\n",re.sub(r"[ \t]+"," ",s.replace("\r",""))).strip()

E=OllamaEmbeddings(model="nomic-embed-text")
if "--reindex" in os.sys.argv:shutil.rmtree(DB,ignore_errors=True)

if not Path(DB).exists():
 files=[f for x in("txt","md") for f in glob.glob(f"{DOCS}/*.{x}")]
 if not files:raise SystemExit("Put .txt or .md files in dart-rag-docs/")
 docs=[Document(page_content=clean(open(f,encoding="utf-8").read()),metadata={"source":Path(f).name,"page":1}) for f in files]
 chunks=RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=200).split_documents(docs)
 Chroma.from_documents(chunks,E,persist_directory=DB)
 print(f"Indexed {len(files)} files, {len(chunks)} chunks.")

V=Chroma(persist_directory=DB,embedding_function=E)
M=ChatOllama(model="gemma3:4b",temperature=.2)

while 1:
 q=input("\n? ")
 if q.lower() in("q","quit","exit"):break
 h=V.similarity_search(q,k=4)
 c="\n\n".join(f"SOURCE: {d.metadata['source']} p{d.metadata['page']}\n{d.page_content}" for d in h)
 print("\n"+M.invoke(f'Use only this context. If absent say "I don’t know based on the provided documents." Cite as [filename p#].\n\n{c}\n\nQ: {q}').content)
