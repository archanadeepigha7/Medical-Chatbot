import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeVectorStore

import pinecone

# Load env
load_dotenv()

# Pinecone init (old stable way)
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment="us-east-1"
)

INDEX_NAME = "medical-chatbot"
PDF_PATH = "data/Medical_book.pdf"

print("📄 Loading PDF...")
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

print("✂️ Splitting text...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

print("🧠 Creating embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("📤 Uploading to Pinecone...")
PineconeVectorStore.from_documents(
    docs,
    embeddings,
    index_name=INDEX_NAME
)

print("✅ Data successfully ingested into Pinecone!")
