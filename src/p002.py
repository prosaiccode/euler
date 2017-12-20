"""
"""

from math import log
from sys import argv
from time import time

def __init__(limit):
    """
    """
    if limit > 8e+307:
        raise Exception("python limit. Use value less than 8e307")
    
    start = time()
    
    n = int(round(fib_n(limit)) // 3 * 3)
    f = fibonacci(n)
    if f[1][0] <= limit:
        sum_of_even_fibonacci = (f[0][0] + f[0][1] - 1) >> 1
    else:   # catches the rounding errors
        sum_of_even_fibonacci = (f[1][1] - 1) >> 1
    
    end = time()
    
    delta_time = end - start
    print("time:", delta_time)
    print("sum:", sum_of_even_fibonacci)
    return sum_of_even_fibonacci, delta_time

def fibonacci(n):
    """
    """
    A = [[1, 1], [1, 0]]
    I = [[1, 0], [0, 1]]
    while n > 0:
        if n & 1:
            # I = I * A
            I = [[A[0][0] * I[0][0] + A[1][0] * I[0][1], A[0][1] * I[0][0] + A[1][1] * I[0][1]],
                 [A[0][0] * I[1][0] + A[1][0] * I[1][1], A[0][1] * I[1][0] + A[1][1] * I[1][1]]]
        # A = A * A
        A = [[A[0][0] * A[0][0] + A[1][0] * A[0][1], A[0][1] * A[0][0] + A[1][1] * A[0][1]],
             [A[0][0] * A[1][0] + A[1][0] * A[1][1], A[0][1] * A[1][0] + A[1][1] * A[1][1]]]
        n >>= 1
    return I

def fib_n(v):
    """
    """
    return 2 * log(v * 5 ** .5) / (log( (1 + 5 ** .5) / 2) - log(2 / (1 + 5 ** .5)))

if __name__ == '__main__':
    """
    # extremes
    __init__(609)
    __init__(610)    # f(15)
    __init__(611)
    __init__(986)
    __init__(987)    # f(16)
    __init__(988)
    __init__(1596)
    __init__(1597)   # f(17)
    __init__(1598)
    """
    if len(argv) == 2:
        __init__(argv[1])
    else:
        __init__(7e+307)
    # """
