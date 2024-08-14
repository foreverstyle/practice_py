# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 计算三角形面积,已知三条边的长度

def calculate_area_triangle(a, b, c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area


if __name__ == '__main__':
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    area=calculate_area_triangle(a,b,c)
    print("The area of the triangle is:", area)