# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
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

def get_distance(s1, s2):
    dx = s1.xcor() - s2.xcor()
    dy = s1.ycor() - s2.ycor()
    return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)


######################################################################
# Section 2 - Your code
sprite1 = create_sprite("knight1", -200, -110)
set_background("castle_ruins_black")
sprite2 = create_sprite("text _bubble", 0, 0)
sprite3 = create_sprite("fish", -85,20)
sprite3.hideturtle()
sprite3.write("I am the messenger.")
sprite3.goto(-85, -7)
sprite3.write("Welcome to Erebos.")

sprite2 = create_sprite("alien",-120,150)
sprite2.color("red")
sprite2.write("Erebos",font = ("Arial", 40, "normal"))
sprite2.hideturtle()
######################################################################


# Section 3 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()




