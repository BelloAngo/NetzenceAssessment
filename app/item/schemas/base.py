from datetime import datetime

from pydantic import UUID4, BaseModel, Field


class Item(BaseModel):
    """
    Base schema for items
    """

    itemId: UUID4 = Field(description="The ID of the item")
    name: str = Field(description="The name of the item")
    description: str = Field(description="The description of the item")
    createdAt: datetime = Field(description="The time the item was created")
