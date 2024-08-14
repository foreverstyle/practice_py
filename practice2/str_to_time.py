# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 将字符串的时间转换为时间戳,同时转化为其他格式的时间

import time

def str_to_time(str_time):
    """
    将字符串的时间转换为时间戳
    :param str_time: 字符串的时间
    :return: 时间戳
    """
    time_array = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    # print(time_array)
    
    # 转换为其他格式的时间
    # other_format_time = time.strftime("%Y/%m/%d %H:%M:%S", time_array)
    # print(other_format_time)

    # 转换为时间戳
    time_stamp = int(time.mktime(time_array))
    return time_stamp

if __name__ == '__main__':    
    str_time = "2021-01-01 12:00:00"
    time_stamp = str_to_time(str_time)
    print(time_stamp)