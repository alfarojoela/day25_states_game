import turtle
import csv
import pandas
from turtle import Turtle


def get_mouse_click_coord(x, y):
    print(x,y)

screen = turtle.Screen()
wrong = turtle.Screen()

screen.title("U.S. States Game")

pointer = Turtle()
pointer.penup()
pointer.hideturtle()
pointer.color("black")


#file location saved as variable
image = "blank_states_img.gif"

#object method to place image into screen
screen.addshape(image)

#turtle object needs to have shape changed to image
turtle.shape(image)

#turtle.onscreenclick(get_mouse_click_coord)  #sends above function to read x and y coords
data = pandas.read_csv("50_states.csv")
state_dict = data.to_dict()  #not sure if this is working
state_list = data["state"].to_list()
#print(state_list)
#print(data)


score = 0
correct_guesses =[]

while score != 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state in state_list:
        score += 1
    #pulls out a row from the Dataframe if answer_state is valid key
        state_listing =data[data.state == answer_state]

    #looks through the row.  finds state information and stores in variable.  values[0] takes index number out
        state_name = state_listing.state.values[0]  #the values[0] takes the index number out
        x_coord = state_listing.x.values[0]
        y_coord = state_listing.y.values[0]

        pointer.goto(x_coord, y_coord)
        pointer.write(state_name)
        correct_guesses.append(state_name)


    # print(state_name)
    # print(x_coord)
    # print(y_coord)


    else:
        print("that is not a state")




#print(state_dict)

turtle.mainloop()  #keeps screen open after code runs


