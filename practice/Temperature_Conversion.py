# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 华氏温度和摄氏温度之间的转换

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

if __name__ == '__main__':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit: ", fahrenheit)

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius: ", celsius)