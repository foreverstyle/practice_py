# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 17
# Description: 莫烦python



done = False
if done:
    a = 1
else:
    a = 2
print(a)

done = False
a = 1 if done else 2
print(a)



l = [i*2 for i in range(10) if i%2==0]
print(l)