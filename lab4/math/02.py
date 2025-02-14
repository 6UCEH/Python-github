import math

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2

print("Expected Output:", math.ceil(area) if area % 1 == 0 else area)
