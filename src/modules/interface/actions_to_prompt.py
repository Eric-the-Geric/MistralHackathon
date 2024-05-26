# from enum import Enum
from typing import Union

from src.shared.actions import Action, ExtraAction

actions_to_prompt: dict[Union[Action, ExtraAction], str] = {
    # Tabs:
    Action.MANAGE: "Go on the 'Manage' tab",
    Action.BUY: "Go to the 'Buy' tab",
    Action.TRADE: "Go to the 'Trade' tab",
    # Actions:
    Action.ROLL_AGAIN: "Roll the dice again",
    Action.BUY_PROPERTY: "Buy the property you landed on Buy ($Any)",
    Action.END_TURN: "End turn",
    Action.PASS: "Pass",
    Action.BID: "Enter an amount and press the 'Bid' button",
    Action.EXIT_AUCTION: "Exit the auction",
    Action.CANCEL_TRADE: "Cancel the trade",
    # Extra actions:
    ExtraAction.INITIALIZE: "Initialize the game for 2 players and start the game. Player 1 has to be human and Player 2 has to be AI (test).",
    ExtraAction.ROLL_DICE: "Roll the dice",
}

model_action_to_prompt = {
    "INITIALIZE": "Initialize the game for 2 players and start the game. Player 1 has to be human and Player 2 has to be AI (test).",
    "BUY": "Buy the property you landed on Buy ($Any)",
    "END_TURN": "End your turn and not buy the property you landed on",
    "ROLL_DICE": "roll the dice",
    "ROLL_AGAIN": "Roll the dice again",
    "OK": "click the 'OK' button to remove the popup",
    "GO_TO_MANAGE_TAB": "Click on the 'MANAGE' tab", 
    #"GO_TO_TRADE_TAB": "Click on the 'Trade' tab", 
    "GO_TO_BUY_TAB": "Click on the Buy *tab*", 
    "BID": "Make a bid that is greater than your opponent", 
    "PASS": "Click on the 'pass' button", 
    "EXIT_AUCTION": "Click on the 'exit auction' button",
}


def get_action_prompt(action: str) -> str:
    return model_action_to_prompt[action]


if __name__ == "__main__":
    action = Action("BUY")
    print(actions_to_prompt[action])
