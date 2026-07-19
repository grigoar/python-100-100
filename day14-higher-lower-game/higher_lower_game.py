# Higher Lower Game

import random

from game_data import GAME_DATA


def get_random_account():
    return random.choice(GAME_DATA)


def play_game():
    account_a = get_random_account()
    account_b = get_random_account()
    while account_a["name"] == account_b["name"]:
        account_b = get_random_account()

    print(
        f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}"
    )
    print(
        f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}"
    )
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == "a":
        if account_a["follower_count"] > account_b["follower_count"]:
            print(
                f"You're right! A has more followers. - A has {account_a['follower_count']} followers and B has {account_b['follower_count']} followers."
            )
        else:
            print(
                f"You're wrong! B has more followers. - B has {account_b['follower_count']} followers and A has {account_a['follower_count']} followers."
            )
    elif guess == "b":
        if account_b["follower_count"] > account_a["follower_count"]:
            print("You're right!")
        else:
            print("You're wrong!")
    else:
        print("Invalid guess!")


game_should_continue = True
while game_should_continue:
    play_game()
    guess = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if guess == "n":
        game_should_continue = False
