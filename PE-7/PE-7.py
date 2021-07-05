import math

n = 10001
lim = 2 * (n + 1)
lowerLim = 2
primes = []
while len(primes)<n:
    nxtPrimes = [y for y in range(lowerLim, lim) if all(map(lambda x: y%x != 0, range(2, math.floor(math.sqrt(y) + 1))))]
    primes += nxtPrimes
    lowerLim = lim
    lim += 2 * (n + 1)

print(primes[n-1])
