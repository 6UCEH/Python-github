import math

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", math.ceil(area) if area % 1 == 0 else area)
