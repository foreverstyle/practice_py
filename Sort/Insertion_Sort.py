# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 插入排序

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    arr = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(arr))