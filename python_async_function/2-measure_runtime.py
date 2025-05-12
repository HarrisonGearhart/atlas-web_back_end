#!/usr/bin/env python3
"""
function measures how long to execute wait_n(n, max_delay)
and returns total_time / n
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    total execution time of wait_n and returns the average time per run
    Args - n(int)
        max_delay(int)
    Returns - total_time / n [float]
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
        total_time = end - start
    return total_time / n
