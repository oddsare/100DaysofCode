class Brain:
    
    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def remaining_questions(self):
        return self.question_number < len(self.question_list)
            
        
        
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer= input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer,current_question.answer)
        
    def check_answer(self,user_answer,correct_anwser):
        if user_answer.lower() == correct_anwser.lower():
            print("You got it right!!")
            self.score += 1
            
        else:
            print("That's Wrong")
        print(f"The correct answer was: {correct_anwser}")
        print(f"you got {self.score} out of {self.question_number}")
        print("\n")
    
        