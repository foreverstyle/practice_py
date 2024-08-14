# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 随机生成一个数字

import random
# 随机生成的0-1之间的数字
random_num = random.random()

# 随机生成的1-100之间的数字
random_num1 = random.randint(1, 100)

# 序列中随机选择一个元素：
seq = [1, 2, 3, 4, 5]
random_num2 = random.choice(seq)

print('随机生成的0-1之间的数字为', random_num)
print('-----------------------------------')
print('随机生成的1-100之间的数字为', random_num1)
print('-----------------------------------')
print('序列中随机选择的元素为', random_num2)
print('-----------------------------------')