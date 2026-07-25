# ? User example
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1


# user_1 = User("001", "john_doe")
# user_2 = User("002", "jane_doe")


# user_1.follow(user_2)

# # user_1.id = "002"
# # user_1.username = "john_doe"

# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)


# ? Quiz example
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
# quiz.next_question()


while quiz.still_has_questions():
    quiz.next_question()
    # quiz.check_answer(input("Enter your answer: "), quiz.next_question())

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
