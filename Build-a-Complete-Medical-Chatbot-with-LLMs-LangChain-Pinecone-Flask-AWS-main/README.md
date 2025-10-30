Project Overview

This project is an end-to-end implementation of a medical chatbot, built with modern Generative AI techniques. You’ll see how I leveraged large language models, vector search, and a web backend to create an interactive application that handles medical-domain queries.


 Key Features

Natural-language chat interface for medical queries

Uses LangChain to structure prompts, chains and retrieval logic

Employs Pinecone vector-database to store and search medical knowledge embeddings

Built on the Flask web framework for backend/API and served as a web app

Modular, clean code structure with configuration, prompts, data, UI all separated


 Technologies Used

Python 

LangChain

Pinecone

Flask

OpenAI GPT-based model (or whichever LLM you used)

HTML/CSS frontend (or any UI you built)

Git & GitHub for version control

 AWS services: EC2, Lambda, API Gateway, etc

🚀 Setup & Run Instructions

Clone this repository:

git clone https://github.com/archanadeepigha7/Medical-Chatbot.git
cd Medical-Chatbot


Install dependencies:

pip install -r requirements.txt


Configure your environment (create a .env or config file):

OPENAI_API_KEY=your_openai_key  
PINECONE_API_KEY=your_pinecone_key  
PINECONE_ENVIRONMENT=your_env  


dataset/knowledge base (The Gale Encyclopedia of Medicine Second Edition Volume 1), run embedding step:

python src/embed_medical_docs.py  


Launch the Flask web app:

flask run  


