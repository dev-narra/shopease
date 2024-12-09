

REQUEST_BODY_JSON = """
{
    "amount": 1.1,
    "method": "string"
}
"""


RESPONSE_200_JSON = """
{
    "id": "string",
    "order_id": "string",
    "amount": 1.1,
    "method": "Card",
    "status": "Success",
    "transaction_date": "2099-12-31 00:00:00"
}
"""

RESPONSE_400_JSON = """
{
    "error": "string"
}
"""

RESPONSE_404_JSON = """
{
    "error": "string"
}
"""

