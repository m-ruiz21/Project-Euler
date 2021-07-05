def isPalindrome(product):  # using definition of palindrome number
    productLen = len(product) -1
    for x in range(productLen//2 + 1):
        if product[x] != product[productLen - x]:
            return False     
    return True

def main():
    palindrome = max(num1 * num2 for num1 in range(500,1000) for num2 in range(500,1000) if isPalindrome(str(num1*num2)))
    return palindrome
    

print(main())
