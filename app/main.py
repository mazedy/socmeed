from fastapi import FastAPI
from .routes import router
from .config import settings

app = FastAPI(
    title="Social Media API (Neo4j + FastAPI)",
    version="1.0.0"
)

# Include routes
app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Social Media API (Neo4j + FastAPI)"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)