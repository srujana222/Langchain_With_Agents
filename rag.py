from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

loader = CSVLoader(
    file_path="data/movies_metadata.csv",
    encoding="utf-8"
)

docs = loader.load()[:100]
print(len(docs))


splitter=RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=50
)

documents = splitter.split_documents(docs)

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
print("Creating FAISS...")
db = FAISS.from_documents(documents, embedding)
print("FAISS created")
# Save vector store
db.save_local("vectorstore")

print("FAISS Vector Store Created Successfully!")
      
retriever = db.as_retriever(
    search_kwargs={"k": 1}
)