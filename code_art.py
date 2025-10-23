import turtle
import random
# ###############################################

t = turtle.Turtle()
t.penup
t.goto(0,0)

# I changed the backround to black to pop more.

turtle.Screen().bgcolor("Black")

t.speed(10)


t.pendown()
colors = ["red", "orange", "yellow" ]

# First Circle

t.goto(0,0)

for i in range (100):
    t.forward(40+i)
    t.left(100)
    t.color(random.choice(colors))
    t.forward(100+i)
    t.color(random.choice(colors))
    t.left(100)

# Second Circle

t.penup
t.goto(200,200)
t.pendown 

for i in range (100):
    t.forward(40+i)
    t.left(100)
    t.color(random.choice(colors))
    t.forward(100+i)
    t.color(random.choice(colors))
    t.left(100)

# Third Circle

t.penup
t.goto(-200,200)
t.pendown 

for i in range (100):
    t.forward(40+i)
    t.left(100)
    t.color(random.choice(colors))
    t.forward(100+i)
    t.color(random.choice(colors))
    t.left(100)

t.penup
t.goto(-200,-200)
t.pendown 

for i in range (100):
    t.forward(40+i)
    t.left(100)
    t.color(random.choice(colors))
    t.forward(100+i)
    t.color(random.choice(colors))
    t.left(100)

t.penup
t.goto(200,-200)
t.pendown 

for i in range (100):
    t.forward(40+i)
    t.left(100)
    t.color(random.choice(colors))
    t.forward(100+i)
    t.color(random.choice(colors))
    t.left(100)














turtle.exitonclick ()




