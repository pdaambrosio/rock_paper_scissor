from utils.choices import Action


def game(user_action: Action, computer_action: Action) -> str:
    if user_action == computer_action:
        return f"Both players selected {user_action.name}. It's a tie!"

    if user_action == Action.Rock:
        if computer_action == Action.Scissors:
            return "Rock smashes scissors! You win!"
        return "Paper covers rock! You lose."

    if user_action == Action.Paper:
        if computer_action == Action.Rock:
            return "Paper covers rock! You win!"
        return "Scissors cuts paper! You lose."

    if user_action == Action.Scissors:
        if computer_action == Action.Paper:
            return "Scissors cuts paper! You win!"
        return "Rock smashes scissors! You lose."
