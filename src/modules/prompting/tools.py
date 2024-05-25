"""Storing the TOOLS variable that our agent will call"""
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "Buy",
            "description": "buy the property",
            "parameters": {
                "type": "object",
                "properties": {
                    "yes": {
                        "type": "string",
                        "description": "buy the property",
                    }
                },
                "required": ["answer"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "Sell",
            "description": "Sell a property",
            "parameters": {
                "type": "object",
                "properties": {
                    "transaction_id": {
                        "type": "string",
                        "description": "Sell a property that you own for a price",
                    }
                },
                "required": ["property", "price"],
            },
        },
    },
    {
            "type": "function",
            "function": {
                "name": "Sell",
                "description": "Sell a property",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "Sell a property that you own for a price",
                        }
                    },
                    "required": ["property", "price"],
                },
            },
    },
    {
            "type": "function",
            "function": {
                "name": "Auction",
                "description": "bid on a property if someone didn't buy it",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "",
                        }
                    },
                    "required": ["bid"],
                },
            },
    }
]
