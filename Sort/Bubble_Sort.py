# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array is:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array is:", sorted_arr)