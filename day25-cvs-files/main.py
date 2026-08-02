# 1. Read the weather data from the CSV file
# from pathlib import Path

# with open(Path(__file__).parent / "weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)

# # 2. Convert the data to a list of dictionaries

# import csv

# with open(Path(__file__).parent / "weather_data.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# import csv
# from pathlib import Path

# with open(Path(__file__).parent / "weather_data.csv", "r") as file:
#     # reader = csv.DictReader(file)
#     reader = csv.reader(file)
#     temperatures = []
#     for row in reader:
#         if row[0] != "day":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# ? DataFrames
# from pathlib import Path

# import pandas as pd

# data = pd.read_csv(Path(__file__).parent / "weather_data.csv")
# print(data)
# print(data["temp"])

# print(data.to_dict())
# print(data["temp"].to_list())

# # get the average temperature
# print(data["temp"].mean())

# # get the maximum temperature
# print(data["temp"].max())

# # get the minimum temperature
# print(data["temp"].min())


# # get data in columns
# print(data["condition"])
# print(data.condition)

# # get data in rows
# print(data[data.day == "Monday"])

# # get the row where the temperature is the highest
# print(data[data.temp == data.temp.max()])

# # create a dataframe from scratch
# new_data = pd.DataFrame(
#     {
#         "day": [
#             "Monday",
#             "Tuesday",
#             "Wednesday",
#             "Thursday",
#             "Friday",
#             "Saturday",
#             "Sunday",
#         ],
#         "temp": [12, 14, 15, 18, 22, 11, 23],
#         "condition": ["Sunny", "Rain", "Rain", "Cloudy", "Sunny", "Sunny", "Sunny"],
#     }
# )
# print(new_data)


# # ? Great squires park Squirrel Data
# data = pd.read_csv(
#     Path(__file__).parent / "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
# )
# print(data)

# # get the data in columns
# print(data["Primary Fur Color"])
# print(data["Primary Fur Color"])

# # get the data in rows
# print(data[data["Primary Fur Color"] == "Gray"])

# # get the data in rows where the Primary Fur Color is Gray
# print(data[data["Primary Fur Color"] == "Gray"].count())

# # get the data in rows where the Primary Fur Color is Gray
# print(data[data["Primary Fur Color"] == "Gray"].count())

# # get the data in rows where the Primary Fur Color is Gray
# print(data[data["Primary Fur Color"] == "Gray"].count())

# data_dict = data[data["Primary Fur Color"] == "Gray"].to_dict()
# print(data_dict)

# ? US state game
import turtle
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).parent
IMAGE = str(BASE_DIR / "blank_states_img.gif")

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv(BASE_DIR / "50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv(BASE_DIR / "states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(int(state_data.x.item()), int(state_data.y.item()))
        writer.write(answer_state)

screen.exitonclick()
