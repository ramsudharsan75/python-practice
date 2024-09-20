"""Sample python server using FastAPI"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """Root path"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """Read item"""
    return {"item_id": item_id, "q": q}
