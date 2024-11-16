from fastapi import APIRouter

from app.item import services
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
