#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    get index of page numbers
    returns a tuple containing 2 ints
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
