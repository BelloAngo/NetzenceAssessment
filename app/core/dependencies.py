import boto3
from mypy_boto3_dynamodb import DynamoDBClient, DynamoDBServiceResource

from app.core.settings import get_settings

# Globals
settings = get_settings()


def get_dynamo_client():
    """
    Get dynamo db connection
    """
    # Initialize the DynamoDB client
    if settings.DEBUG:
        dynamodb: DynamoDBClient = boto3.client(
            "dynamodb",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.DYNAMO_URL,
        )
    else:
        dynamodb: DynamoDBClient = boto3.client(
            "dynamodb",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

    return dynamodb


def get_dynamo_resource():
    """
    Get dynamo db connection
    """
    # Initialize the DynamoDB client
    if settings.DEBUG:
        dynamodb: DynamoDBServiceResource = boto3.resource(
            "dynamodb",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.DYNAMO_URL,
        )
    else:
        dynamodb: DynamoDBServiceResource = boto3.client(
            "dynamodb",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

    return dynamodb
