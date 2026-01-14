from fastapi import FastAPI,Form
import requests,json

app=FastAPI()

@app.post('/summarize')
def summarize(text: str=Form(...)):
    response=requests.post(
        "http://localhost:11434/api/chat",
        json={
        "model": "llama2",
        "messages": [
            {"role": "system", "content": "You are a summarization assistant. Give a short summary"},
            {"role": "user", "content": text}
        ],
        "stream": False
    }
)

    summary = response.json()["message"]["content"]
    return summary