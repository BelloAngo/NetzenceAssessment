ITEM = {
    "TableName": "Items",
    "AttributeDefinitions": [
        {
            "AttributeName": "itemId",
            "AttributeType": "S",
        },
    ],
    "KeySchema": [
        {"AttributeName": "itemId", "KeyType": "HASH"},
    ],
    "ProvisionedThroughput": {
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5,
    },
}


MODULE_TABLES = {"items": ITEM}
