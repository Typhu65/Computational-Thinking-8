# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random, math


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
    sprite.shapesize(50,50)
    sprite.goto(x,y)
    window.update()
    return sprite

window = turtle.Screen()
window.tracer(0)
# Section 2: Setup
set_background("grass")
dog_sprite = create_sprite("cool_dog",0,-200)
brick_sprite = create_sprite("bricks",0,0)
zombie_sprite = create_sprite("zombie",300,0)
timer = 0
obstacles = []
#position_of_s1 = 
# Section 3: define movement controls

#if timer % 10 == 0:
#    y_position = random.randint (-250, 250)
#    zombie_sprite = create_sprite("basketball", 300, y_position)
#    zombie_sprite.setheading(180)
#    obstacles.append(zombie_sprite)
# s3.setheading(to_angle=s1)


def check_hit_box(target_sprite, candidate_enemy_position):
    # check if zombie_sprite is within target sprite bounds
    print ("zombie_shapesize: {0}",zombie_sprite.shapesize)

def update_zombie_position():  

   # print (str.format("zombie_shapesize: {0}, zombie position: {1}",zombie_sprite., zombie_sprite.pos()))

    angle_radians = math.atan2(zombie_sprite.pos()[1] - dog_sprite.pos()[1], zombie_sprite.pos()[0] - dog_sprite.pos()[0])    
    angle_degrees = 180.0 + angle_radians * (180.0/math.pi)
    zombie_sprite.setheading(angle_degrees)
    zombie_sprite.forward(15.0/60.0)
    
    #print (str.format('angle in radians: {0}, angle in degrees {1}',angle_radians, angle_degrees))

    #print(angle_degrees)
    #print(ball_sprite.pos())
    #print(dog_sprite.pos())


def move_up():
    dog_sprite.setheading(90)
    dog_sprite.forward(10)
        
def move_down():
    dog_sprite.setheading(270)
    dog_sprite.forward(10)

def move_left():
    dog_sprite.setheading(180)
    dog_sprite.forward(10)
    
def move_right():    
    dog_sprite.setheading(0)
    dog_sprite.forward(10)

window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")

# Section 4: define other controls
# hide and show controls
def hide():
    dog_sprite or brick_sprite.hideturtle()
def show():
    dog_sprite or brick_sprite.showturtle()

 # if block_placement % 10 == 0:

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 5: game loop
window.listen()
while True:
    time.sleep(0.016666)
    update_zombie_position()
    
    window.update()