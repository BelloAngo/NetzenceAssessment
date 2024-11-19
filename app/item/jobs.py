import json
import os
from datetime import UTC, datetime, timedelta

from core.dependencies import get_dynamo_resource
from external.aws.media import upload_file_to_bucket
from fastapi.encoders import jsonable_encoder
from item import services
from item.schemas import base

# Globals
dynamo = get_dynamo_resource()
item_table = dynamo.Table("items")


async def archive_items(event, context):
    # Get items
    response = item_table.scan()
    items = response.get("Items", [])

    # init items to delete
    archive = []
    # Loop and check for old items
    for item in items:
        # Transform obj
        item = base.Item(**item)

        # init 30day ago
        archive_time = datetime.now(tz=UTC) - timedelta(minutes=1)  # timedelta(days=30)

        # Check: if item was created before 30days ago
        if item.createdAt <= archive_time:
            # append archives with the item dict
            archive.append(jsonable_encoder(item.model_dump()))
            print(item.itemId)

    # Dump deleted items to json
    with open("archive.json", "w") as file:
        json.dump(archive, file, indent=4)

    # Save archive to s3
    curr_time = datetime.now()
    upload_file_to_bucket(
        "archive.json",
        f"arch-{curr_time.strftime("%Y-%m")}",
        curr_time.strftime("%Y-%m-%d"),
    )

    #  Delete item
    for item in archive:
        await services.delete_item(item=base.Item(**item))

    # Delete archive file
    os.remove("archive.json")

    return len(archive)
