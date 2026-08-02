login_schema = {
    "type": "object",
    "properties": {
        "access_token": {
            "type": "string"
        },
        "token_type": {
            "type": "string"
        }
    },
    "required": [
        "access_token",
        "token_type"
    ],
    "additionalProperties": False
}