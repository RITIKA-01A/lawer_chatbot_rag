from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

## 1.upload and load raw pdf
pdfs_directory = 'pdfs/'

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())


def load_pdf(file_path):
    loader =loader=PyPDFLoader(file_path)
    documents = loader.load()
    return documents

documents = load_pdf("universal_declaration_of_human_rights.pdf")
# print(len(documents))

#Step 2: Create Chunks
def create_chunks(documents): 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

text_chunks = create_chunks(documents)

#Step 3: Setup Embeddings Model (Use DeepSeek R1 with Ollama)
model_name="all-MiniLM-L6-v2"
def get_embedding_model(hf_model_name):
    embeddings = HuggingFaceEmbeddings(model_name=hf_model_name)
    return embeddings


#Step 4: Index Documents **Store embeddings in FAISS (vector store)
FAISS_DB_PATH="vectorstore/db_faiss"
faiss_db=FAISS.from_documents(text_chunks, get_embedding_model(model_name))
faiss_db.save_local(FAISS_DB_PATH)