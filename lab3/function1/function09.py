def sphere_volume(radius):
    return (4 / 3) * 3.14159 * (radius ** 3)


r = float(input("Введите радиус сферы: "))
volume = sphere_volume(r)
print("Объем сферы:", round(volume, 2))
