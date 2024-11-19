##############################################################################
#   a123_TR_apple_typing_3.py
#   Run code in VS Code to be able to access the images.
#   Example soulution:
#      Code connects to the image of an apple.
#      The apple is located on the image of a tree.
#      The apple does not draw a line as it falls.
#      When A is pressed, the letter A appears on the apple.
#      The apple falls to the ground when the A key is pressed.
#      The apple and letter dissapear after the apple hits the ground.
##############################################################################
import turtle as trtl
import random as rd
from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

# given a turtle, active_apple, set that turtle to be shaped
# by the image file
def draw_apple(active_apple, letter):
    active_apple.shape(apple_image)
    active_apple.showturtle()
    draw_letter(letter, active_apple)
    wn.update()

# This function moves the apple to the ground and hides it.
def drop_apple():
    wn.tracer(True)
    apple.goto(apple.xcor(), ground_height)
    apple.clear()
    apple.hideturtle()
    wn.tracer(False)
    reset_apple(apple)


# letter is of type str
# active_apple is a turtle
def draw_letter(letter, active_apple):
    active_apple.color("white")
    remember_position = active_apple.position()
    active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
    active_apple.write(letter, font=("Arial", 74, "bold"))
    active_apple.setpos(remember_position)

#   a123_apple_and_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty.
def reset_apple(apple):
    if len(letters) > 0:
        newx = rd.randint(-200, 200)
        newY = apple.ycor()
        new_letter = rd.randint(0, len(letters) - 1)
        apple.goto(newx, newY)
        draw_apple(apple, letters.pop(new_letter))
#TODO Create a function that draws a new letter from the letter list.

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
#for i in range(0, number_of_apples):
    #Your code here

#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter
# to disappear. Call the apple resetting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

wn.listen()
trtl.mainloop()
wn.listen()
trtl.mainloop()
draw_apple(apple, letters[rd.randint(0, len(letters) - 1)])
wn.onkeypress(drop_apple)

wn.listen()
trtl.mainloop()
