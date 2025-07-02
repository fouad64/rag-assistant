import os
import logging
from uuid import uuid4

from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_chroma(documents, db_path: str = "chroma_db", collection_name: str = "rag_collection"):
    """Set up a local Chroma vector database using a list of documents."""
    try:
        # ✅ إنشاء دالة التحويل إلى embedding
        embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

        # ✅ تهيئة Chroma Client
        client = PersistentClient(path=db_path)

        # ✅ إنشاء أو جلب مجموعة Chroma
        collection = client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_function
        )

        # ✅ تقسيم المحتوى النصي إلى chunks
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)

        for doc in documents:
            if not doc or not doc.text:
                continue
            chunks = text_splitter.split_text(doc.text)
            collection.add(
                documents=chunks,
                ids=[str(uuid4()) for _ in range(len(chunks))]
            )

        logger.info(f"Chroma database initialized at {db_path}")
        return collection

    except Exception as e:
        logger.error(f"Error setting up Chroma: {e}")
        raise
