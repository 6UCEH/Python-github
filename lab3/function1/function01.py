def grams_to_ounces(grams):
    return grams / 28.3495231


grams = 100
ounces = grams_to_ounces(grams)
print(grams, "граммов =", round(ounces, 2), "унции")
