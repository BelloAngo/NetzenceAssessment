from pydantic import BaseModel, Field


class ItemEdit(BaseModel):
    """
    Edit schema for items
    """

    name: str = Field(description="The name of the item")
    description: str = Field(description="The description of the item")
