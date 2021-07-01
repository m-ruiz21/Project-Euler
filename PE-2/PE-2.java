class PE2 {
    public static void main(String[] args) {
        System.out.println(getFibSum());
    } 
    
    static int getFibSum() {
        int fibSum = 2; // sum of even Fibonacci numbers up to 2 
        int num2= 1;  // Fibonacci number 2 away
        int num1 = 2;  // Fibonacci number 1 away
        while (num2 + num1 <= 4000000) {
            int tempSum = num1 + num2;
            if (tempSum % 2 == 0)
                fibSum += tempSum;
            num2= num1;
            num1 = tempSum;
        }
        return fibSum;  // returns 4613732
    }
}

