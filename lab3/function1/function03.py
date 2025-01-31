def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits


heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print("Курицы:", chickens, "Кролики:", rabbits)
