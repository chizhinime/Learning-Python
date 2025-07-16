#Grade Checker
score = int(input("Enter score: "))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")

print(" ")

#Day of the week Responder
number = int(input("the week: "))
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thurday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Invalid input")

print(" ")

#Traffic Light System
color = str(input("Enter Color: "))
if color == 'red':
    print("Stop")
elif color == 'yellow':
    print("Ready")
elif color == 'green':
    print("Go")
else:
    print("Invalid Color")

print(" ")

#Number Sign Checker
number = int(input("Enter the number: "))
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
elif number < 0:
    print("Negative")
else:
    print("Invalid")

print(" ")

#Movie Ticket Pricing
age = int(input("Enter your age: "))
if age <= 5:
    print("Free")
elif age <= 12:
    print("Child ticket")
elif age <= 59:
    print("Regular ticket")
elif age >= 60:
    print("Senior ticket")
else:
    print("Invalid")