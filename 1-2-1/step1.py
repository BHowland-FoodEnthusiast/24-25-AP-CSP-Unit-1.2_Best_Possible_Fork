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
font_setup = "arial", 20, "normal"
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.color(fill_color)
spot.shapesize(spot_size, spot_size)
spot.penup()
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-390, 280)
score_writer.pendown()
counter = trtl.Turtle()
counter.penup()
counter.goto(-370, 280)
counter.pendown()
#-----game functions--------
def spot_click(x, y):
    global timer_up
    if timer_up == False:
        spot.penup()
        spot.hideturtle()
        change_position()
        spot.showturtle()
    else:
        spot.hideturtle()

def change_position():
    new_xpos = rand.randint(-400, 400)
    new_ypos = rand.randint(-300, 300)
    update_score()
    spot.goto(new_xpos, new_ypos)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
countdown()
spot.onclick(spot_click)
wn = trtl.Screen()
wn.mainloop()
wn.ontimer(countdown, counter_interval)