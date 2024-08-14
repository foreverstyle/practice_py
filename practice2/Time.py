# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 实时显示时间

import time
import datetime

def display_time():
    try:
        while True:
            # 获取当前时间
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # 在同一行输出时间，\r 使得光标返回到行首
            print(f"\rCurrent Time: {current_time}", end="")
            
            # 休眠一秒钟
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram stopped.")

if __name__ == '__main__':
    display_time()
