"""This module contains the pagination logic for the application."""

import math


def get_pagination_metadata(*, tno_items: int, count: int, page: int, size: int):
    """This function is used to the pagination metadata of a response.

    Args:
        tno_items (int): The tno items
        count (int): The number of items you are returning
        page (int): The current page
        size (int): The number of items per page

    Returns:
        dict: A dictionary containing the paginated response

    Sample:
        {
            "page": 1,
            "size": 10,
            "count": 10,
            "items": []
        }
    """
    total_no_items = tno_items
    total_no_pages = math.ceil(total_no_items / size)
    metadata = {
        "total_no_items": total_no_items,
        "total_no_pages": total_no_pages,
        "page": page,
        "size": size,
        "count": count,
        "has_next_page": page < total_no_pages,
        "has_prev_page": page > 1,
    }
    return metadata
