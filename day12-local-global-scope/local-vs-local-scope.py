
#? Scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#? #Local Scope

# def drink_portion():
#     global portion 
#     portion = 2
#     print(f"portion inside function: {portion}")

# drink_portion()
# print(f"portion outside function: {portion}")

# #?Global Scope
# player_health = 10

# def drink_portion():
#     player_health = 2
#     print(f"player_health inside function: {player_health}")

# drink_portion()
# print(f"player_health outside function: {player_health}")

#?There is no Block Scope

# game_level = 3

# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)

# create_enemy()

#? Modifying Global Scope

# enemies = 1

# def increase_enemies():
#     # global enemies
#     # enemies += 1
#     # print(f"enemies inside function: {enemies}")
#     return enemies + 1

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#? Global Constants

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@jack"

# def calc_square(number):
#     return PI * number * number

# print(calc_square(2))
# print(URL)
# print(TWITTER_HANDLE)

#? Number Guessing Game

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
    return turns - 1

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    answer = random.randint(1, 100)
    # print(f"The answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

game()