# (see also Adv Python in Programming.xlsx)

import multiprocessing     # import multiprocessing module to create processes

# USING UNSHARED/SEPARATE MEMORY SPACES
result = []                # a normal Python list (not shared between processes)

def calc_square(numbers):   # define a function to calculate squares (runs in child process)
    global result           # use global 'result' variable inside this function
    for n in numbers:       # loop through each number in the list
        result.append(n*n)  # append square of number to result list
    print("result inside process (with separate memory): " + str(result))  # print result inside child process + output: "result inside process: [4, 9, 25]"

if __name__ == "__main__":  # check if this script is being run directly (parent process)
    numbers = [2,3,5]       # define a list of numbers to process
    p = multiprocessing.Process(target=calc_square, args=(numbers,)) # create child process with target function and arguments

    p.start()               # start the child process
    p.join()                # wait until the child process finishes execution

    print("result outside process (with separate memory): " + str(result)) # print result in parent process + output: "result outside process: []"

"""
This program demonstrates how a global list behaves differently in multiprocessing.
The child process updates its own copy of the result list (printing squared numbers inside), but the parent process
still sees an empty result outside because memory is not shared between processes unless special objects like
multiprocessing.Array or Manager are used.
"""
    # The problem here is that both parent & child processes are taking up different memory spaces therefore different results
    # In order to resolve this issue, shared memory is used (see also Adv Python in Programming.xlsx)


# USING SHARED MEMORY WITH ARRAY & VALUE
def calc_square_av(numbers, resulta, v):   # Function to calculate squares in a child process
    v.value = 5.67                     # Update the shared value to 5.67
    for idx, n in enumerate(numbers):  # Loop through each number with its index + "enumerate" while looping thru sequence also keep track of index
        resulta[idx] = n*n              # Store square of number in shared array at same index

if __name__ == "__main__":             # Code to run only in the main (parent) process
    numbers = [2,3,5]                  # Input list of numbers
    resulta = multiprocessing.Array('i',3)  # Shared array of 3 integers, initialized with zeros
    v = multiprocessing.Value('d', 0.0)    # Shared double value, initialized to 0.0
    p_av = multiprocessing.Process(target=calc_square_av, args=(numbers, resulta, v))  # Create process to run calc_square

    p_av.start()                          # Start the process
    p_av.join()                           # Wait until the process finishes

    print(v.value)                     # Print the final shared value (updated inside process)

"""
This program demonstrates how to use multiprocessing with shared memory in Python.
- `multiprocessing.Array` is used to share an array of integers between processes.
- `multiprocessing.Value` is used to share a single floating-point value.
- The child process updates both the array and the shared value, and the parent process
  can read the updated results after the process finishes.
"""


# USING SHARED MEMORY WITH QUEUE
def calc_square_q(numbers, q):   # Function to calculate squares and put results in a queue
    for n in numbers:            # Loop through each number
        q.put(n*n)               # Put the square of number into the queue

if __name__ == "__main__":       # Run this block only if the file is executed directly
    numbers = [2,3,5]            # List of numbers to square
    q = multiprocessing.Queue()  # Create a multiprocessing queue for inter-process communication
    p_q = multiprocessing.Process(target=calc_square_q, args=(numbers,q))  # Create a process to run calc_square_q with arguments

    p_q.start()                  # Start the process
    p_q.join()                   # Wait until the process finishes

    while q.empty() is False:    # Keep looping while the queue has values
        print(q.get())           # Get and print each value from the queue

# Difference btw multiprocessing.Queue() & queue.Queue() (see Adv Python in Programming.xlsx)

"""
This program uses Python's multiprocessing to calculate squares of numbers in a separate process. The results are sent 
back to the main process using a queue, which ensures safe data sharing between processes.
"""