#   a123_apple_1.py
import turtle as trtl

#-----setup-----
letter = "A"
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
apple = trtl.Turtle()
wn.bgpic("background.gif")
pear = trtl.Turtle()
letter_draw = trtl.Turtle()
letter_draw.penup()
letter_draw.goto(200, 200)
letter_draw.pendown()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_letter()
  wn.update()

def draw_letter():

  letter_draw.color("white")
  letter_draw.write("A", font=("Arial", 74, "bold"))

def fall_apple():
  apple.setheading(270)
  apple.forward(150)

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()
#-----function calls-----
wn.listen()
wn.onkeypress(fall_apple, letter)
draw_apple(apple)
draw_pear(pear)
wn.mainloop()