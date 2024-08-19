# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 17
# Description: 莫烦Python

# 为什么有生成器
# 你要了解生成器，首先你必须知道循环这回事。因为循环是一个用简短语句表示的重复执行过程。 那么生成器就是为循环设计的。

# 那么是因为循环遇到了什么问题，才会有人想要要用生成器呢？ 在循环的时候，我们的目的是为了每次循环拿到一些特定数据，然后为这些数据做处理。但是无可避免的会在内存中记录这些数值， 当需要记录的数值很多的时候，我们的内存可能就吃不消了。而生成器，即现做现吃的意思，你跟着我的教程，往下走， 就会越来越深刻体会到 Python 是怎么现做现吃了~

# 所以生成器这个名字也比较应景，我只在需要这个数据的时候生成它，生成完了我就不用了，也不需要记录。这种时候将会节约我很多内存的需求。

items = []  # 假设这里在记录一个很大的列表
for item in range(5):
    if item % 2 == 0:
        items.append(item)

for i in items:
    print(i)

# 这种需要先保存一个 items 的列表，但当你做机器学习或者数据处理的时候， 如果这个 items 列表的数据量很大，就会非常占内存。

def need_return():
    tmp = 2
    for item in range(300):
        if item == tmp:
            tmp *= item
            yield item

for i in need_return():
    print(i)
