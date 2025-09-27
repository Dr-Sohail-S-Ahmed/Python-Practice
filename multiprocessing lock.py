import time
import multiprocessing

# WITHOUT MULTIPROCESSING LOCK (every time different value maybe printed)
def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value + 1

def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1

if __name__ == "__main__":
    balance = multiprocessing.Value('i',200)
    d = multiprocessing.Process(target=deposit,args=(balance,))
    w = multiprocessing.Process(target=withdraw,args=(balance,))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)    # Every time a different value maybe printed bcz both deposit & withdraw try to access balance at the same time


# WITH MULTIPROCESSING LOCK (every time same value is printed)
def deposit(balance, lock):                       # Function to deposit money safely using a lock
    for i in range(100):                          # Repeat 100 times
        time.sleep(0.01)                          # Small delay to simulate real-world processing
        lock.acquire()                            # Acquire lock so only one process can change balance
        balance.value = balance.value + 1         # Safely increase balance by 1
        lock.release()                            # Release lock for others to use

def withdraw(balance, lock):                      # Function to withdraw money safely using a lock
    for i in range(100):                          # Repeat 100 times
        time.sleep(0.01)                          # Small delay to simulate real-world processing
        lock.acquire()                            # Acquire lock so only one process can change balance
        balance.value = balance.value - 1         # Safely decrease balance by 1
        lock.release()                            # Release lock for others to use

if __name__ == '__main__':                        # Run this only when file is executed directly
    balance = multiprocessing.Value('i', 200)     # Create a shared integer value starting at 200
    lock = multiprocessing.Lock()                 # Create a lock to prevent race conditions
    d = multiprocessing.Process(target=deposit, args=(balance,lock))  # Create deposit process
    w = multiprocessing.Process(target=withdraw, args=(balance,lock)) # Create withdraw process
    d.start()                                     # Start deposit process
    w.start()                                     # Start withdraw process
    d.join()                                      # Wait for deposit to finish
    w.join()                                      # Wait for withdraw to finish
    print(balance.value)                          # Print final balance after both processes finish
    # lock.acquire() is put before the critical section of the code which may cause abnormal output if not regulated
    # lock.release() is put after it
"""
This program demonstrates how to safely update a shared balance between two processes (deposit and withdraw) using a 
multiprocessing lock. The lock ensures that only one process modifies the balance at a time, preventing race conditions 
and keeping the final result consistent.
"""