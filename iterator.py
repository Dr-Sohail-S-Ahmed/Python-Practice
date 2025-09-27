# ITERATING THRU A LIST
a = ["abc", "cde", "fgh", "ijk"]

for i in a:     # To iterate thru a list
    print(i)

print(dir(a))   # "dir()" doesn't care about the variable name but it only gives methods of what's stored in it which in this case is a list

# ITERATING USING ITER METHOD
it = ["What", "a", "good", "boy", "am", "I"]
itr = iter(it)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))    # "print(next(itr))" again would throw an exception StopIteration

"""
Difference between "next()" & "__next__()":
a) "__next__()" is the (low-level method) hidden engine inside iterator which isn't usually called directly + it raises
StopIteration exception when things run out + ANALOGY: Gear inside a clock
b) "next()" is the (user-friendly function) official button to advance the iterator + it calls object's "__next__"
behind the scenes + it gives a safer option to pass a default value if the iterator is finished instead of crashing +
ANALOGY: Clock face

RULE OF THUMB: Use "next()" when using an iterator, implement "__next__()" only when building an iterator
"""

# ITERATORS - EXAMPLE 1 (LIST)
for element in [1, 2, 3]:
    print(element)

# ITERATORS - EXAMPLE 2 (TUPLE)
for element in (1, 2, 3):
    print(element)

# ITERATORS - EXAMPLE 3 (DICTIONARY)
for key in {'one': 1, 'two': 2}:
    print(key)

# ITERATORS - EXAMPLE 4 (STRING)
for char in "123":
    print(char)

# ITERATORS - EXAMPLE 5 (FILE)
for line in open("C:\\Users\\Admin\\PycharmProjects\\PYTHON PRACTICE\\example.txt"):
    print(line, end = "")

# REVERSE ITERATION METHOD
rev = ["plum", "a", "out", "pulled"]
itr = reversed(rev)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

# PRACTICE EXERCISE 1
class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","CNN","FOX","ABC","PTV","ZTV","ESPN"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

# PRACTICE EXERCISE 2
    # Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
    # The iterator should stop when it reaches a limit defined in the constructor.

class Fibonacci:                              # Define a class for Fibonacci iterator
    def __init__(self, limit):                # Constructor takes a limit (number of terms)
        # default constructor
        self.previous = 0                     # Start first number of Fibonacci
        self.current = 1                      # Start second number of Fibonacci
        self.n = 1                            # Counter to track how many terms generated
        self.limit = limit                    # Store the maximum number of terms

    def __iter__(self):                       # Make the class iterable
        return self                           # Return the iterator object itself

    def __next__(self):                       # Define logic for the next Fibonacci number
        if self.n < self.limit:               # Check if we are still below the term limit
            result = self.previous + self.current  # Calculate next Fibonacci number
            self.previous = self.current           # Update previous number
            self.current = result                  # Update current number
            self.n += 1                            # Increment the counter
            return result                          # Return the next Fibonacci number
        else:
            raise StopIteration               # Stop when limit is reached


# init the fib_iterator
fib_iterator = iter(Fibonacci(5))             # Create an iterator for 5 Fibonacci terms
while True:                                   # Keep looping until StopIteration
    # print the value of next fibonacci up to nth fibonacci
    try:
        print(next(fib_iterator))             # Print next Fibonacci number
    except StopIteration:                     # Break when iteration ends
        break                                 # Exit the loop

"""
This code defines a custom Fibonacci iterator that generates Fibonacci numbers 
up to a given number of terms (limit). It uses __iter__() and __next__() methods 
to produce numbers one by one. In the example, Fibonacci numbers up to the 5th 
term are printed, and the iteration stops automatically when the limit is reached.
"""
