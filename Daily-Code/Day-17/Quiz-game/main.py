from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]
for q_s in question_data:
    question_text=q_s['text']
    question_answer=q_s['answer']
    new_question=Question(question_text, question_answer)
    question_bank.append(new_question)
    
#print(len(question_bank))
#print(question_bank)
quiz= QuizBrain(question_bank)  

while quiz.still_has_question():
    quiz.next_question()
    
print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


#REFERENCE:
'''
https://opentdb.com/
HERE WE GENERATED THE QUESTIONS FROM THIS WESITE
'''