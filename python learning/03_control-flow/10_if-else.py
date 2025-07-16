#Even or Odd
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

print(" ")

#Password Check
password = str(input("Enter password: "))
if password == "python":
    print("Access granted")
else:
    print("Wrong password")

print(" ")

#Temperature Checker
temp = int(input("Enter the temperature: "))
if temp > 30:
    print("It's hot")
else:
    print("It's normal")

print(" ")

#Age Verification
age = int(input("Enter your age: "))
if age > 18:
    print("Adult")
else:
    print("Minor")

print(" ")

#Check for Empty Input
username = str(input("Enter the input: "))
if username != "":
    print("Welcome", username)
else:
    print("Please enter a name")