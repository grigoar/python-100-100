# print("Hello"[0])

# # Large numbers can have _
# print (1_11+ 111)

# # FLOAT
# print (3.1223)

# #BOOLEAN

# print (True)
# print (False)

# num_char = len(input("What is your name?"))
# print (type(num_char))

# print ("your name has " + str(num_char) + " characters.")

# a = float(123)

# print (type(a))

# print (a)


# Exercise 1
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# two_digit_number = input("Type a two digit number: ")

# print(type(two_digit_number))

# first_digit= two_digit_number[0]
# second_digit = two_digit_number[1]
# print (str(first_digit)+ " + " + str(second_digit) + " = "+ str(int(first_digit) + int(second_digit))) # 3 + 4 = 7

# More operations
# print ( 2 ** 3)

# BMI calculator : BMI = w(kg) / height * height (m2)

# height = input("enter your height in m (ex: 1.75):")
# weight = input ("enter your weight in kg (ex: 83):")

# bmi  = float(weight) / (float(height) *float(height))

# bmi_int = int(bmi)
# print("your BMI is:" + str(bmi))
# print (bmi_int)
# print ("rounded" + str(round(bmi,2)))

# print (8 /3)
# result = 4/2
# result/=2
# print(result)

# score = 0
# score +=1
# print(score)

# height = 1.8
# isWinning = True
# #f-String
# print (f"your score is {score}, height - {height} , winning - {isWinning}")

# Your life in weeks
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input 

# my_age_s = input("What is your current age?")
# my_age = float(my_age_s)
# max_age = 90

# max_months = max_age * 12
# max_weeks = max_age * 52
# max_days = max_age*365

# my_months_left = max_months-(my_age*12)
# my_weeks_left = max_weeks - (my_age*52)
# my_days_left = max_days - (my_age * 365)

# print(f"You have {my_days_left} days, {my_weeks_left} weeks, and {my_months_left} months left")

# Tip calculator
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

print ("Welcoome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip_percentage=float(input("What percentage tip would you like to give? 10, 12, or 15?"))
total_people=int(input ("How many people to split the bill?"))

# result = round(float(bill/total_people) * (tip_percentage/100 +1),2)
result = round(float((tip_percentage/100 *bill +bill)/total_people ), 2)

final_amount = f"{result:.2f}"

print(f"Each person should pay: ${result:.2f}")