import boto3
from boto3_type_annotations.s3 import Client as S3Client
from core.settings import get_settings
from mypy_boto3_dynamodb import DynamoDBClient, DynamoDBServiceResource

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
            region_name=settings.A_REGION,
            aws_access_key_id=settings.A_ACCESS_KEY_ID,
            aws_secret_access_key=settings.A_SECRET_ACCESS_KEY,
            endpoint_url=settings.DYNAMO_URL,
        )
    else:
        dynamodb: DynamoDBClient = boto3.client(
            "dynamodb",
            region_name=settings.A_REGION,
            aws_access_key_id=settings.A_ACCESS_KEY_ID,
            aws_secret_access_key=settings.A_SECRET_ACCESS_KEY,
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
            region_name=settings.A_REGION,
            aws_access_key_id=settings.A_ACCESS_KEY_ID,
            aws_secret_access_key=settings.A_SECRET_ACCESS_KEY,
            endpoint_url=settings.DYNAMO_URL,
        )
    else:
        dynamodb: DynamoDBServiceResource = boto3.resource(
            "dynamodb",
            region_name=settings.A_REGION,
            aws_access_key_id=settings.A_ACCESS_KEY_ID,
            aws_secret_access_key=settings.A_SECRET_ACCESS_KEY,
        )

    return dynamodb


def get_s3_client():
    """
    Get s3 client
    """
    # Initialize the DynamoDB client
    if settings.DEBUG:
        s3: S3Client = boto3.client(
            "s3",
            region_name=settings.A_REGION,
            aws_access_key_id=settings.A_ACCESS_KEY_ID,
            aws_secret_access_key=settings.A_SECRET_ACCESS_KEY,
            endpoint_url=settings.DYNAMO_URL,
        )
    else:
        s3: S3Client = boto3.client(
            "s3",
            region_name=settings.A_REGION,
            aws_access_key_id=settings.A_ACCESS_KEY_ID,
            aws_secret_access_key=settings.A_SECRET_ACCESS_KEY,
        )

    return s3
