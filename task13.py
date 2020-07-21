from timeit import default_timer as timer
from datetime import timedelta
import time


def timee(function_to_be_timed):
    def inside_time(*args, **kwds):
        start = timer()
        function_to_be_timed(*args, **kwds)
        end = timer()
        delta = timedelta(seconds=end - start)
        print(f"{delta.total_seconds()} seconds")

    return inside_time


@timee
def factorial(num):
    # This will return the factorial of a number
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i

    print(f"The Factorial of {num} is {fact}")
    return fact


@timee
def my_sum(number1, number2):
    print(f"The sum of {number1} and {number2} is {number1+number2}")
    return number1 + number2


@timee
def my_product(number1, number2):
    print(f"The product of {number1} and {number2} is {number1*number2}")
    return number1 * number2


# Testing Decorators
factorial(7)
print()
my_sum(289, 111)
print()
my_product(289, 111)
