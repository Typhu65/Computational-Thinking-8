# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("dungeon")
s1 = create_sprite("cool_dog",0,-200)
s2 = create_sprite("corgi",0,-200)
# Section 3: define movement controls

def move_up():
    s1.setheading(90)
    s1.forward(10)
        
def move_down():
    s1.setheading(270)
    s1.forward(10)
    
def move_left():
    s1.setheading(180)
    s1.forward(10)
    
def move_right():    
    s1.setheading(0)
    s1.forward(10)

def draw ():
    s1.pendown()

def stop_drawing ():
    s1.penup()

def red_pen ():
    s1.color("red")

def orange_pen ():
    s1.color("orange")

def yellow_pen ():
    s1.color("yellow")

def green_pen ():
    s1.color("green")

def blue_pen ():
    s1.color("blue")

def purple_pen ():
    s1.color("purple")

def black_pen ():
    s1.color("black")

def reset():
    s1.goto(0,-200)
window.onkeypress(reset, "r")
window.onkeypress(move_up, "w")
window.onkeypress(move_left, "a")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(draw, "c")
window.onkeypress(stop_drawing, "v")
window.onkeypress(red_pen, "1")
window.onkeypress(orange_pen, "2")
window.onkeypress(yellow_pen, "3")
window.onkeypress(green_pen, "4")
window.onkeypress(blue_pen, "5")
window.onkeypress(purple_pen, "6")
window.onkeypress(black_pen, "0")



def move_up():
    s2.setheading(90)
    s2.forward(10)
        
def move_down():
    s2.setheading(270)
    s2.forward(10)
    
def move_left():
    s2.setheading(180)
    s2.forward(10)
    
def move_right():    
    s2.setheading(0)
    s2.forward(10)

def draw ():
    s2.pendown()

def stop_drawing ():
    s2.penup()

def red_pen ():
    s2.color("red")

def orange_pen ():
    s2.color("orange")

def yellow_pen ():
    s2.color("yellow")

def green_pen ():
    s2.color("green")

def blue_pen ():
    s2.color("blue")

def purple_pen ():
    s2.color("purple")

def black_pen ():
    s2.color("black")

def reset():
    s2.goto(0,200)
window.onkeypress(reset, "r")
window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")
window.onkeypress(draw, "c")
window.onkeypress(stop_drawing, "v")
window.onkeypress(red_pen, "1")
window.onkeypress(orange_pen, "2")
window.onkeypress(yellow_pen, "3")
window.onkeypress(green_pen, "4")
window.onkeypress(blue_pen, "5")
window.onkeypress(purple_pen, "6")
window.onkeypress(black_pen, "0")
# Section 4: define other controls
# hide and show controls
def hide():
    s1 or s2.hideturtle()
def show():
    s1 or s2.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 5: game loop
window.listen()
while True:
    time.sleep(0.000000000001)
    window.update()