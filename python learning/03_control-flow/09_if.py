#positive number check
number = int(input("Enter the number: "))
if number > 0:
    print("Positive Number")

print(" ")

#check for discount eligibility
amount = int(input("Enter the amount: "))
if amount > 10000:
    print("Eligible for discount")

print(" ")

#Name length checker
name = str(input("Enter Your Name: "))
if len(name) > 5:
    print("That's a long name!")

print(" ")

#Check for Keyword
sentence = str(input("Write a sentence: "))
if "python" in sentence.lower():
    print("Python lover!")

print(" ")

#Check if Number is Divisible by 7
number = int(input("Enter the luck number: "))
if number % 7 == 0:
    print("Lucky number!")