import random
# Pick a word at random
word_list = ["adder", "actor", "baron", "backs", "chick", "chalk", "demur", "drill", "enter", "exits", "fills", "ferns", "gates", "gapes", "hills", "halve", "iller", "icons" "jacks", "jeans", "kills", "karma", "lives", "livid", "minor", "macho", "newly", "nexus", "oasis", "oaken", "poppy", "pzazz", "query", "quirk", "right", "rings", "sings", "shins", "thigh", "thrum", "under", "usher", "visit", "vines", "wines", "wicks", "xerox", "xylol", "yacks", "yacht", "zippy", "zebra" ]

#word_list = []

#with open("wordle.txt", "r") as file:
#    the_file_content = file.read()
#    word_list.extend(the_file_content.split("\n"))

hidden_word = random.choice(word_list)
print("WORDLE! You have 6 guesses - good luck!")


# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""
    if len(guess_word) == 5:
        # First letter (in python, counting starts at 0 not 1)
        if guess_word[0] == hidden_word[0]:
            output += "🟩"
        elif guess_word[0] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # Second letter 
        if guess_word[1] == hidden_word[1]:
            output += "🟩"
        elif guess_word[1] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"
        
        # Third letter 
        if guess_word[2] == hidden_word[2]:
            output += "🟩"
        elif guess_word[2] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # Fourth letter 
        if guess_word[3] == hidden_word[3]:
            output += "🟩"
        elif guess_word[3] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # Fifth letter 
        if guess_word[4] == hidden_word[4]:
            output += "🟩"
        elif guess_word[4] in hidden_word:
            output += "🟨"
        elif guess_word[4] not in hidden_word:
            output += "⬛"
        else: print("Try again.)")
        
            

            
        
        

        # Result
        print(output)
        if output == "🟩🟩🟩🟩🟩":
            print("You win!")
            break

        print(f"You used {i+1} guesses")  

else: 
    print("Try again next time. The word is {0}".format(hidden_word))