import turtle as trtl
import random as rand
#initalize variables
wn = trtl.Screen()
maze_painter = trtl.Turtle()
length = 20
path_width = 10

#setup turtle
maze_painter.left(90)
maze_painter.speed(0)
maze_painter.pensize(5)

# draw maze
# Process:
# draw a line
# turn left
# increment length
# repeat
def add_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)

for wall in range(21):
    door = rand.randint(path_width * 2, (length - path_width * 2))
    barrier = rand.randint(path_width * 2, (length - path_width * 2))
    maze_painter.forward(length/3)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if wall >= 5:
        add_barrier()
    maze_painter.forward(length - path_width - length/3)
    maze_painter.left(90)
    length += 10




wn.listen()
wn.mainloop()