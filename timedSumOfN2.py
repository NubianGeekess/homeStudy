import time

def sumof_n2(n):

    start = time.time()

    the_sum = (n*(n+1))/2
    end =time.time()

    return the_sum, end - start

print sumof_n2(10)