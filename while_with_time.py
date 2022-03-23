# Import time library
import time

# Declare variables
number = 0

# Repeat 5 seconds
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

# Print
print("This repeats {} times during 5 seconds.".format(number))