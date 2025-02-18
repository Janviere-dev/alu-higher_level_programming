#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number  >=10:
     last digit = number % 10
 else:
     lsat digit = (((number * -1) % 10) * -1)
     string = "last digit of"
     if last digit >5:
         print(f"{string} {number} is {last digit} and is greater than 5")
     elif last digiy ==0:
         print(f"{string} {number} is {last digit} and is 0")
     else:
         print(f"{string} {number} is {last digit} and is less than 6 and not 0")
