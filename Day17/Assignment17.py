from question_model import Question
from data import question_data
from quiz_brain import Brain


question_data =question_data
question_bank = []



for i in range(len(question_data)):
    question_text = question_data[i]["text"]
    question_answer =question_data[i]["answer"]
    new_question = Question(question_text,question_answer)

    question_bank.append(new_question)


quiz = Brain(question_bank)
while quiz.remaining_questions() :
    
    quiz.next_question()
    
print("You've completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")