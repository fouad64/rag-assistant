from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openrouter import OpenRouter
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_index(documents: list, storage_dir: str, api_key: str, llm_model: str):
    """Build and persist a vector store index from documents."""
    try:
        # Configure LLM and embeddings
        Settings.llm = OpenRouter(api_key=api_key, model=llm_model)
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
        Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)  # زيادة الحجم
        
        # Check if index exists
        if os.path.exists(storage_dir):
            logger.info(f"Loading existing index from {storage_dir}")
            storage_context = StorageContext.from_defaults(persist_dir=storage_dir)
            index = load_index_from_storage(storage_context)
        else:
            logger.info("Building new index")
            for doc in documents:
                logger.info(f"Document content sample: {doc.text[:200]}...")  # فحص النص
            index = VectorStoreIndex.from_documents(documents, show_progress=True)
            index.storage_context.persist(persist_dir=storage_dir)
        
        return index
    except Exception as e:
        logger.error(f"Error building index: {e}")
        raise