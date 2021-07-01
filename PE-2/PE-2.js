var num1 = 2, num2 = 1, fibSum = 2;
while (num1 + num2 < 4000000) {
    var tempSum = num1 + num2;
    if (tempSum % 2 == 0) {
        fibsum += tempSum;
    }
    num2 = num1
    num1 = tempSum
}
console.log(fibSum)

