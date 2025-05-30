import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()


def start():
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=os.getenv("ENV", "development") == "development",
    )


if __name__ == "__main__":
    start()
