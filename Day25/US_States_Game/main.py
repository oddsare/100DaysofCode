import turtle
import pandas
screen = turtle.Screen()

screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



def get_state(user_guess):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state.color("Black")
    
    state_row = state_answer[state_answer.state == user_guess]
    
    x = state_row.x.item()
    y = state_row.y.item()
    state.goto(x,y)
    state.write(user_guess,False,"Center",("Arial",10,"normal"))
game_is_on = True
guessed_states = []
state_answer = pandas.read_csv("50_states.csv")


#to_csv = pandas.DataFrame(state_answer["state"].items())

#to_csv.to_csv("All States")



while game_is_on:

    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct","Whats another state's name? ").title()
    
    
    if answer_state == "Exit":
        missing = state_answer[~state_answer.state.isin(guessed_states)]
        missing_questions = pandas.DataFrame(missing)
        missing_questions.to_csv("Missing_States")
        break

    for state in state_answer.state:
        if state == answer_state and state not in guessed_states:
            
            
            
            guessed_states.append(state) 
            get_state(answer_state)
        if len(guessed_states) == 50:
            
            game_is_on = False


turtle.mainloop()

