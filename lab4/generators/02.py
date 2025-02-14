def even_generator(n):
    for i in range(0, n + 1, 2):  
        yield i

n = int(input("Enter a number: "))

print(*even_generator(n), sep=", ")

# OR
#print(",".join(map(str, even_generator(n))))
