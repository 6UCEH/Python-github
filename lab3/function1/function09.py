def sphere_volume(radius):
    return (4 / 3) * 3.14159 * (radius ** 3)


r = float(input("\nВведите радиус сферы:\n"))
volume = sphere_volume(r)
print("\nОбъем сферы:\n", round(volume, 2))
