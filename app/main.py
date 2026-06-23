from fastapi import FastAPI
from app.routers import metrics

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "Engine Online",
        "version": "1.0.0"
    }

app.include_router(metrics.router)