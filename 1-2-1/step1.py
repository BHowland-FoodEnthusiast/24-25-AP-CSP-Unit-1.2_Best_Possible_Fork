# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
fill_color = "pink"
spot_size = 2
spot_shape = "circle"
global score
score = 0
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.color(fill_color)
spot.shapesize(spot_size, spot_size)
spot.penup()
score_writer = trtl.Turtle

#-----game functions--------
def spot_click(x, y):
    spot.penup()
    spot.hideturtle()
    change_position()
    spot.showturtle()

def change_position():
    new_xpos = rand.randint(-400, 400)
    new_ypos = rand.randint(-300, 300)
    update_score()
    spot.goto(new_xpos, new_ypos)

def update_score():
    global score
    score += 1
    print(score)


#-----events----------------
spot.onclick(spot_click)
wn = trtl.Screen()
wn.mainloop()