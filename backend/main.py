
from fastapi import FastAPI

app = FastAPI(title="Smart Study Planner")


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Study Planner!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
