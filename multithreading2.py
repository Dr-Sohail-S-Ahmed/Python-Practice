# PRACTICE EXERCISE
    # 1. Create any multithreaded code using for loop for creating multithreads
        # for i in range(10):
            # th = Thread(target=func_name, args=(i, ))
    # 2. Print total active threads in multithreaded code using threading.active_count()

import time                      # import time module for sleep function
import threading                 # import threading module to manage threads
from threading import Thread     # import Thread class directly for convenience

def sleepMe(i):                  # define a function that simulates thread sleeping
    print("Thread %i will sleep." % i)   # print message before sleeping
    time.sleep(5)                         # pause execution for 5 seconds
    print("Thread %i is awake" % i)       # print message after waking up

for i in range(10):              # loop from 0 to 9 (10 times)
    th = Thread(target=sleepMe, args=(i, ))   # create a thread to run sleepMe with argument i
    th.start()                              # start the thread (runs sleepMe in parallel)
    print("Current Threads: %i." % threading.active_count())   # show how many threads are active

"""
This program creates 10 threads, each calling the sleepMe function with a different number. Each thread prints
a message, sleeps for 5 seconds, then prints again when it wakes up. While threads are being started, the program
prints the current number of active threads.
"""