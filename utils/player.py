from random import randint
from utils.choices import Action


def get_player_selection() -> Action:
    choices: list = [f"{action.name}[{action.value}]" for action in Action]
    choices_str: str = ", ".join(choices)
    selection: int = int(input(f"Enter a choice ({choices_str}): "))
    action: Action = Action(selection)
    return action


def get_computer_selection():
    selection = randint(0, len(Action) - 1)
    action = Action(selection)
    return action
