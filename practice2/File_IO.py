# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description:文件I/O操作 

# 打开文件
with open('test.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('This is a test file.\n')

# 读取文件
with open('test.txt', 'r') as f:
    print(f.read())