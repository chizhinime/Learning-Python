#01 rectangle Area = Lenght * Width

Lenght = int(input("Enter Lenght: "))
Width = int(input("Enter Width: "))
Area_of_a_rectangle = Lenght * Width
print("Area of a Rectangle is: ",Area_of_a_rectangle)
print(" ")

#02 Triangle Area = 1/2 * Base * Height

Base = int(input("Enter Base: "))
Height = int(input("Enter Height: "))
Area_of_a_triangle = 1/2 * Base * Height
print("Area of a triangle is:", Area_of_a_triangle)
print(" ")

#03 Circle Area = pi * r ** 2 , Circumference = 2 * pi * r (pi = 3.14)

pi = 3.14
Radius = int(input("Enter the Radius: "))
Area_of_a_circle = pi * Radius ** 2
print("Area of a Circle is:", Area_of_a_circle)
print(" ")

Radius = int(input("Enter the Radius: "))
Circumference = 2 * pi * Radius
print("Circumference of a cirle is:", Circumference)
print(" ")

#04 Cylinder Volume = pi * r ** 2 * h

pi = 3.14
Radius = int(input("Enter the Radius: "))
Height = int(input("Enter the Height: "))
Volume_of_a_cylinder = pi * Radius ** 2 * Height
print("Volume of a Cylinder is:", Volume_of_a_cylinder)
print(" ")

#05 Sphere Volume = 43 * pi * r ** 2

pi = 3.14
Radius = int(input("Enter the Radius: "))
Volume_of_a_sphere = 43 * pi * Radius ** 2
print("Volume of a Sphere is:", Volume_of_a_sphere)
print(" ")

#06 Area of Parallelogram = Base * Height

Base = int(input("Enter the Base: "))
Height = int(input("Enter the Height: "))
Area_of_a_parallelogram = Base * Height
print("Area of a Parallelogram is:", Area_of_a_parallelogram)
print(" ")

#07 Pythagorean Theorem a ** 2 + b ** 2 == c ** 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = (a ** 2 + b ** 2) / 2
print("c:", c)
print(" ")

#08 Slope Formula m = (y2 - y1) / (x2 - x1)  m represent the slope

x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
m = (y2 - y1) / (x2 - x1)
print("Slope is:", m)
print(" ")

#09 distance formula two dimensions (2D) d = [(x2 - x1) ** 2 + (y2 - y1) ** 2] ** 2
# three dimensions (3D) d =[(x2 -x1) ** 2 + (y2 -y1) ** 2 + (z2 - z1) ** 2] ** 2

#Two Dimension (2D)
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 2
print("The 2D is:", d)
print(" ")

#Three Dimension (3D)
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
z1 = int(input("Enter z1: "))
z2 = int(input("Enter z2: "))
d = ((x2 -x1) ** 2 + (y2 -y1) ** 2 + (z2 - z1) ** 2) ** 2
print("The 3D is:", d)
print(" ")

#10 Midpoint formula  Midpoint = ( (x1 + x2) / 2, (y1 + y2) / 2)

x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
Midpoint = ( (x1 + x2) / 2, (y1 + y2) / 2)
print("Midpoint is:", Midpoint)
print(" ")