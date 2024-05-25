from enum import Enum
from typing import Union

from src.shared.actions import Action


class ExtraAction(Enum):
    INITIALIZE = "INITIALIZE"
    ROLL_DICE = "ROLL_DICE"


actions_to_prompt: dict[Union[Action, ExtraAction], str] = {
    # Tabs:
    Action.MANAGE: "Go on the 'Manage' tab",
    Action.BUY: "Got to the 'Buy' tab",
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


def get_action_prompt(action: Union[Action, ExtraAction]) -> str:
    return actions_to_prompt[action]
