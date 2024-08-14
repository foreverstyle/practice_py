# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 计算圆的面积

import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    radius = float(input("请输入圆的半径："))
    area = calculate_area_circle(radius)
    print("圆的面积为：", area)