# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 二分查找算法


def binary_search(arr, target):
    """
    二分查找算法
    :param arr: 待查找的数组
    :param target: 要查找的元素
    :return: 元素在数组中的索引，如果不存在，则返回-1
    """
    left = 0
    right = len(arr) - 1
    find_count = -1
    while left <= right:
        find_count += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"查找成功，查找次数为 {find_count}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    index = binary_search(arr, target)
    if index == -1:
        print(f"{target} 不在数组中")
    else:
        print(f"{target} 在数组中，索引为 {index}")