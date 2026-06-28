
# #? Hangman (by me)
# import random 

# word_list = ["banana", "find", "abracadabra"]

# word_picked = random.choice(word_list)

# letters_words_picked = list(word_picked)
# print(letters_words_picked)

# word_guessed = []

# for letter in range (0, len(word_picked)):
#   word_guessed.append("__ ")


# finalStage = "DEAD"

# initialStage = ""

# while initialStage != finalStage:
#   print(f"Word to find: {("".join(word_guessed))}")

#   user_letter = input("Guess a letter: ").lower()
  
#   isLetterInWord = False

#   for index in range (0, len(letters_words_picked)):
#     if user_letter == letters_words_picked[index]:
#       isLetterInWord=True
#       word_guessed[index] = letters_words_picked[index]
    
#   if not isLetterInWord:
#     if initialStage=="":
#       initialStage="D";
#     elif initialStage=="D":
#       initialStage="DE";
#     elif initialStage=="DE":
#       initialStage="DEA";
#     elif initialStage=="DEA":
#       initialStage="DEAD"

#   print(f"You are in stage: {initialStage}. Game stops at {finalStage}.")
#   if "__" not in "".join(word_guessed):
#     print("You win")
#     break


# #? Hangman (by me) - improved
import random
# import word_list
from word_list import words

# word_list = ["banana", "find", "abracadabra"]
word_list = words

word_picked = random.choice(word_list)

letters_words_picked = list(word_picked)
print(letters_words_picked)

word_guessed = []

for letter in range (0, len(word_picked)):
  word_guessed.append("__ ")


finalStage = "DEAD"

initialStage = ""

def checkLetterInWord():
  isLetterInWord = False

  for index in range (0, len(letters_words_picked)):
    if user_letter == letters_words_picked[index]:
      isLetterInWord=True
      word_guessed[index] = letters_words_picked[index]
  
  return isLetterInWord

def checkStage(isLetterInWord: bool):
  global initialStage
  if not isLetterInWord:
    if initialStage=="":
      initialStage="D";
    elif initialStage=="D":
      initialStage="DE";
    elif initialStage=="DE":
      initialStage="DEA";
    elif initialStage=="DEA":
      initialStage="DEAD"
  return initialStage

while initialStage != finalStage:
  print(f"Word to find: {("".join(word_guessed))}")

  user_letter = input("Guess a letter: ").lower()
  
  isLetterInWord = checkLetterInWord()
    
  checkStage(isLetterInWord)

  print(f"You are in stage: {initialStage}. Game stops at {finalStage}.")
  if "__" not in "".join(word_guessed):
    print("You win")
    break