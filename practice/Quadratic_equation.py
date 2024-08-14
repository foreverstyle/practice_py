# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 二次方程

import math

def quadratic_equation(a, b, c):
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The roots are real and different.")
        print("Root 1 = ", root1)
        print("Root 2 = ", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("The roots are real and equal.")
        print("Root 1 = Root 2 = ", root)
    else:
        realPart = -b / (2*a)
        imaginaryPart = math.sqrt(-discriminant) / (2*a)
        print("The roots are complex and different.")
        print("Root 1 = ", realPart, "+", imaginaryPart, "i")
        print("Root 2 = ", realPart, "-", imaginaryPart, "i")


if __name__ == '__main__':
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    quadratic_equation(a, b, c)