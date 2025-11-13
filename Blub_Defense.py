# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random, math

sprite_width = 80
sprite_height = 100

class RectangleHitbox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.right = x + width
        self.bottom = y + height

    def is_colliding(self, hit_box):
        return (self.x < hit_box.right and
                self.right > hit_box.x and
                self.y < hit_box.bottom and
                self.bottom > hit_box.y)

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
dog_sprite = create_sprite("gurb",0,-200)
zombie_sprite = create_sprite("zombie",300,0)
brick_sprites = []
# Create the original sprite
#original_sprite = turtle.Turtle()
#original_sprite = create_sprite("bricks")
#original_sprite.speed(0) # Fastest speed for instant creation
obstacles = []
clones = []


def collides_with_bricks(zombie_hitbox) :

    # iterate through all the brick sprites and check collision against the zombie hitbox
    for brick_sprite in brick_sprites:

        brick_hitbox = RectangleHitbox(brick_sprite.pos()[0], brick_sprite.pos()[1], sprite_width, sprite_height)
        if zombie_hitbox.is_colliding(brick_hitbox):
            return True
        
    return False

# The beginning of my dad's part

def update_zombie_position():  

   # print (str.format("zombie_shapesize: {0}, zombie position: {1}",zombie_sprite., zombie_sprite.pos()))

    zombie_move_speed = 0.8

    # create a normalized (length = 1) vector in the direction from the zombie to the dog
    zombie_to_dog_vec = [dog_sprite.pos()[0]-zombie_sprite.pos()[0], dog_sprite.pos()[1] - zombie_sprite.pos()[1]]
    magnitude = math.sqrt(zombie_to_dog_vec[0]*zombie_to_dog_vec[0] + zombie_to_dog_vec[1]*zombie_to_dog_vec[1])
    normalized_zombie_to_dog_vec = [zombie_to_dog_vec[0]/magnitude, zombie_to_dog_vec[1]/magnitude]


    candidate_zombie_pos = [zombie_sprite.pos()[0]+zombie_move_speed*normalized_zombie_to_dog_vec[0],
                         zombie_sprite.pos()[1]+zombie_move_speed*normalized_zombie_to_dog_vec[1]]

    zombie_hitbox = RectangleHitbox(candidate_zombie_pos[0], candidate_zombie_pos[1], sprite_width, sprite_height)
    
    if collides_with_bricks(zombie_hitbox):
        # check keeping x vector constant

        x_offset = 1 if normalized_zombie_to_dog_vec[0] >= 0 else -1 
        y_offset = 1 if normalized_zombie_to_dog_vec[1] >= 0 else -1 

        candidate_zombie_pos = [zombie_sprite.pos()[0],
                         zombie_sprite.pos()[1]+zombie_move_speed*y_offset]
        zombie_hitbox = RectangleHitbox(candidate_zombie_pos[0], candidate_zombie_pos[1], sprite_width, sprite_height)

        if collides_with_bricks(zombie_hitbox):
            #check keep y vector constant
            candidate_zombie_pos = [zombie_sprite.pos()[0]+zombie_move_speed*x_offset,
                         zombie_sprite.pos()[1]]
            zombie_hitbox = RectangleHitbox(candidate_zombie_pos[0], candidate_zombie_pos[1], sprite_width, sprite_height)
            #change collision variable by one 

            if collides_with_bricks(zombie_hitbox):
                return
    zombie_sprite.setpos(candidate_zombie_pos[0], candidate_zombie_pos[1])   
#
# The end of my dad's part
#
    #angle_radians = math.atan2(zombie_sprite.pos()[1] - dog_sprite.pos()[1], zombie_sprite.pos()[0] - dog_sprite.pos()[0])    
    #angle_degrees = 180.0 + angle_radians * (180.0/math.pi)
    #zombie_sprite.setheading(angle_degrees)
    #zombie_sprite.forward(30.0/60.0)
    
    #print (str.format('angle in radians: {0}, angle in degrees {1}',angle_radians, angle_degrees))

    #print(angle_degrees)
    #print(ball_sprite.pos())
    #print(dog_sprite.pos())

#if dog_sprite (xpos) =


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

def create_clone():
    new_clone = turtle.Turtle()
    new_clone.shape(original_sprite.shape)
    new_clone.speed(0)


def check_hit_box(target_sprite, candidate_enemy_position):
    # check if zombie_sprite is within target sprite bounds
    print ("zombie_shapesize: {0}",zombie_sprite.shapesize)


def mouse_click(mouse_x, mouse_y):

    zombie_hitbox = RectangleHitbox(zombie_sprite.pos()[0], zombie_sprite.pos()[1], sprite_width, sprite_height)
    brick_hitbox = RectangleHitbox(mouse_x, mouse_y, sprite_width, sprite_height)

    if not zombie_hitbox.is_colliding(brick_hitbox) and len(brick_sprites) < 10:
        brick_sprite = create_sprite("bricks",0,0)
        brick_sprite.setpos(mouse_x,mouse_y)
        brick_sprites.append(brick_sprite)

def zombie_touches_dog():

    zombie_hitbox = RectangleHitbox(zombie_sprite.pos()[0], zombie_sprite.pos()[1], sprite_width, sprite_height)
    dog_hitbox = RectangleHitbox(dog_sprite.pos()[0], dog_sprite.pos()[1], sprite_width, sprite_height)
    return zombie_hitbox.is_colliding(dog_hitbox)

window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")
window.onscreenclick(mouse_click)
# Section 4: define other controls
# hide and show controls


def hide():
    dog_sprite()
def show():
    dog_sprite()



window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

# if zombie_sprite.pos()[0] == dog_sprite.pos()[0] and not zombie_hitbox.is_colliding(brick_hitbox):
#    zombie_sprite.setheading(zombie_sprite + 180)
#     for i in range (10):
#         go_forward(10)

#if zombie_sprite.pos()[1] == dog_sprite.pos()[1] and not zombie_hitbox.is_colliding(brick_hitbox):
   
   # zombie_sprite.setheading(zombie_sprite += 180)
    #for i in range (10):
     #   go_forward(10)


# Section 5: game loop
window.listen()
timer = 0
while True:
    sleep_time = 0.016666
    time.sleep(sleep_time)
    timer += sleep_time

    update_zombie_position()
    
    if zombie_touches_dog():
        print("You survived")
        print({timer})
        print("seconds, good job!")
        turtle.hideturtle() 
        break

        

    window.update()
    