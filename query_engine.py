from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import RetrieverQueryEngine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_query_engine(index: VectorStoreIndex):
    """Create a query engine from a vector store index."""
    try:
        # Create a retriever with higher similarity top_k
        retriever = index.as_retriever(similarity_top_k=10)
        
        # Create a query engine using the retriever
        query_engine = RetrieverQueryEngine(retriever=retriever)
        
        logger.info("Query engine created successfully")
        return query_engine
    except Exception as e:
        logger.error(f"Error creating query engine: {e}")
        raise