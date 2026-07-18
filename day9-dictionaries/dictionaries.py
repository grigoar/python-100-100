
#? dictionary - {key: value}
# programming_dictionary = {"bug": "a nice bug",
# "function":"group things"
# }

# programming_dictionary["bug"] = "new value"

# print(programming_dictionary)

# programming_dictionary["Loop"] = "Some loop"
# print(programming_dictionary)

# # empty dictionary
# empty_dictionary={}

# # loop through a dictionary

# for key in programming_dictionary:
#   print(key)
#   print (programming_dictionary[key])

#? student scores

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#   if student_scores[student]>90:
#     student_grades[student]="Outstanding"
#   elif student_scores[student]>80:
#     student_grades[student]="Exceed Expectations"
#   elif student_scores[student]>70:
#     student_grades[student]="Acceptable"
#   else:
#     student_grades[student] = "Fail"

# print(student_grades)

# ? Nesting

# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin"
# }

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   }
# ]

# def add_new_country(country, visits, cities):
#   new_country = {}
#   new_country["country"] = country
#   new_country["visits"] = visits
#   new_country["cities"] = cities

#   newCountry2 ={
#     "country": country,
#     "visits": visits,
#     "cities": cities
#   }
#   travel_log.append(new_country)
#   travel_log.append(newCountry2)
#   print(travel_log)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# from replit import clear

#? secret auction program
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  winner = ""
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest_bid}")
  
  bidding_finished = False
  while not bidding_finished:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
      bidding_finished = True
      find_highest_bidder(bids)
      
    else:
      # clear()
      find_highest_bidder(bids)

print(bids)

find_highest_bidder(bids)

