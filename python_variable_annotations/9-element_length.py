#!/usr/bin/env python3
"""
Annotate the below function’s parameters
and return values with the appropriate types
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args - lst(Iterable[Sequence]): an iterable of sequences
    Returns - List[Tuple[Sequence, int]]: list of tuples
    """
    return [(i, len(i)) for i in lst]
