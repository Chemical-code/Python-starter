import random
print("# random module")

# random(): return float of 0.0 <= x < 1.0
print("- random():", random.random())

# uniform(min, max) return float of designated range
print("- uniform(10, 20):", random.uniform(10, 20))

# randrange(): return int of designated range
# - randrange(max): return of 0 to max
# - radnrange(min, max): return of min to max
print("- randrange(10):", random.randrange(10))

# choice(list): choose element inside list
print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))

# shuffle(list): mix elements of list randomly
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

# sample(list, k=<number>): pick k of elements of list
print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))