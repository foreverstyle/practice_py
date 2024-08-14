# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 快速排序算法实现

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]      #挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
    

if __name__ == '__main__':
    arr = [3, 7, 2, 5, 1, 4, 9, 6, 8]
    print(quick_sort(arr))

