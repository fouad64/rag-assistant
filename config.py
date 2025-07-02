import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
LLM_MODEL = "meta-llama/llama-3.2-11b-vision-instruct:free"
PDF_DIR = "data/pdfs"
URL_LIST = [
    "https://en.wikipedia.org/wiki/Open_RAN",
    "https://www.o-ran.org/",
    "https://lf-o-ran-sc.atlassian.net/wiki/spaces/REL/pages/12812923/K+Release"
    "https://en.wikipedia.org/wiki/MIMO"
]
INDEX_STORAGE_DIR = "storage"