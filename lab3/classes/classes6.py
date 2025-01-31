is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))


numbers = range(1, 21)


prime_numbers = [num for num in numbers if is_prime(num)]


print("Простые числа:", prime_numbers)
