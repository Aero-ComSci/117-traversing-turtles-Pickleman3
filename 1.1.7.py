import turtle as trtl
trtl.speed(0)
trtl.pensize(20)
my_turtles = []
#Make a data base
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

#Make aclass
class pain:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0

    def create_turtles(self):
        for i in turtle_shapes:
            t = trtl.Turtle(shape=i)
            my_turtles.append(t)
            t.pencolor(turtle_colors[0])
            t.fillcolor(turtle_colors[0])
            turtle_colors.pop(0)

    def move_turtles(self):
        x = 0 
        for t in my_turtles:
            t.penup()
            t.goto(self.xpos, self.ypos)  
            t.pendown()
            t.right(30 + x)
            t.forward(80)
            self.xpos = t.xcor()  
            self.ypos = t.ycor()  
            x += 50           

t = pain()
t.create_turtles() 
t.move_turtles()    

wn = trtl.Screen()
wn.mainloop()
