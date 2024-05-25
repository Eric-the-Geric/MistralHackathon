from enum import Enum

from src.shared.actions import Action

actions_to_prompt: dict[Action, str] = {
    Action.BUY_PROPERTY: "Buy the current property",
}


class ExtraAction(Enum):
    INITIALIZE = "INITIALIZE"
    ROLL_DICE = "ROLL_DICE"


extra_actions_to_prompt: dict[ExtraAction, str] = {
    ExtraAction.INITIALIZE: "Initialize the game for 2 players and start the game",
    ExtraAction.ROLL_DICE: "Roll the dice",
}
