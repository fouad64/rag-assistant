import os
from dotenv import load_dotenv
from chroma_integration import setup_chroma  # استيراد معدل
from data_loader import load_data
from index_builder import build_index
from query_engine import create_query_engine
import logging

# تحميل المتغيرات البيئية
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
LLM_MODEL = "meta-llama/llama-3.2-11b-vision-instruct:free"
PDF_DIR = "data/pdfs"
URL_LIST = [
    "https://en.wikipedia.org/wiki/Open_RAN",
    "https://www.o-ran.org/",
    "https://lf-o-ran-sc.atlassian.net/wiki/spaces/REL/pages/12812923/K+Release"
]
INDEX_STORAGE_DIR = "storage"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def display_chroma_results(results):
    documents = results["documents"]

    if not documents or not any(documents):
        print("\n⚠️ Chroma didn't return a useful answer.\n")
        return

    first_answer = documents[0][0]
    print("\n📄 Chroma Top Answer (Formatted):\n")

    # تقسيم الجملة إلى أوامر باستخدام علامات فاصلة أو نهاية أسطر
    lines = first_answer.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        sublines = [part.strip() for part in line.replace('&&', '\n').replace(';', '\n').replace('|', '\n').split('\n')]
        for cmd in sublines:
            if cmd:
                print(f"🔹 {cmd}")


def main():
    # تحميل البيانات من PDFs وURLs
    documents = load_data(PDF_DIR, URL_LIST)

    # تهيئة Chroma بكل الوثائق (مش بس PDF)
    chroma_collection = setup_chroma(documents, db_path="chroma_db", collection_name="rag_collection")

    # بناء الفهرس للنظام القائم على LLM
    index = build_index(documents, INDEX_STORAGE_DIR, OPENROUTER_API_KEY, LLM_MODEL)
    query_engine = create_query_engine(index)

    print("🔍 RAG System Ready! Enter your question (type 'exit' or 'q' to quit):")
    while True:
        query = input("\n> ")
        if query.lower() in ["exit", "q"]:
            print("👋 Exiting... See you soon!")
            break

        use_chroma = input("Use Chroma? (y/n): ")
        if use_chroma.lower() == 'y':
            results = chroma_collection.query(query_texts=[query], n_results=5)
            display_chroma_results(results)
        else:
            response = query_engine.query(query)
            print(f"\n💬 Answer: {response}")


if __name__ == "__main__":
    main()
