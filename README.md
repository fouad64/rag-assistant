RAG Integration Project
Overview
This repository contains the first phase of a project that integrates Retrieval-Augmented Generation (RAG) using Chroma vector database, LLaMA Index, and OpenRouter API. The project is designed to load documents from PDFs and web URLs, process them into a vector store, and enable efficient retrieval and generation tasks. A second phase, currently in development, will include a graphical user interface (GUI). The GUI repository link will be provided soon.
Features

Load and process PDF documents from a specified directory.
Fetch and process web content from a list of URLs.
Set up a local Chroma vector database for document storage.
Build and persist a vector store index using LLaMA Index.
Utilize OpenRouter API and Hugging Face embeddings for advanced text processing.

Project Structure

__pycache__: Python bytecode cache.
chroma_db: Directory for the Chroma vector database.
data/pdfs: Directory containing PDF documents to be processed.
storage: Directory for storing the persisted vector index.
env: Environment configuration file.
.gitignore: Git ignore file.
chroma_integration.py: Script for setting up the Chroma database.
config.py: Configuration settings.
data_loader.py: Script for loading data from PDFs and web URLs.
index_builder.py: Script for building and persisting the vector index.

Prerequisites

Python 3.8+
Required Python packages (install via requirements.txt if provided, or manually install dependencies like chromadb, llama-index, openrouter, huggingface_hub, etc.).
An OpenRouter API key (store in .env as OPENROUTER_API_KEY).

Installation

Clone the repository:git clone https://github.com/fouad64/first-commit.git
cd first-commit


Create and activate a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt  # If requirements.txt exists, otherwise install manually


Set up your OpenRouter API key in a .env file:OPENROUTER_API_KEY=your_api_key_here



Usage

Ensure all PDFs are placed in the data/pdfs directory.
Update the URL_LIST in config.py with desired web URLs.
Run the data loader:python data_loader.py


Set up the Chroma database:python chroma_integration.py


Build and persist the index:python index_builder.py



Future Development
This is the first phase of the project. The second phase, which includes a GUI, is currently under development. The repository for the GUI phase will be linked here once available: (https://github.com/mohesham59/Assistant-using-agentic-ai-for-O-RAN)].
Contributing
Feel free to fork this repository, submit issues, or create pull requests for improvements.

