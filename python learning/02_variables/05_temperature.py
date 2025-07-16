#temperature conversion

#converting Celsius to Fahrenheit F = (9 / 5 * C) + 32
#converting Fahrenheit to Celsius C = (5 / 9) * (F - 32)
#converting Celsius to Kelvin K = C + 273.15

Celsius = int(input("Enter Celsius: "))
Fahrenheit = (9 / 5 * Celsius) + 32
print(Fahrenheit,"F")

Fahrenheit = int(input("Enter Fahrenheit: "))
Celsius = (5 / 9) * (Fahrenheit - 32)
print(Celsius,"C")

Celsius = int(input("Enter Celsius: "))
Kelvin = Celsius + 273.15
print(Kelvin,"K")