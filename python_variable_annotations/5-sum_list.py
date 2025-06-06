#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes input_list (list of floats)
    and returns the sum as a float
    """
    return (sum(input_list))
