# (For details, see Adv Python in Programming.xlsx)

# WITH MULTIPROCESSING POOL
from multiprocessing import Pool   # Import Pool to run tasks in parallel using multiple processes
import time                        # Import time module to measure execution time

def fmp(n):                        # Define a function that performs some heavy calculation
    sum = 0                        # Initialize sum variable
    for x in range(1000):          # Loop through numbers from 0 to 999
        sum += x * x               # Add square of each number to sum
    return sum                     # Return the computed sum

if __name__ == "__main__":         # Run this block only if file is executed directly
    t1 = time.time()               # Record start time for multiprocessing
    p = Pool()                     # Create a pool of worker processes
                                   # Empty Pool() creates as many worker processes (by default) as there are CPU cores
                                     # ...but processes can also be defined as Pool(processes=n)
    result = p.map(fmp, range(100000))  # Distribute work of calling fmp across multiple processes
                                       # for a smaller range/array/task the output might not seem significant
    p.close()                      # Stop the pool from accepting new tasks
    p.join()                       # Wait for all worker processes to finish
    print("Pool took: ", time.time() - t1)  # Print total time taken by multiprocessing
    # This is multiprocessing

    t2 = time.time()               # Record start time for serial processing
    result = []                    # Create an empty list to store results
    for x in range(100000):         # Loop through numbers from 0 to 9999
        result.append(fmp(x))      # Call fmp one by one and store the result
    print("Serial processing took: ", time.time() - t2)  # Print total time taken by serial execution
    # This is without multiprocessing

"""
This program compares two approaches for running the same task:
1. Using multiprocessing.Pool to split work across multiple CPU cores (parallel).
2. Using a normal loop to run the same task one by one (serial).
It then prints the time taken by each method so we can see the performance difference.
"""