#Generate integers between 1,5
import random
from random import shuffle

print (random.randint(0, 5))

#a random number between 0 and 100
print(type(random.random() * 100))

#a random element from a list
myList = [True, 56, "Book", "R", 56.89, False, 0.56]
print(random.choice(myList))

#shuffles the elements in list in place,
x = [[i] for i in range(10)]
shuffle(x)
print(x)

#Generate a randomly selected element from range(start, stop, step)
print (random.randrange(0, 100, 4))


import random
print (random.randint(0, 5))