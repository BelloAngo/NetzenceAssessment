import boto3
from botocore.exceptions import ClientError

from app.core.settings import get_settings

# Globals
settings = get_settings()

# Initialize the DynamoDB client
if settings.DEBUG:
    dynamodb = boto3.client("dynamodb", endpoint_url=settings.DYNAMO_URL)
else:
    dynamodb = boto3.client(
        "dynamodb",
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )


def check_or_create_table(table_name, table_config):
    """Checks if a DynamoDB table exists or creates it."""
    try:
        # Check if the table exists
        response = dynamodb.describe_table(TableName=table_name)
        print(
            f"Table '{table_name}' already exists. Status: {response['Table']['TableStatus']}"
        )
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            # Table does not exist, create it
            print(f"Table '{table_name}' not found. Creating...")
            dynamodb.create_table(
                TableName=table_name,
                AttributeDefinitions=table_config["AttributeDefinitions"],
                KeySchema=table_config["KeySchema"],
                ProvisionedThroughput=table_config["ProvisionedThroughput"],
            )
            print(f"Table '{table_name}' creation initiated.")
        else:
            # Other exceptions
            print(f"Error checking table '{table_name}': {e}")
            raise


def initialize_tables(tables_dict: dict):
    """Initializes all tables for the provided modules."""
    for table_name, table_config in tables_dict.items():
        check_or_create_table(table_name, table_config)
