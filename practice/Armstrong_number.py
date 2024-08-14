# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 

def is_armstrong(num):
    num_str = str(num)
    length = len(num_str)
    sum_of_powers = sum([int(digit) ** length for digit in num_str])
    return sum_of_powers == num


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")