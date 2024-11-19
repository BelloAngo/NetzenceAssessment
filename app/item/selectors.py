from pydantic import UUID4

from core.dependencies import get_dynamo_resource
from item.exceptions import ItemNotFound
from item.schemas import base

# Globals
dynamo = get_dynamo_resource()
item_table = dynamo.Table("items")


async def get_item_by_id(id: UUID4, raise_exc: bool = True):
    # Get item
    resp = item_table.get_item(Key={"itemId": str(id)})
    item = resp.get("Item", None)

    # Check: item not found
    if not item and raise_exc:
        raise ItemNotFound()

    return base.Item(**item) if item else None
