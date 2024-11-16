from botocore.exceptions import ClientError

from app.core.dependencies import get_dynamo_client
from app.core.settings import get_settings

# Globals
settings = get_settings()


def check_or_create_table(table_name: str, table_config: dict):
    """Checks if a DynamoDB table exists or creates it."""

    dynamo_client = get_dynamo_client()
    try:
        # Check if the table exists
        response = dynamo_client.describe_table(TableName=table_name)
        print(
            f"Table '{table_name}' already exists. Status: {response['Table']['TableStatus']}"
        )
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            # Table does not exist, create it
            print(f"Table '{table_name}' not found. Creating...")
            try:
                dynamo_client.create_table(
                    TableName=table_name,
                    AttributeDefinitions=table_config["AttributeDefinitions"],
                    KeySchema=table_config["KeySchema"],
                    ProvisionedThroughput=table_config["ProvisionedThroughput"],
                )
                print(f"Table '{table_name}' creation initiated.")
            except ClientError as e:
                print(f"Error creating table '{table_name}': {e}")
                raise
        else:
            # Other exceptions
            print(f"Error checking table '{table_name}': {e}")
            raise


def initialize_tables(tables: dict):
    """Initializes all tables for the provided modules."""
    for table_name, table_config in tables.items():
        check_or_create_table(table_name, table_config)
