# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 




def is_leap_year(year):
    if year % 4 == 0 and (year % 100!= 0 or year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
    
if(__name__ == '__main__'):
    while True:
        try:
            year = int(input("Enter a year: "))
            is_leap_year(year)
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

