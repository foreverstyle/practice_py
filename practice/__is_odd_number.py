# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(10))