
from fastapi import FastAPI

app = FastAPI(
    title="GCM_AGENT",
    description="AI Voice and Chat Assistant",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to GCM_AGENT"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
