from llama_index.core.readers import SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(pdf_dir: str, url_list: list):
    """Load documents from PDFs and web URLs."""
    try:
        documents = []
        
        # Load PDFs
        if os.path.exists(pdf_dir):
            logger.info(f"Loading PDFs from {pdf_dir}")
            pdf_reader = SimpleDirectoryReader(pdf_dir)
            docs = pdf_reader.load_data()
            for doc in docs:
                logger.info(f"PDF content sample: {doc.text[:200]}...")  # فحص النص المستخرج
            documents.extend(docs)
        else:
            logger.warning(f"PDF directory {pdf_dir} does not exist")
        
        # Load web pages
        if url_list:
            logger.info(f"Loading web pages: {url_list}")
            web_reader = SimpleWebPageReader(html_to_text=True)
            documents.extend(web_reader.load_data(url_list))
        
        logger.info(f"Loaded {len(documents)} documents")
        return documents
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise