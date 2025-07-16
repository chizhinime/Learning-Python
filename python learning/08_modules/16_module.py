#1. Use the math Module

import math

# Square root
print("Square root of 16 is:", math.sqrt(16))

print(" ")
# Area of a circle (r = 5)
radius = 5
area = math.pi * radius ** 2
print("Area of circle:", area)

print(" ")
#2. Use the random Module

import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("Correct!")
else:
    print(f"Wrong! The number was {number}")

print(" ")
#3. Use the datetime Module

from datetime import datetime

now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

print(" ")
#4. Use the os Module

import os

print("Current Directory:", os.getcwd())
print("Files and Folders:")
print(os.listdir())

print(" ")
#5. Use the time Module

import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up!")
