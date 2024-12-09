

REQUEST_BODY_JSON = """
{
    "email": "string@string.com",
    "password": "string"
}
"""


RESPONSE_200_JSON = """
{
    "token": "string",
    "user": {
        "id": 1,
        "email": "string@string.com",
        "role": "string"
    }
}
"""

RESPONSE_401_JSON = """
{
    "error": "string"
}
"""

RESPONSE_400_JSON = """
{
    "error": "string"
}
"""

