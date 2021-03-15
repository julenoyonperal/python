from question_model import Question
from data import question_data



question_data[1]["text"]
question_data[1]["answer"]

question_bank = list()

question_bank = []

for i in range(len(question_data)):
  question_bank.append(Question(question_data[i]["text"],
                                question_data[i]["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    
print(f"You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_numbre}")