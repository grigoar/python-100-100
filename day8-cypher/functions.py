
#? Functions
# def greet():
#   print("hello")
#   print("How are you are?")
#   print("The weather sucks")

# greet()

#? function with input

# def greet_with_name(name):
#   print(f"hello {name}")
#   print(f"How are you are {name}?")
#   print(f"The weather sucks, {name}")

# greet_with_name("Grigore")

#? function with multiple inputs

# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"How is the weather in {location}, {name}?")
# greet_with("Grig", "Cluj")

#? function with multiple inputs, positional arguments

# def greet_with( location,name):
#     print(f"hello {name}")
#     print(f"How is the weather in {location}, {name}?")
# greet_with(name="Grig", location="Cluj")

#? area of a wall calculator

# import math
# def paint_calc(height, width, cover):
#   nr_cans = (height * width / cover)
#   print(f"I need {math.ceil(nr_cans)} of paint")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#? Prime number checker

# def prime_checker(number):
#   isPrime= True
#   if number == 2 or number == 3:
#     return print(f"The {number} is prime number")
#   for i in range(2, int(number/2)):
#     if number%i== 0:
#       isPrime=False
#       return print(f"The {number} is not prime")
#   if isPrime: print(f"The {number} is prime")
  


# number = int(input("Check this number: "))
# prime_checker(number)

#? Caesar Cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):

  if direction == "encode":
    encoded =""

    for ch in text:
      if ch in alphabet:
        index = alphabet.index(ch)
        new_index = (index + shift) % 26
        encoded += alphabet[new_index]
      else:
        encoded += ch
    return print(f"The encoded text is {encoded}")
  else:
    decoded=""
    for ch in text:
      if ch in alphabet:
        index = alphabet.index(ch)
        new_index = (index-shift) %26
        decoded+=alphabet[new_index]
      else:
        decoded +=ch
    return print(f"The decoded text is {decoded}")

text = input("Type your message: ")
shift = int(input("Type the shift number: "))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
caesar(text, shift, direction)