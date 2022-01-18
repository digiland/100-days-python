from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []

for question in question_data:
    question_bank.append(
        Question(question['question'], question['correct_answer']))


quiz = QuizBrain(question_bank)

while quiz.more_questions():
    quiz.next_question()

print(f"Your final score is {quiz.score}")
