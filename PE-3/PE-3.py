# using the fundamental theorem of arithmatic
from math import *

num = 600851475143

def getPrimeFactor(num):
    if num == 2: return 2
    for x in range(2, ceil(sqrt(num)) + 1):
        if num % x == 0:
            return x
    return num

while getPrimeFactor(num) != num:
    num //= getPrimeFactor(num)
    
print(num)
