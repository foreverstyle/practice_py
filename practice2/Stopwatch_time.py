# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 

import time
import datetime

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

    def display_elapsed_time(self):
        try:
            while self.running:
                elapsed_time = self.get_time()
                print(f"\rElapsed Time: {elapsed_time:.2f} seconds", end="")
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
            print("\nStopwatch stopped. Time elapsed:", self.get_time())

if __name__ == '__main__':
    stopwatch = Stopwatch()
    print("Press Enter to start the stopwatch, Ctrl + C to stop, and Enter to restart.")
    while True:
        try:
            input()
            if stopwatch.running:
                stopwatch.stop()
            else:
                stopwatch.start()
                stopwatch.display_elapsed_time()
        except KeyboardInterrupt:
            print("\nProgram stopped.")
            break
