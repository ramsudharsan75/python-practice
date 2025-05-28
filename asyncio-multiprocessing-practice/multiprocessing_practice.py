"""Try multiprocessing with requests."""

import os
from datetime import datetime
from multiprocessing import Pool

import requests


def main():
    """Main function."""
    start = datetime.now()

    with Pool(processes=os.cpu_count()) as pool:
        pool.map(get_call, range(10))

    end = datetime.now()
    print(f"Time taken using multiprocessing: {(end - start).total_seconds()} seconds")

    start = datetime.now()

    for _ in range(10):
        get_call(None)

    end = datetime.now()
    print(
        f"Time taken without multiprocessing: {(end - start).total_seconds()} seconds"
    )


def get_call(_):
    """Make a request to the server."""
    return requests.get("http://localhost:8000", timeout=1)


if __name__ == "__main__":
    main()
