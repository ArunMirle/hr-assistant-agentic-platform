
from fastapi import FastAPI

app = FastAPI(
    title="Agentic HR Platform",
    version="0.1.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to Agentic HR Platform"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
