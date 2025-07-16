#Create and Print a List

foods = ["Pizza", "Rice", "Chicken", "Beans", "Ice Cream"]
print(foods)

print(" ")
#Access List Items

fruits = ["Apple", "Banana", "Cherry"]
print("First:", fruits[0])
print("Last:", fruits[-1])

print(" ")
#Change a Value in a List

colors = ["Red", "Green", "Blue"]
colors[1] = "Black"
print(colors)

print(" ")
#Append an Item

cars = ["Toyota", "BMW", "Honda"]
cars.append("Tesla")
print(cars)

print(" ")
#Check if Item Exists

animals = ["Lion", "Tiger", "Zebra", "Elephant"]
animal = input("Enter an animal: ")

if animal in animals:
    print(f"{animal} is in the list.")
else:
    print(f"{animal} is not in the list.")

print(" ")
#Loop Through a List

languages = ["Python", "Java", "C++"]
for lang in languages:
    print(lang)

print(" ")
#List Length

numbers = [10, 20, 30, 40, 50]
print("Length:", len(numbers))

print(" ")
#Remove an Item

devices = ["Phone", "Tablet", "Laptop", "Smartwatch"]
devices.remove("Tablet")
print(devices)

print(" ")
#Sort a List

nums = [9, 3, 7, 1, 5]
nums.sort()
print("Sorted list:", nums)

print(" ")
#List Slicing

items = ["A", "B", "C", "D", "E", "F"]
print("First 3 items:", items[:3])

print(" ")
#Sum All Numbers in a List

numbers = [5, 10, 15, 20]
print("Sum:", sum(numbers))

print(" ")
#Find the Largest Number

values = [12, 43, 7, 89, 3]
print("Max value:", max(values))

print(" ")
#Remove Duplicates from a List

dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(dup_list))
print("Unique values:", unique_list)

print(" ")

dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in dup_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

print(" ")
#List Comprehension: Squares

squares = [x**2 for x in range(1, 11)]
print(squares)

print(" ")
#Nested List Access

data = [[1, 2], [3, 4], [5, 6]]
print(data[1][1])  # Output: 4
