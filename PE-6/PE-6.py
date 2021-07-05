# using formula for the arithmetic series: Sn = n/2 (a1+an)
# where Sn is the sum, n is the length of the series, a1 is the first number, and "an" is the last

def squareOfSum(an):
    num = (an//2) * (1 + an)    
    return num**2

# using Gauss' formula for the sum of k^a from k = 1 to n.
# the formula for a = 2 being [n(n+1)(2n+1)] / 6, with n being the length of the series.
# because the lower bounds will always be 1, our n will always equal the an from the arithmetic series 

def sumOfSquares(an):
    num = (an * (an+1) * ((2*an) + 1)) // 6
    return num

def difference(an):     # so you don't have to change both
    return squareOfSum(an) - sumOfSquares(an)


print(difference(100)) # change to change upper bounds, lower bounds must always be 1

