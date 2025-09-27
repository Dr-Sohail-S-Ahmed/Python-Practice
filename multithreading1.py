import time                   # import time module to measure execution time and add delays
import threading              # import threading module to create and run threads

def calc_square(numbers):     # define function to calculate squares of a list
    print("calculate square numbers")   # print message when square calculation starts
    for n in numbers:                     # loop through each number in the list
        time.sleep(1)                     # pause for 1 second to simulate delay
        print('square:', n*n)             # print the square of the current number

def calc_cube(numbers):       # define function to calculate cubes of a list
    print("calculate cube of numbers")   # print message when cube calculation starts
    for n in numbers:                     # loop through each number in the list
        time.sleep(1)                     # pause for 1 second to simulate delay
        print('cube:', n*n*n)             # print the cube of the current number

arr = [2,3,8,9]               # define a list of numbers to process

t = time.time()               # record the start time

t1 = threading.Thread(target=calc_square, args=(arr,))  # create first thread to run square function
t2 = threading.Thread(target=calc_cube, args=(arr,))    # create second thread to run cube function
    # (arr,) refers to 1-element tuple + if ',' not placed, Python will treat it as a list

t1.start()                    # start the first thread
t2.start()                    # start the second thread

t1.join()                     # wait until the first thread finishes
t2.join()                     # wait until the second thread finishes

print("done in : ", time.time()-t)   # print total time taken to complete both threads
print("Hah... I am done with all my work now!")   # print final completion message
