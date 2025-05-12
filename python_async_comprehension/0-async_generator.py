#!/usr/bin/env python3
"""
coroutine called async_generator will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Generator that waits 1 second before yielding a random
    float between 0 and 10, 10 times
    returns a random number between 0 and 10 (10 times)
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
