num1, num2, fibSum= 2, 1, 2   # number 1 away, number 2 away, Fibonacci sum of evens after 1 and 2
while num2 + num1 < 4000000:
    tempSum = num1 + num2
    if tempSum % 2 == 0:
        fibSum+= tempSum
    num2 = num1
    num1 = tempSum

print(fibSum) # returns 4613732








    


