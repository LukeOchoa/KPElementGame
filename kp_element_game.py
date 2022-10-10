import random


# Instead of creating a bunch of if-statements to handle every single case
# Use a more programatic approach to solve it by simply saying
# -> If the element is dominant, I win
# -> Else: I lose

def compare_choices(player, computer, list_of_elements):
    result = ""

    if player == computer:
        result = "its a draw...!"
    else:
        # If the index at list_of_elements[player](which is the losing element)
        # is the same as the one the computer chose, then you win. Otherwise you lose...
        if list_of_elements[player] == computer:
            result = "you win...!"
        else:
            result = "you lose...!"

    return "\nPlayer: |{}|\nComputer: |{}|\n".format(player, computer) + result + "\n"


choices = ["earth", "fire", "water", "air"]
# In this dictionary is a key/value pair of elements
# The key is the dominant element and the value is the losing element
# "Stronger Element": "Weaker Element"...
dict_of_elements = {
    "earth": "fire",
    "fire": "air",
    "water":  "earth",
    "air": "water"
}

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("earth, fire, water, or air? :").lower()

    print(compare_choices(player, computer, dict_of_elements))

    if input("Play again? (yay/nay): ").lower() != "yay":
        break

print("Sayonara!")
