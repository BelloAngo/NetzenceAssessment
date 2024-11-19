from pydantic import Field

from common.schemas import ResponseSchema
from item.schemas.base import Item


class ItemResponse(ResponseSchema):
    """
    Response schema for items
    """

    msg: str = "Item retrieved successfully"
    data: Item = Field(description="The details of the item")
