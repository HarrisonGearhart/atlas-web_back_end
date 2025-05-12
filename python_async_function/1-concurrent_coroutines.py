#!/usr/bin/env python3
"""
run multiple asynchronous coroutines concurrently
"""
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    args - n int (times to run wait_random)
    max_delay (time of delay in seconds)
    returns - list[float] (listof all delays)
    """
    delays: typing.List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))

    return sorted(delays)
