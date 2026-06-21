
#? Rollercoster

# print("Welcome to the rollercoaster")
# height = int (input("What is your height in cm? "))

# if height==120:
#   print (f"You can ride the rollercoaster {height}")
# else:
#   print("Sorry, you are not allowed to ride! To short!")

#? Odd or Even

# number = int (input("Which number do you want to check? "))

# if number%2 ==1:
#   print(f"The number {number} is odd")
# else:
#   print(f"The number {number} is even")


#? Nested if/else

# print("Welcome to the rollercoaster")
# height = int (input("What is your height in cm? "))

# if height>120:
#   print (f"You can ride the rollercoaster {height}")
#   age = int (input("What is your age? "))
#   if age<10:
#     print("Please pay $3")
#   elif age<=18:
#     print("please pay $7")
#   else:
#     print("Please pay $12")
# else:
#   print("Sorry, you are not allowed to ride! To short!")

#? BMI with interpretation
# BMI calculator : BMI = w(kg) / height * height (m2)

# height = input("enter your height in m (ex: 1.75):")
# weight = input ("enter your weight in kg (ex: 83):")

# bmi  = float(float(weight) / (float(height) *float(height)))

# print("your BMI is:" + f"{bmi:.2f}")
# print ("rounded " + str(round(bmi,2)))

# if bmi<18.5:
#   print("you are underweight")
# elif bmi>=18.5 and bmi<25:
#   print("You have a normal weight")
# elif (bmi>=25 and bmi<30):
#   print("You are overweight")
# elif bmi>=30 and bmi<35:
#   print("You are obese")
# else:
#   print("You are clinically obese")

#? Leap year

# year = int (input("Which year do you want to check? "))

# # if (year%4 ==0 and year%100!=0) or year%400==0:
# #   print("Leap year")
# # else:
# #   print("Not leap year")
# if year%4 ==0:
#   if year%400 == 0:
#     print("Leap year")
#   elif year%100 ==0:
#     print("not Leap Year")
#   else:
#     print("Leap Year")
# else:
#   print("Not leap year")

#? Rollercoster with billing
# print("Welcome to the rollercoaster")
# height = int (input("What is your height in cm? "))
# bill=0

# if height>120:
#   print (f"You can ride the rollercoaster {height}")
#   age = int (input("What is your age? "))
#   if age<10:
#     print("Please pay $3")
#     bill=3
#   elif age<=18:
#     print("please pay $7")
#     bill=7
#   else:
#     print("Please pay $12")
#     bill=12

#   wants_photo= input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill+=3
# else:
#   print("Sorry, you are not allowed to ride! To short!")

# print (f"The bill is {bill}")

#? Pizza order
# Don't change the code below 
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # # Don't change the code above

# if size == "S":
#   bill=15
#   pep_option = 2
# elif size == "M":
#   bill=20
#   pep_option = 3
# else:
#   bill=25
#   pep_option = 3
# if add_pepperoni == "Y":
#   bill+=pep_option
# if extra_cheese=="Y":
#   bill+=1
# pepperoni_cost = pep_option if add_pepperoni == "Y" else 0
# cheese_cost = 1 if extra_cheese == "Y" else 0

# print(f"Size: {size} | Pepperoni: {'Yes' if add_pepperoni == 'Y' else 'No'} (+${pepperoni_cost}) | Extra cheese: {'Yes' if extra_cheese == 'Y' else 'No'} (+${cheese_cost}) | Total: ${bill}")

#? Logical operators
# print("Welcome to the rollercoaster")
# height = int (input("What is your height in cm? "))
# bill=0

# if height>120:
#   print (f"You can ride the rollercoaster {height}")
#   age = int (input("What is your age? "))
#   if age<10:
#     print("Please pay $3")
#     bill=3
#   elif age<=18:
#     print("please pay $7")
#     bill=7
#   elif age>=45 and not age>55:
#     print("Everything is going to be ok. have a free ride with us!")
#   else:
#     print("Please pay $12")
#     bill=12

#   wants_photo= input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill+=3
# else:
#   print("Sorry, you are not allowed to ride! To short!")

# print (f"The bill is {bill}")

#? Love calculator
# #Don't change the code below
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# #Don't change the code above

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count("t")
# l = lower_case_string.count("l")

# love = t+l

# love_score = int(str(t) + str(l))
# print(love_score)

# if love_score <10 or love_score > 90:
#   print(f"Your love score is {love_score}, no chance")
# elif (love_score>=40 and love_score<=50):
#   print(f"Your score is {love_score}, you have a chance")
# else:
#   print(f"Your score is {love_score}")

# Treasure hunting 
# Don't change the code below
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Example: 23: ")
# Don't change the code above

if position[0] or position[1] >3:
  print("not good")
  exit()

map[int(position[0])-1][int(position[1])-1]="X"
print(f"{row1}\n{row2}\n{row3}")

if(position[0]== "2"):
  print("nice")
else:
    print("not_nice")










