#Section 1: for Loop Solutions
#Print Numbers 1 to 10

for i in range(1, 11):
    print(i)

print(" ")
#Print Even Numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print(" ")
#Calculate the Sum of First 100 Numbers

total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

print(" ")
#Print Multiplication Table of 5

for i in range(1, 13):
    print(f"5 x {i} = {5 * i}")

print(" ")
#Reverse Countdown (10 to 1)

for i in range(10, 0, -1):
    print(i)

print(" ")
#Section 2: while Loop Solutions
#Countdown Timer (5 to 1)

count = 5
while count > 0:
    print(count)
    count -= 1

print(" ")
#Keep Asking Until Correct Answer

answer = 0
while answer != 4:
    answer = int(input("What is 2 + 2? "))
print("Correct!")

print(" ")
#Password Input with 3 Attempts

correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password")
        attempts += 1

if attempts == 3:
    print("Access denied")

print(" ")
#Sum of Numbers Until User Enters 0

total = 0
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter another number (0 to stop): "))

print("Total sum is:", total)

print(" ")
# Print All Odd Numbers Under 50

i = 1
while i < 50:
    if i % 2 != 0:
        print(i)
    i += 1

print(" ")
#Section 3: Nested Loop Solutions
#print a 5x5 Grid of Stars

for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

print(" ")
#Multiplication Table (1–5)

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

print(" ")
#Number Pyramid

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print(" ")
#Right-Angle Triangle of Stars

for i in range(1, 5):
    print("*" * i)

print(" ")
#List All Pairs (1–3)

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()