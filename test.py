import turtle
import random
# Create the main screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Sprite Cloning with Keypress")

# Create the original sprite
original_sprite = turtle.Turtle()
original_sprite.shape("circle")
original_sprite.color("blue")
original_sprite.penup()
original_sprite.speed(0) # Fastest speed for instant creation

# List to store the cloned sprites
clones = []

# Function to create a clone on keypress
def create_clone():
    new_clone = turtle.Turtle()
    new_clone.shape(original_sprite.shape())
    new_clone.color(original_sprite.color())
    new_clone.penup()
    new_clone.speed(0)
    
    # Position the clone near the original sprite or at a specific location
    new_clone.goto(original_sprite.xcor() + 20, original_sprite.ycor()) 
    
    clones.append(new_clone)
    print(f"Clone created. Total clones: {len(clones)}")

# Assign the create_clone function to a keypress
screen.onkey(create_clone, "space") # Press the spacebar to create a clone

# Listen for keypresses
screen.listen()

# Keep the window open
screen.mainloop()



