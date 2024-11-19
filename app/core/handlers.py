from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

from common.exceptions import CustomHTTPException, InternalServerError
from core.settings import get_settings

# Globals
settings = get_settings()


async def base_exception_handler(_: Request, exc: Exception):
    """
    Exception handler for 'NotFound' exception
    """
    print(exc)

    # Send email if in live mode
    if not settings.DEBUG:
        ...
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": "Internal Server Error", "loc": []},
                "data": None,
            }
        ),
    )


async def request_validation_exception_handler(_: Request, exc: RequestValidationError):
    """
    Exception handler for 'RequestValidationError' raised by pydantic
    """

    # Get error message
    error = exc.errors()[0]

    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": error["msg"], "loc": error["loc"]},
                "data": None,
            }
        ),
    )


async def internal_server_error_exception_handler(_: Request, exc: InternalServerError):
    """Exception handler for 'InternalServerError' exception"""
    print(exc)

    # Send email if in live mode
    if not settings.DEBUG:
        ...
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": "Internal Server Error", "loc": []},
                "data": None,
            }
        ),
    )


async def custom_http_exception_handler(_: Request, exc: CustomHTTPException):
    """
    Exception handler for 'Base' exception
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            {
                "status": "error",
                "error": {"msg": exc.msg, "loc": exc.loc},
                "data": None,
            }
        ),
    )
