from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
from extract_json import extract_json # Renaming to avoid conflict

def data_retriever(file):
    # Load the document, split it into chunks, embed each chunk, and load it into the vector store.
    raw_documents = extract_json(file)


    # Assuming OpenAIEmbeddings is properly initialized and available as `embeddings`
    db = Chroma.from_documents(raw_documents, OpenAIEmbeddings())  # Embedding the whole document into a single point
    
    """
    Assigning score_threshold to 0.5 to retrieve a document with above 
    50% relevance score, and setting "K" == 1
    """
    retriever_instance = db.as_retriever(
        search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0, "k": 1}
    )   
    return retriever_instance
