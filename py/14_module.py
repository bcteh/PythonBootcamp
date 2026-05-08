#use math_utils module
import math_utils
print(math_utils.add(10,5)) 
print(math_utils.sub(10,5))
print(math_utils.mul(10,5))
print(math_utils.div(10,5))


#use math_utils module
from math_utils import add, div, mul,sub
print(add(10,5))
print(sub(10,5))
print(mul(10,5))
print(div(10,5))

import os
import sys
import datetime
import random

now = datetime.datetime.now()
print("Current date and time:", now)    

random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

random_fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
random_fruit = random.choice(random_fruits)
print("Random fruit:", random_fruit)

print("Current working directory:", os.getcwd())
print("Python version:", sys.version)

