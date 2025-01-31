from function09 import sphere_volume
from function06 import reverse_words
from function01 import grams_to_ounces

#  reverse_words
sentence = input("Введите предложение: ")
result = reverse_words(sentence)
print("Результат:", result)

#  grams_to_ounces
grams = 100
ounces = grams_to_ounces(grams)
print(grams, "граммов =", round(ounces, 2), "унции")

#  функции sphere_volume
radius = 3
print("Объем сферы с радиусом", radius, "=", round(sphere_volume(radius), 2))
