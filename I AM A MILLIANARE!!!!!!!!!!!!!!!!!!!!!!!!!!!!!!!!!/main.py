from Question import Question
from QuestionMaster import QuestionMaster
from question_list import questions_and_answers
question_bank = []
for question in questions_and_answers:
    question_bank.append(Question(question["question"], question["answer"]))
question_master = QuestionMaster(q_list=question_bank)
question_master.start_quiz()