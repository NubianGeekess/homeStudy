# An example of a recursive function to
# find the factorial of a number
def recur_fact(x):
    """
    This is a recursive function to find the factorial of an integer
    """
    if x == 1:
        return 1
    else:
        print (x * recur_fact(x - 1))

recur_fact(5)
