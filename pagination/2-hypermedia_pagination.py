#!/usr/bin/env python3
"""
helper function
"""

import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    get index of page numbers
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ find page """
        # make sure both are int and greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # needs to be a tuple
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        # if not in range of dataset than return empty list
        if start >= len(dataset):
            return []

        # return the index of start and end
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        dictionary with hypermedia-style pagination
        """
        # get same arguments as get page
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        # ceiling of total_data / page_size
        total_pages = math.ceil(total_data / page_size)

        # dict to hold data
        hyper_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        # return the dict
        return (hyper_data)
