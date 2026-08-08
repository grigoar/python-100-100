# # List Comprehension

# numbers = [1, 2, 3, 4, 5]
# # ? squared = [n**2 for n in numbers]
# squared = [number**2 for number in numbers]
# print(squared)

# # ? List Comprehension with if statement
# numbers = [1, 2, 3, 4, 5]
# squared = [n**2 for n in numbers if n % 2 == 0]
# print(squared)

# # ? List Comprehension with if else statement
# numbers = [1, 2, 3, 4, 5]
# squared = [n**2 if n % 2 == 0 else n for n in numbers]
# print(squared)

# # ? List comprehension for letter in word
# word = "hello"
# letters = [letter for letter in word]
# print(letters)

# # ? List comprehension for number in range
# numbers = [number for number in range(1, 10)]
# print(numbers)

# # ? List comprehension for number in range with step
# numbers = [number for number in range(1, 10, 2)]
# print(numbers)

# # ? List comprehension for number in range with step and if statement
# numbers = [number for number in range(1, 10) if number % 2 == 0]
# print(numbers)

# # ? List comprehension for number in range with step and if else statement
# numbers = [number if number % 2 == 0 else number**2 for number in range(1, 10)]
# print(numbers)


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# # ? Dictionary Comprehension
# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_scores = {name: random.randint(0, 100) for name in names}
# print(student_scores)

# passed_students = {
#     name: score for (name, score) in student_scores.items() if score >= 60
# }
# print(passed_students)

# sentence = "What is the Airspeed Velocity, of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split(" ")}
# print(result)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# names_length = {name: len(name) for name in names}
# print(names_length)

# # Weather Data
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# # loop through pandas dataframe
# import pandas as pd

# student_data_frame = pd.DataFrame(
#     {
#         "student": list(student_scores.keys()),
#         "score": list(student_scores.values()),
#     }
# )
# print(student_data_frame)

# for index, row in student_data_frame.iterrows():
#     print(row.student, row.score)


# ? Nato Alphabet Project
import pandas as pd

data = pd.read_csv("day26-lists-comprehension/nato_phonetic_alphabet.csv")
print(data)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

word = input("Enter a word: ").upper()
phonetic_code = [nato_dict[letter] for letter in word]
print(phonetic_code)
