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


#-----events----------------
wn = trtl.Screen()
wn.mainloop()