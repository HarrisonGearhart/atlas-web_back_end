#!/usr/bin/env python3
"""
function that creates and returns task wait_random(max_delay)
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    creates and returns task wait_random(max_delay)
    Args - max_delay(int): delay in seconds to wait
    Returns - asyncio.Task: the wait_random(max_delay) task
    """

    temp = asyncio.create_task(wait_random(max_delay))
    return (temp)
