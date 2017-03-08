import time

def sum_of_n(n):

    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i

    end =time.time()

    return theSum, end - start

print(sum_of_n(10))
