import time
import math

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)  
    result = math.sqrt(number)  
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")


num = int(input())
delay = int(input())

delayed_square_root(num, delay)
