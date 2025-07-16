#1. Basic Function with No Parameters

def greet():
    print("Hello, world!")

greet()

print(" ")
#2. Function with One Parameter

def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Chizhinime")

print(" ")
#3. Return Sum of Two Numbers

def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8

print(" ")
#4. Even or Odd Checker

def is_even(number):
    return number % 2 == 0

print(is_even(4))  # Output: True

print(" ")
#5. Square of a Number

def square(n):
    return n ** 2

print(square(6))  # Output: 36

print(" ")
#6. Get Maximum of Three Numbers

def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(10, 5, 8))  # Output: 10

print(" ")
#7. Check if String is a Palindrome

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("madam"))  # Output: True

print(" ")
#8. Calculate Factorial

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120

print(" ")
#9. Count Vowels in a String

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # Output: 3

print(" ")
#10. Generate a List of Even Numbers

def get_even_numbers(limit):
    return [x for x in range(2, limit + 1) if x % 2 == 0]

print(get_even_numbers(10))  # Output: [2, 4, 6, 8, 10]

print(" ")
#11. Check Prime Number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))  # Output: True

print(" ")
#12. Fibonacci Sequence

def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]

print(" ")
#13. Find Duplicates in a List

def find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))  # Output: [2, 1]

print(" ")
#14. Simple Calculator

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

print(calculator(10, 5, "*"))  # Output: 50

print(" ")
#15. Function with Default Parameter

def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()         # Output: Hello, Guest!
greet_user("Grace")  # Output: Hello, Grace!