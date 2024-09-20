"""Asyncio practice"""

import asyncio
from datetime import datetime

import aiohttp


async def get_call(_):
    """Make an asynchronous HTTP request."""
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8000", timeout=aiohttp.ClientTimeout(1)) as response:
            return await response.text()


async def main():
    """Main function."""
    start = datetime.now()
    tasks = [get_call(None) for _ in range(10000)]
    await asyncio.gather(*tasks)
    end = datetime.now()
    print(f"Time taken using asyncio: {(end - start).total_seconds()} seconds")

    start = datetime.now()
    done, pending = await asyncio.wait(
        [asyncio.create_task(get_call(None)) for _ in range(10000)],
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        try:
            task.cancel()
            await task
        except asyncio.CancelledError:
            pass

    end = datetime.now()
    print(
        f"Time taken using asyncio with wait: {(end - start).total_seconds()} seconds"
    )


if __name__ == "__main__":
    asyncio.run(main())
