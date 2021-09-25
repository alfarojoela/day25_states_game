import turtle

def get_mouse_click_coord(x, y):
    print(x,y)

screen = turtle.Screen()

screen.title("U.S. States Game")

#file location saved as variable
image = "blank_states_img.gif"

#object method to place image into screen
screen.addshape(image)

#turtle object needs to have shape changed to image
turtle.shape(image)


turtle.onscreenclick(get_mouse_click_coord)  #sends above function to read x and y coords

turtle.mainloop()  #keeps screen open after code runs


