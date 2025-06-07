import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.ht()
writer.penup()

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()
state_coords = state_data.set_index("state").to_dict("index")

number_guesses = 0
number_correct = 0
correct_answers = []

def print_label(state):
    x = state_coords[state]["x"]
    y = state_coords[state]["y"]
    writer.goto(x,y)
    writer.write(state)

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{number_correct}/{number_guesses} States Correct", prompt="What's another state's name")
    number_guesses += 1
    if answer_state:
        answer_state = answer_state.title()
        if answer_state in state_list and answer_state not in correct_answers:
            print_label(answer_state)
            number_correct += 1
            correct_answers.append(answer_state)
        else:
            if answer_state == "Exit":
                game_is_on = False

                #save list of states not guessed
                not_guessed_states = []
                for state in state_list:
                    if not state in correct_answers:
                        not_guessed_states.append(state)
                pandas.DataFrame(not_guessed_states).to_csv("Not_guessed_states.csv")



