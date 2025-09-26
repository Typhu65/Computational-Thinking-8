
builder_points = 0
PVPer_points = 0
redstoner_points = 0
annoying_points = 0
Erebos = 0

print("Welcome to Minecraft Personality Quiz!")

input("Press Enter to start.")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

answer = input("How would you troll your friends on a Server? (A) Build a obsidian wall around their base? (B) Build a TNT cannon and blow up their base? (C) Kill all their animals?")
if answer == " A":
    builder_points += 1
elif answer == " B":
    redstoner_points += 1
elif answer == " C":
    PVPer_points += 1
elif answer == " E":
    Erebos += 1
else:
    print("Choose A, B, or C next time.")
    annoying_points += 1

input("Press Enter to continue.")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

answer = input("If you had an hour of playing Minecraft what would you do? (A) Build a house? (B) Mine for redstone? (C) Grief a friend's base?")
if answer == " A":
    builder_points += 1
elif answer == " B":
    redstoner_points += 1
elif answer == " C":
    PVPer_points += 1
elif answer == " r":
    Erebos += 1
else:
    print("Choose A, B, or C next time.")
    annoying_points += 1

input("Press Enter to continue.")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

answer = input("If your base was griefed by your friends what would you do? (A) Build a monument where it was? (B) Build a tnt cannon to destroy their base? (C) Hunt them down ruthlessly?")
if answer == " A":
    builder_points += 1
elif answer == " B":
    redstoner_points += 1
elif answer == " C":
    PVPer_points += 1
elif answer == " e":
    Erebos += 1
else:
    print("Choose A, B, or C next time.")
    annoying_points += 1

input("Press Enter to continue.")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

answer = input("What is the first thing you do on a Minecraft server started by your friends? (A) Find a location and build a house? (B) Build a secret base with a redstone door? (C) Just start killing people?")
if answer == " A":
    builder_points += 1
elif answer == " B":
    redstoner_points += 1
elif answer == " C":
    PVPer_points += 1
elif answer == " b":
    Erebos += 1
else:
    print("Choose A, B, or C next time.")
    annoying_points += 1

input("Press Enter to continue.")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

answer = input("How do you give somebody a gift in Minecraft? (A) Build them a house? (B) Build them a vault with a big redstone door? (C) Hunt down their arch-nemisis and bring their armour to them?")
if answer == " A":
    builder_points += 1
elif answer == " B":
    redstoner_points += 1
elif answer == " C": 
    PVPer_points += 1
elif answer == " o":
    Erebos += 1
else:
    print("Choose A, B, or C next time.")
    annoying_points += 1

input("Press Enter to continue.")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

answer = input("How would you protect your dog in Minecraft? (A) Build a huge fortess for it? (B) Build automated defenses for its doghouse? (C) Kill everyone else so that no one can kill it?")
if answer == " A":
    builder_points += 1
elif answer == " B":
    redstoner_points
elif answer == " C":
    PVPer_points += 1
elif answer == " s":
    Erebos += 1
else:
    print("Choose A, B, or C next time.")

input("Press Enter to continue.")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

answer = input("Which farm do you like best? (A) A super pretty windmill surrounded by wheat farms? (B) A super complicated kelp farm/auto-smelter? (C) Attack somebody and take over their creeper farm?")
if answer == " A":
    builder_points += 1
elif answer == " B":
    redstoner_points += 1
elif answer == " C":
    PVPer_points += 1
elif answer == " ." or " 1":
    Erebos += 1
    print("Erebos Loading...")
else:
    print("Choose A, B, or C next time.")
    annoying_points += 1



input("Press Enter to see what type of minecraft player you are.")

print("...")

print("Calculating...")

if builder_points > redstoner_points and builder_points > PVPer_points and builder_points > annoying_points and builder_points > Erebos:
    print("You are a builder!")
elif redstoner_points > builder_points and redstoner_points > PVPer_points and redstoner_points > annoying_points and redstoner_points > Erebos:
    print("You are a redstoner!")
elif PVPer_points > builder_points and PVPer_points > redstoner_points and PVPer_points > annoying_points and PVPer_points > Erebos:
    print("You are a PVPer")
elif annoying_points > builder_points and annoying_points > redstoner_points and annoying_points > PVPer_points and annoying_points > Erebos:
    print("You are annoying!!!")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>. YOU ARE ANNOYING!!!!!!!!!!!!!!!!!!!!!!!!")
elif builder_points == redstoner_points:
    print("You are equally a builder and redstoner!")
elif builder_points == PVPer_points:
    print("You are equally a builder and a PVPer!")
elif builder_points == annoying_points:
    print("You are equallly a builder and ANNOYING!!!")
elif redstoner_points == PVPer_points:
    print("You are equally a redstoner and a PVPer!")
elif redstoner_points == annoying_points:
    print("You are equally a redstoner and ANNOYING!!!")
elif PVPer_points == annoying_points:
    print("You are equally a PVPer and ANNOYING!!! ")
elif Erebos == 7:
    print("Welcome to Erebos.")

print("GOOD JOB.")
















































