# RAG Integration Project

## Overview
This repository contains the first phase of a project that integrates Retrieval-Augmented Generation (RAG) using Chroma vector database, LLaMA Index, and OpenRouter API. The project is designed to load documents from PDFs and web URLs, process them into a vector store, and enable efficient retrieval and generation tasks. A second phase, currently in development, will include a graphical user interface (GUI). The GUI repository link will be provided soon.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fouad64/first-commit.git
   cd first-commit
2.Create and activate a virtual environment:
```bash


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:
If requirements.txt exists, run:
```bash


pip install -r requirements.txt
Otherwise, install manually.


Set up your OpenRouter API key in a .env file:
plaintext
```bash
OPENROUTER_API_KEY=your_api_key_here
-------------------------------------------------------------
Usage
Ensure all PDFs are placed in the data/pdfs directory.
Update the URL_LIST in config.py with desired web URLs.
Run the data loader:
bash

Collapse

Wrap

Run

Copy
python data_loader.py
Set up the Chroma database:
bash

Collapse

Wrap

Run

Copy
python chroma_integration.py
Build and persist the index:
bash

Collapse

Wrap

Run

Copy
python index_builder.py
Future Development
This is the first phase of the project. The second phase, which includes a GUI, is currently under development. The repository for the GUI phase will be linked here once available: [GUI Repository Link TBD - Please send the link to include it].

Contributing
Feel free to fork this repository, submit issues, or create pull requests for improvements.
