from pydantic import Field

from app.common.schemas import ResponseSchema
from app.item.schemas.base import Item


class ItemResponse(ResponseSchema):
    """
    Response schema for items
    """

    msg: str = "Item retrieved successfully"
    data: Item = Field(description="The details of the item")
