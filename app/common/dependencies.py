from typing import Literal

from common.types import PaginationParamsType
from core.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def pagination_params(
    q: str | None = None,
    page: int = 1,
    size: int = 10,
    order_by: Literal["asc", "desc"] = "desc",
):
    """Helper Dependency for pagination"""
    return PaginationParamsType(q=q, page=page, size=size, order_by=order_by)
