def grams_to_ounces(grams):
    return grams / 28.3495231


grams = float(input("\nHow many gram?\n"))
ounces = grams_to_ounces(grams)
print(grams, "граммов =", round(ounces, 2), "унции")
