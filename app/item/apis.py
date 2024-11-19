from typing import cast

from fastapi import APIRouter
from pydantic import UUID4

from common.schemas import ResponseSchema
from item import selectors, services
from item.schemas import base, create, edit, response

# Globals
router = APIRouter()


@router.post(
    "",
    summary="Create Item",
    response_description="The details of the item created",
    status_code=201,
    response_model=response.ItemResponse,
)
async def route_items_create(item_in: create.ItemCreate):
    """
    This endpoint creates a new item
    """

    item = await services.create_item(data=item_in)

    return {"data": item}


@router.get(
    "/{item_id}/",
    summary="Get Item Details",
    response_description="The details of the item",
    status_code=200,
    response_model=response.ItemResponse,
)
async def route_items_get(item_id: UUID4):
    """
    This endpoint returns the details of an item
    """

    # Get item
    item = cast(base.Item, await selectors.get_item_by_id(id=item_id))

    return {"data": item}


@router.put(
    "/{item_id}/",
    summary="Edit item details",
    response_description="The new details of the item",
    status_code=200,
    response_model=response.ItemResponse,
)
async def route_items_edit(item_id: UUID4, item_in: edit.ItemEdit):
    """
    This endpoint edits the item's details
    """

    # Get item
    item = cast(base.Item, await selectors.get_item_by_id(id=item_id))

    # Edit item
    new_item = await services.edit_item(item=item, data=item_in)

    return {"data": new_item}


@router.delete(
    "/{item_id}/",
    summary="Delete item",
    response_description="Item has been deleted successfully",
    status_code=200,
    response_model=ResponseSchema,
)
async def route_items_delete(item_id: UUID4):
    """
    This endpoint deletes an item
    """

    # Get item
    item = cast(base.Item, await selectors.get_item_by_id(id=item_id))

    # Delete item
    await services.delete_item(item=item)

    return {"msg": "Item has been deleted successfully", "data": None}
