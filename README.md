# Text Summarization Application

## Project Overview
This project is a **Text Summarization application** that leverages a **locally hosted LLaMA model** via Ollama. The application provides a modern, interactive interface for users to summarize text efficiently.

---

## Goal
Build a text summarization tool using a locally hosted LLaMA model, with a modern backend and frontend stack.

---

## Technology Stack

- **Ollama** – Run LLaMA locally for text summarization.  
- **FastAPI** – Backend API to interact with the LLaMA model.  
- **Streamlit** – Frontend user interface for easy interaction.  
- **Git & GitHub** – Version control and project publishing.

---

## Features
- Summarize any text input quickly.  
- Interactive web interface via Streamlit.  
- Fully local processing using LLaMA (no external API calls).  
- Easily deployable and version-controlled with GitHub.

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Start backend:
   uvicorn backend.main:app --reload
4. Start frontend:
   streamlit run frontend/app.py
