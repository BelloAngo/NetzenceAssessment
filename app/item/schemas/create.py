from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    """
    Create schema for items
    """

    name: str = Field(description="The name of the item")
    description: str = Field(description="The description of the item")
