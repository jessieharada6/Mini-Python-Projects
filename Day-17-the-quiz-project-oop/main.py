from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q['question'],q['correct_answer']))
# print(question_bank)
# for q in question_bank:
#     print(q.text)

quiz = QuizBrain(question_bank)
# print(quizBrain.questions_list)

while quiz.still_has_questions():
    quiz.next_question()

# quizBrain.display_result()
print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")