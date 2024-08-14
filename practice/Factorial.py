# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 

def factorial(n):
    # if n == 0:   # base case
    #     return 1
    # else:
    #     return n * factorial(n-1)   # recursive case
    result_factorial = 1
    for i in range(1, n+1):
        result_factorial *= i
    return result_factorial

if __name__ == '__main__':
    n=int(input("Enter a number: "))
    print("Factorial of", n, "is", factorial(n))