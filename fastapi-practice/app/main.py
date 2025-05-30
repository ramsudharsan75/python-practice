"""Practicing FastAPI"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app import database, models
from app.routers import auth, posts, users, votes

# models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def root():
    """Root Route"""
    return {"message": "Hello World"}
