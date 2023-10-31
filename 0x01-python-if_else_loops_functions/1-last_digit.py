#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = number % 10
if number < 0:
    number *= -1
    result = (number % 10) * -1
    number *= -1
if result > 5:
    print(f"Last digit of {number:d} is {result:d} and is greater than {5:d}")
elif result == 0:
    print(f"Last digit of {number:d} is {result:d} and {0:d}")
else:
    print(f"Last digit of {number:d} is {result:d} and is less" +
          " than 6 and not 0")
