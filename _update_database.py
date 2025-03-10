

from functions.add_to_chroma import add_to_chroma
from functions.get_document_loader import load_pdf_documents, load_xml_documents, load_web_documents
from functions.get_embedding_function import get_embedding_function
from functions.get_text_spliter import split_text

from enum import Enum
from timeit import default_timer as timer

CHROMA_PDF_PATH = "chroma/pdf"
CHROMA_XML_PATH = "chroma/xml"
CHROMA_WEB_PATH = "chroma/web"

DATA_PDF_PATH = "data/pdf"
DATA_XML_PATH = "data/xml"
DATA_WEB_PATH = "data/web"

class EMBEDDING(Enum):
    NOMIC = "nomic-embed-text"
    MXBAI = "mxbai-embed-large"
    SNOWFLAKEv2 = "snowflake-arctic-embed2"
    JINA = "jina/jina-embeddings-v2-base-es"

def main():

    size, overlap = 500, 25

    print("PDF")
    start = timer()
    documents = load_pdf_documents(DATA_PDF_PATH)
    chunks = split_text(documents, size, overlap)
    # for doc in documents:
    #     print(doc.metadata)
    # print(chunks)
    end = timer()
    print("Load & Split: %.2fs" % (end-start))
    start = timer()
    add_to_chroma(chunks, CHROMA_PDF_PATH, get_embedding_function(model=EMBEDDING.NOMIC))
    end = timer()
    print("Update DB: %.2fs" % (end-start))

    print("XML")
    start = timer()
    documents = load_xml_documents(DATA_XML_PATH) 
    chunks = split_text(documents, size, overlap)
    end = timer()
    print("Load & Split: %.2fs" % (end-start))
    start = timer()
    add_to_chroma(chunks, CHROMA_XML_PATH, get_embedding_function(model=EMBEDDING.NOMIC))
    end = timer()
    print("Update DB: %.2fs" % (end-start))

    print("WEB")
    start = timer()
    documents = load_web_documents(DATA_WEB_PATH)
    chunks = split_text(documents, size, overlap)
    end = timer()
    print("Load & Split: %.2fs" % (end-start))
    start = timer()
    add_to_chroma(chunks, CHROMA_WEB_PATH, get_embedding_function(model=EMBEDDING.NOMIC))
    end = timer()
    print("Update DB: %.2fs" % (end-start))    

if __name__ == "__main__":
    main()