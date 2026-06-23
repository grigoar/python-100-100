import random
import my_module

#? importing modules (no export needed), random function
# random_integer = random.randint(1,10)
# print(random_integer)

# print(my_module.pi)

# # 0-1 / 0-5
# random_float = random.random() *5

# print(random_float)

# love_score = random.randint(1,100)

# print(f"Your love score is {love_score}")


# ? Head and tail random
# coin_face = random.randint(0,1)

# if(coin_face==1):
#   print ("heads")
# elif (coin_face==0):
#   print("tail")

#? Lists, append, extend, replace
# states_of_america = ["Delaware", "Pensylvania","Delaware", "Pensylvania"]

# # print(states_of_america[0])
# print(states_of_america[-1])
# states_of_america[-1] = "Texas"

# print(states_of_america[-1])

# states_of_america.append("Grigoreland")
# states_of_america.extend(["tt", "ff"])

# print(states_of_america)

#? Who will pay the bill?
# names_string = input("Give me a list of names separated by ',': ")
# names_string="Grig,Ana,Vasile,Mark,John"
# names = names_string.split(",")
# print(names)
# print(len(names))

# total = len(names)
# payer_index = random.randint(0,total-1)

# print(f"The {names[payer_index]} will pay the bill today. Yuppy!")
# payer= random.choice(names)

# print(f"{payer} will pay the bill today. Yuppy!")

#? index errors, and nested lists

# states_of_america = ["Delaware", "Pensylvania","Delaware", "Pensylvania"]

# print(states_of_america[1])

# list2 = ["test", "ntt"]

# merged = [states_of_america, list2]
# print(merged)

# Treasure hunting 
# Don't change the code below
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? Example: 23: ")
# # Don't change the code above

# if int(position[0])>3 or int(position[1]) >3:
#   print("not good")
#   exit()

# map[int(position[0])-1][int(position[1])-1]="X"
# print(f"{row1}\n{row2}\n{row3}")

# if(position[0]== "2"):
#   print("nice")
# else:
#     print("not_nice")

# ? Rock paper, scissors
print("Welcome to the Rock, Paper, Scissors game!")

user_choice = int(input("Please select an option: 1 - Rock, 2 - Paper, 3 - Scissors. Ex> 1 "))

computer_choice = random.randint(1,3)


rock = "Rock"
paper = "Paper"
scissors = "Scissors"
rock_number = 1
paper_number = 2
scissors_number = 3
mapping = {rock_number: rock, paper_number: paper, scissors_number: scissors}

if user_choice not in mapping:
  print("Invalid choice")
  exit()

print(f"User choice: {mapping[user_choice]}")
print(f"Computer choice: {mapping[computer_choice]}")

if user_choice == computer_choice:
  print(f"Draw - {mapping[user_choice]}")
elif user_choice == rock_number and computer_choice == paper_number:
  print(f"I lose! {mapping[computer_choice]} beats {mapping[user_choice]}")
elif user_choice == rock_number and computer_choice == scissors_number:
  print(f"I win! {mapping[user_choice]} beats {mapping[computer_choice]}")
elif user_choice == paper_number and computer_choice == rock_number:
  print(f"I win! {mapping[user_choice]} beats {mapping[computer_choice]}")
elif user_choice == paper_number and computer_choice == scissors_number:
  print(f"I lose! {mapping[computer_choice]} beats {mapping[user_choice]}")
elif user_choice == scissors_number and computer_choice == rock_number:
  print(f"I lose! {mapping[computer_choice]} beats {mapping[user_choice]}")
elif user_choice == scissors_number and computer_choice == paper_number:
  print(f"I win! {mapping[user_choice]} beats {mapping[computer_choice]}")























# user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. ")
# print(user_choice)
# computer_choice = random.randint(0,2)
# print(computer_choice)
# if user_choice == computer_choice:
#   print("It's a tie!")
# elif user_choice == 0 and computer_choice == 1:
#   print("You lose!")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif user_choice == 1 and computer_choice == 0: