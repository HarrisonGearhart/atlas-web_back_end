#!/usr/bin/env python3
"""
function that creates and returns task wait_random(max_delay)
"""
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Run task_wai_random n times with max_delay as arg
    Args - n (int): times to run task_wait_random
    max_delay: the time of delay in seconds
    Returns - List[float]: list of all the delays
    """
    delays: typing.List[float] = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))

    return sorted(delays)
