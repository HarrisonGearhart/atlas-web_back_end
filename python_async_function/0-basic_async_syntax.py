#!/usr/bin/env python3
"""
asynchronous coroutine that takes an int as arg
and then waits from 0- that arg in seconds
then returns the time waited
"""
import asyncio
import random


# asynce def for async function
# max_delay - default value 10
async def wait_random(max_delay: int = 10) -> float:
    """
    waits a random time form 0-max_delay

    Args - max_delay (int): time in seconds with default of 10
    Returns - float: the time in seconds that we waited
    """
    ran_delay = random.uniform(0, max_delay)
    await asyncio.sleep(ran_delay)
    return (ran_delay)
