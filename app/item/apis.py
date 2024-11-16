from fastapi import APIRouter
from pydantic import UUID4

from app.item import selectors, services
from app.item.schemas import create, response

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
    item = await selectors.get_item_by_id(id=item_id)

    return {"data": item}
