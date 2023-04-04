from utils.game import game
from utils.choices import Action
from utils.player import get_player_selection, get_computer_selection


def main() -> None:
    print('Welcome to Rock, Paper, Scissors!')
    while True:
        try:
            user_action: Action = get_player_selection()
        except ValueError as e:
            range_str: str = f"[0, {len(Action) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        computer_action: Action = get_computer_selection()
        print(f"\nYou chose {user_action.name}, computer chose {computer_action.name}.")
        print(game(user_action, computer_action))

        play_again: str = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break


if __name__ == '__main__':
    main()
