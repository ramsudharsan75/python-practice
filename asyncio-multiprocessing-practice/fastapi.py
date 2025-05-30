from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    """Root endpoint."""
    return {"message": "Hello, World!"}
