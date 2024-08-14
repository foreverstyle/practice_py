# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    n = int(input("Enter the number of terms: "))
    for i in range(n):
        print(fibonacci(i))