# Import random numbers
import random
# Make simple alphabet list
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# Open file in write mode
with open("info.txt", "w") as file:
    for i in range(1000):
        # Form random variables
        name = random.choice(alphabet) + random.choice(alphabet)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # Write text
        file.write("{}, {}, {}\n".format(name, weight, height))
