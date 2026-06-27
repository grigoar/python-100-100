from array import array
import random
#? Simple loops
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)


#? Average Height
# students_heights = input ("Input a list of students height: ").split()

# # 171 172 188 199 222 111

# if(len(students_heights) == 0):
#   print("no heights entered")
#   exit()
# for n in range(0, len(students_heights)):
#   students_heights[n] = int(students_heights[n])
# print(students_heights)


# all_height = 0
# count = 0

# for sh in students_heights:
#   all_height +=sh
#   count+=1

# average = float(all_height/count)

# print(f"Average height is: {average:.3f}")

#? high score

# students_scores = input ("Input a list of students scores: ").split()
# max = int(students_scores[0])
# for n in range(0, len(students_scores)):
#   students_scores[n] = int(students_scores[n])
#   if students_scores[n] > max:
#     max = students_scores[n]

# print(f"The maximum is: {max}")

#? for range with step
# sum =0
# for number in range (1, 101):
#   sum +=number

# print(f"Sum is: {sum}")

# #? sum of even numbers
# sum =0 
# for number in range(2, 101,2):
#   sum+=number

# print(f"sum of even numbers: {sum}")

# ? fizz buzz numbers

# for number in range(1, 101):
#   if number%3 ==0 and number%5 ==0:
#     print("FizzBuzz")
#   elif number%3 ==0:
#     print("Fizz")
#   elif number%5 ==0:
#     print("Buzz")
#   else:
#     print(number)

# ? Password generator
import random
from typing import Any
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

password = ""


for letter_in in range (0, nr_letters):
  password+= random.choice(letters)
for letter_in in range (0, nr_numbers):
  password+= random.choice(numbers)
for letter_in in range (0, nr_symbols):
  password+= random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)
shuffled_password = "".join(password_list)

print(f"The password is: {password}")

list_password = list(password)
random.shuffle(list_password)

print(f"The password shuffle is: {"".join(list_password)}")
print(f"The password shuffle is: {shuffled_password}")

password=""
options=["letters","numbers","symbols"]
r_n=nr_numbers
r_l=nr_letters
r_s = nr_symbols
for letter_in in range (0, nr_letters + nr_numbers+nr_symbols):
  random_option = random.choice(options)
  if(random_option == "letters" and r_l>0):
    password+= random.choice(numbers)
    r_l = r_l-1
  if(random_option == "numbers" and r_n>0):
    password+= random.choice(letters)
    r_n=r_n-1
  if(random_option == "symbols" and r_s>0):
    password+= random.choice(symbols)
    r_s=r_s-1

print(f"The password on hard is: {password}")