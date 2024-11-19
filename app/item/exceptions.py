from common.exceptions import NotFound


class ItemNotFound(NotFound):
    """
    Exception for 404 Item Not Found
    """

    def __init__(self, *, loc=None):
        super().__init__("Item Not Found", loc=loc)
