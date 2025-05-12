#!/usr/bin/env python3
"""
file for task 2
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension() 4 times in parallel and measures runtime.
    returns the total runtime.
    """
    start = time.time()
    await asyncio.gather(*[asyncio.create_task(
        async_comprehension()) for _ in range(4)])
    return time.time() - start
