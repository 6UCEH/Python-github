def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes


numbers = [10, 15, 17, 19, 20]  
prime_numbers = filter_prime(numbers)
print("Простые числа:", prime_numbers)
