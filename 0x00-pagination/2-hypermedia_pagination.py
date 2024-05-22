#!/usr/bin/env python3
import csv
import math
from typing import List

"""Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in
    a list for those particular pagination parameters.

    Args:
        page (int): page numper
        page_size (int): page size

    Returns:
        tuple: tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
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
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        index = index_range(page, page_size)
        return dataset[index[0]: index[1]]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        hypermedia = {}
        data = self.get_page(page, page_size)
        
        hypermedia['page_size'] = len(data)
        hypermedia['page'] = page
        hypermedia['data'] = data
        
        totalPages = math.ceil(len(self.__dataset) / page_size)
        if (page >= totalPages):
            hypermedia['next_page']  = None
        else:
            hypermedia['next_page'] = page + 1
        if(page == 1):
            hypermedia['prev_page'] = None
        else:
            hypermedia['prev_page'] = page - 1
            
        hypermedia['total_pages'] = totalPages
        
        return hypermedia