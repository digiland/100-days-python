# ask question
class QuizBrain:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_bank[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {question.text} (True/ False)")
        self.check_answer(answer, question.answer)

    def more_questions(self):
        return self.question_number < len(self.question_bank)

        # check if answer is correct
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
            print(f"Your score is {self.score} \n\n")
        else:
            print("Wrong!\n\n")
