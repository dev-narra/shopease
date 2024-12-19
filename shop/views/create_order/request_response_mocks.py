

REQUEST_BODY_JSON = """
{
    "id": "string",
    "products": [
        {
            "name": "string",
            "description": "string",
            "price": 1.1,
            "mfg_date": "string",
            "exp_date": "string",
            "category": "string",
            "stock_quantity": 1.1,
            "id": 1
        }
    ],
    "customer": {
        "id": 1,
        "name": "string",
        "email": "string",
        "phone": "string",
        "address": "string"
    },
    "payment": {
        "id": 1,
        "amount": 1.1,
        "method": "Card",
        "transaction_date": "string"
    },
    "status": "Pending",
    "expected_delivery_date": "2099-12-31",
    "order_datetime": "2099-12-31 00:00:00"
}
"""


RESPONSE_200_JSON = """
{
    "id": "string",
    "products": [
        {
            "name": "string",
            "description": "string",
            "price": 1.1,
            "mfg_date": "string",
            "exp_date": "string",
            "category": "string",
            "stock_quantity": 1.1,
            "id": 1
        }
    ],
    "customer": {
        "id": 1,
        "name": "string",
        "email": "string",
        "phone": "string",
        "address": "string"
    },
    "payment": {
        "id": 1,
        "amount": 1.1,
        "method": "Card",
        "transaction_date": "string"
    },
    "status": "Pending",
    "expected_delivery_date": "2099-12-31",
    "order_datetime": "2099-12-31 00:00:00"
}
"""

