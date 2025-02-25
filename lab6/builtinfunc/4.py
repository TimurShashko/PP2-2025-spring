import time
import math

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000.0)
    return math.sqrt(number)

if __name__ == "__main__":
    n = float(input("Enter a number to take square root of: "))
    ms = int(input("Enter milliseconds to wait: "))
    result = delayed_sqrt(n, ms)
    print(f"Square root of {n} after {ms} miliseconds is {result}")
