# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

#-----game configuration----
fill_color = "pink"
spot_size = 20
spot_shape = "circle"

#-----initialize turtle-----
spot = trtl.Turtle()
trtl.shape(spot_shape)
trtl.color(fill_color)
spot.shapesize(spot_size, spot_size)

#-----game functions--------
def spot_click(x, y):
    print("Hello World!")


#-----events----------------
spot.onclick(spot_click)
wn = trtl.Screen()
wn.mainloop()