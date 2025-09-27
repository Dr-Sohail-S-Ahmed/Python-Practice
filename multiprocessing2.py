# METHOD 2

import multiprocessing

square_result = []

def calc_square(numbers):
    global square_result    # (see Adv Python in Programming.xlsx) + Using "global" keyword tells Python that this "square_result" is...
                            # ...referring to the one defined at module (file) top level (i.e. it isn't a new local one defined here)
    for n in numbers:
        print("square " + str(n*n))
        square_result.append(n*n)
    print("within a process: result " + str(square_result))     # Appended result would only show if print is called from...
                                                                # ..inside function otherwise it'd return blank list

if __name__ == "__main__":
    arr = [2,3,8,9]
    p = multiprocessing.Process(target=calc_square, args=(arr,))
    p.start()
    p.join()
    print("result " + str(square_result))
    print("Done")
