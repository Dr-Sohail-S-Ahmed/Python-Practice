# (For details, see Adv Python in Programming.xlsx)

# WITHOUT MULTIPROCESSING POOL
def f(n):
    return n*n*n

if __name__ == "__main__":
    array = [2,3,4,5,6,7,8,9]

    result = []
    for n in array:
        result.append(f(n))

    print(result)