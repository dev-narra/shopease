


RESPONSE_200_JSON = """
{
    "orders": [
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
                "id": "string",
                "order_id": "string",
                "amount": 1.1,
                "method": "Card",
                "status": "Success",
                "transaction_date": "2099-12-31 00:00:00"
            },
            "status": "Pending",
            "expected_delivery_date": "2099-12-31",
            "order_datetime": "2099-12-31 00:00:00"
        }
    ],
    "total": 1,
    "page": 1,
    "size": 1
}
"""

