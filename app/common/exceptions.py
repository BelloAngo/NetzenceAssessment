from datetime import datetime


class CustomHTTPException(Exception):
    """Base exception for all HTTP exceptions"""

    def __init__(self, msg: str, *, status_code: int, loc: list | None = None):
        self.status_code = status_code
        self.msg = msg
        self.loc = loc


class InternalServerError(Exception):
    """
    Common base class for all 500 internal server error responses
    """

    def __init__(self, msg: str, *, loc: str | None = None):
        self.msg = msg
        self.loc = loc
        self.timestamp = datetime.now()


class BadRequest(CustomHTTPException):
    """Custom base exceptions for all bad request"""

    def __init__(self, msg: str, *, loc: list | None = None):
        super().__init__(msg, status_code=400, loc=loc)


class Unauthorized(CustomHTTPException):
    """Custom base exceptions for all unauthorized exceptions"""

    def __init__(self, msg: str, *, loc: list | None = None):
        super().__init__(msg, status_code=401, loc=loc)


class Forbidden(CustomHTTPException):
    """Custom base exception for all forbidden exceptions"""

    def __init__(self, msg: str = "Forbidden", *, loc: list | None = None):
        super().__init__(msg=msg, status_code=403, loc=loc)


class NotFound(CustomHTTPException):
    """
    Common base class for all 404 responses
    """

    def __init__(self, msg: str, *, loc: list | None = None):
        super().__init__(msg, status_code=404, loc=loc)


class Conflict(CustomHTTPException):
    """Custom base exception for all conflict exceptions"""

    def __init__(self, msg: str, *, loc: list | None = None):
        super().__init__(msg, status_code=409, loc=loc)
