#!/usr/bin/env python3

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
