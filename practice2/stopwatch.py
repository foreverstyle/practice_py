# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 实现秒表功能
# 功能：按下回车键开始计时，按下Ctrl + C 停止计时键停止计时，显示计时时间，按下回车键重新开始计时。

import time

class Stopwatch:    
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("Stopwatch started...")

    def stop(self):
        if self.running:
            self.stop_time = time.time()
            self.running = False
            print("Stopwatch stopped. Time elapsed:", self.get_time())

    def reset(self):
        self.start_time = 0
        self.stop_time = 0
        self.running = False
        print("Stopwatch reset.")

    def get_time(self):
        if self.running:
            return time.time() - self.start_time
        else:
            return self.stop_time - self.start_time

if __name__ == '__main__':
    stopwatch = Stopwatch()
    print("Press Enter to start the stopwatch, Ctrl + C to stop, and Enter to restart.")
    
    while True:
        try:
            input()
            if stopwatch.running:
                stopwatch.reset()
                stopwatch.start()
            else:
                stopwatch.start()
        except KeyboardInterrupt:
            stopwatch.stop()
            print("Press Enter to restart the stopwatch.")
