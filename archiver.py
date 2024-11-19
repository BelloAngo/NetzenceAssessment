import json
import logging
import os
from datetime import UTC, datetime, timedelta

import boto3
from botocore.exceptions import ClientError

# Variables
s3_bucket = os.environ.get("S3_BUCKET")


# Globals
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("items")


def lambda_handler(event, context):
    try:
        # Calculate the cutoff date (30 days ago)
        cutoff_date = datetime.now(tz=UTC) - timedelta(minutes=1)

        # Scan the table for items with createdAt older than 30 days
        response = table.scan()
        items = response.get("Items", [])

        # Filter the items based on the `createdAt` field
        old_items = [
            item
            for item in items
            if datetime.fromisoformat(item["createdAt"]).replace(tzinfo=UTC)
            < cutoff_date
        ]

        # Log and return the filtered items
        logging.info(f"Found {len(old_items)} items older than 30 days.")

        # Save archive to s3
        curr_time = datetime.now()
        upload_json_to_s3(
            old_items,
            f"arch-{curr_time.strftime('%Y-%m')}/{curr_time.strftime('%Y-%m-%d')}.json",
        )

        #  Delete item
        for item in old_items:
            table.delete_item(Key={"itemId": item["itemId"]})

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "msg": f"Archived {len(old_items)} items",
                    "items": old_items,
                }
            ),
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}


def upload_json_to_s3(json_data, key):
    """
    Upload a JSON object to an S3 bucket.

    :param json_data: The JSON object to upload
    :param key: The key (file name) to store in the bucket
    """
    try:
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)

        # Upload the JSON string as a file
        response = s3_client.put_object(
            Bucket=s3_bucket,
            Key=key,
            Body=json_string,
            ContentType="application/json",  # Set the content type
        )

        print(f"Successfully uploaded {key} to {s3_bucket}")
        return response
    except ClientError as e:
        print(f"Failed to upload JSON to S3: {str(e)}")
        raise
