"""Storing the TOOLS variable that our agent will call"""

ACTIONS = [
{
        "type": "function",
        "function": {
            "name": "Action",
            "description": "Choose a single action to take. BUY: Use this to buy the property; END_TURN use this to end the turn and not buy the property",
            "parameters": {
                "type": "object",
                "properties": {
                    "ACTIONS": {
                        "type": "string",
                        "enum": ["BUY", "END_TURN"],
                        "description": "The action you want to take",
                        },
                },
                "required": ["action"],
            },
        },
    }
        ]
STARTER_TOOLS = [
{
        "type": "function",
        "function": {
            "name": "Action",
            "description": "Choose a single action to take",
            "parameters": {
                "type": "object",
                "properties": {
                    "BUY": {
                        "type": "string",
                        "description": "Use this to buy the property",
                        },
                    "END_TURN": {
                        "type": "string",
                        "description": "Use this to end the turn and not buy the property",
                        },
                },
                "required": ["action"],
            },
        },
    }
        ]
TOOL_AUCTION = [
    {
        "type": "function",
        "function": {
            "name": "Action",
            "description": "Choose an action to take",
            "parameters": {
                "type": "object",
                "properties": {
                    "BID": {
                        "type": "string",
                        "description": "Use this to make a bid on a property",
                        },
                    "PASS": {
                        "type": "string",
                        "description": "Use this to not make a bid on a property because you don't have the funds or don't want the property",
                        },
                    "EXIT_AUCTION": {
                        "type": "string",
                        "description": "Once an auction has finished and everyone has either bid or passed.",
                        },
                },
                "required": ["action"],
            },
        },
    }
        ]

TOOLS_MAIN = [
{
        "type": "function",
        "function": {
            "name": "Action",
            "description": "Choose an action to take",
            "parameters": {
                "type": "object",
                "properties": {
                    "BUY_PROPERTY": {
                        "type": "string",
                        "description": "Buy the property",
                        },
                    "END_TURN": {
                        "type": "string",
                        "description": "End your turn",
                        },
                },
                "required": ["action"],
            },
        },
    }

        ]

TOOLS_MANAGE = [

        ]
TOOLS_IDLE = [
{
        "type": "function",
        "function": {
            "name": "Action",
            "description": "Choose an action to take",
            "parameters": {
                "type": "object",
                "properties": {
                    "END_TURN": {
                        "type": "string",
                        "description": "End your turn because you have done what you wanted to",
                        },
                    "MANAGE": {
                        "type": "string",
                        "description": "Enter into the management interface. You will then be prompted to select a property and you can then proceed to buy or morgage it",
                        },
                    "SELECT_PROPERTY": {
                        "type": "string",
                        "description": "You can only do this when in the management game state. Select a property to either buy or morgage",
                        },
                
                    "BUY": {
                        "type": "string",
                        "description": "You can only do this in the SELECT_PROPERTY game state. Use this to buy a property",
                        },
                    
                    "MORGAGE": {
                        "type": "string",
                        "description": "You can only do this in the SELECT_PROPERTY game state. Use this to morgage your property. This renders it useless but you get money based on the properties value",
                        },

                    #"TRADE": {
                    #    "type": "string",
                    #    "description": "You can only do this in the SELECT_PROPERTY game state. Use this to morgage your property. This renders it useless but you get money based on the properties value",
                    #    },

                   # "SELECT_OTHER_PLAYER": {
                   #     "type": "string",
                   #     "description": "Selects another player to get information about them.",
                   #     },

                   # "SELECT_PROPERTY_AND_AMOUNT": {
                   #     "type": "string",
                   #     "description": "Select a property owned by another player and specify an amount to pay them for it.",
                   #     },

                   # "CANCEL_TRADE": {
                   #     "type": "string",
                   #     "description": "Cancel the trade if you change your mind",
                   #     },
                },
                "required": ["action"],
            },
        },
    }

        ]

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "Action",
            "description": "Choose an action to take",
            "parameters": {
                "type": "object",
                "properties": {
                    "END_TURN": {
                        "type": "string",
                        "description": "End your turn because you have done what you wanted to",
                        },
                    "MANAGE": {
                        "type": "string",
                        "description": "Enter into the management interface. You will then be prompted to select a property and you can then proceed to buy or morgage it",
                        },
                    "SELECT_PROPERTY": {
                        "type": "string",
                        "description": "You can only do this when in the management game state. Select a property to either buy or morgage",
                        },
                
                    "BUY": {
                        "type": "string",
                        "description": "You can only do this in the SELECT_PROPERTY game state. Use this to buy a property",
                        },
                    
                    "MORGAGE": {
                        "type": "string",
                        "description": "You can only do this in the SELECT_PROPERTY game state. Use this to morgage your property. This renders it useless but you get money based on the properties value",
                        },

                    #"TRADE": {
                    #    "type": "string",
                    #    "description": "You can only do this in the SELECT_PROPERTY game state. Use this to morgage your property. This renders it useless but you get money based on the properties value",
                    #    },

                   # "SELECT_OTHER_PLAYER": {
                   #     "type": "string",
                   #     "description": "Selects another player to get information about them.",
                   #     },

                   # "SELECT_PROPERTY_AND_AMOUNT": {
                   #     "type": "string",
                   #     "description": "Select a property owned by another player and specify an amount to pay them for it.",
                   #     },

                   # "CANCEL_TRADE": {
                   #     "type": "string",
                   #     "description": "Cancel the trade if you change your mind",
                   #     },
                },
                "required": ["action"],
            },
        },
    }
]

    #ROLL_AGAIN: "ROLL_AGAIN"
    #CHANCE: "CHANCE"
    #END_TURN: "END_TURN"
    #BID: "BID"
    #PASS: "PASS"
    #EXIT_AUCTION: "EXIT_AUCTION"
    #MANAGE: "MANAGE"
    #SELECT_PROPERTY: "SELECT_PROPERTY"
    #BUY: "BUY"
    #MORGAGE: "MORGAGE"
    #TRADE: "TRADE"
    #SELECT_OTHER_PLAYER: "SELECT_OTHER_PLAYER"
    #SELECT_PROPERTY_AND_AMOUNT: "SELECT_PROPERTY_AND_AMOUNT"
    #PROPOSE_TRADE: "PROPOSE_TRADE"
    #CANCEL_TRADE: "CANCEL_TRADE"
