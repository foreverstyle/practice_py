# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 五人分鱼问题

fish = 100
while True:
    total_fish = fish
    count = 0;
    for i in range(5):
        if(total_fish-1)%5==0:
            total_fish=(total_fish-1)//5*4
            count+=1
        else:
            count=0
            break
    if(count == 5):
        break
    fish +=1

print("总共有",fish,"只鱼")