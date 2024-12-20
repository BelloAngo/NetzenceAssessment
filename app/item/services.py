import uuid
from datetime import UTC, datetime

from fastapi.encoders import jsonable_encoder

from core.dependencies import get_dynamo_resource
from item.schemas import base, create, edit

# Globals
dynamo = get_dynamo_resource()
item_table = dynamo.Table("items")


async def create_item(data: create.ItemCreate):
    """
    Create item

    Args:
        data (create.ItemCreate): The details of the new item

    Returns:
        base.Item: The details of the created item
    """
    # init obj
    item = base.Item(
        itemId=uuid.uuid4(),
        name=data.name,
        description=data.description,
        createdAt=datetime.now(tz=UTC),
    )

    # Create entry
    item_table.put_item(Item=jsonable_encoder(item.model_dump()))

    return item


async def edit_item(item: base.Item, data: edit.ItemEdit):
    """
    Edit item

    Args:
        item (base.Item): The item obj
        data (edit.ItemEdit): The new details of the item

    Returns:
        base.Item: The edited item
    """
    # Save changes
    item_table.update_item(
        Key={"itemId": str(item.itemId)},
        UpdateExpression="SET #name = :name, description = :description",
        ExpressionAttributeNames={
            "#name": "name",  # Use a placeholder for the reserved keyword
        },
        ExpressionAttributeValues={
            ":name": data.name,
            ":description": data.description,
        },
        ReturnValues="ALL_NEW",
    )

    # Set new values
    for field, value in data.model_dump().items():
        setattr(item, field, value)

    return item


async def delete_item(item: base.Item):
    """
    Delete item

    Args:
        item (base.Item): The item obj

    Returns:
        item: The deleted item obj
    """
    # Delete item
    item_table.delete_item(Key={"itemId": str(item.itemId)})

    return item
