"""p002.py

Dynamic programming approach to the problem stated at 
https://projecteuler.net/problem=2

Finds the n of F(limit) then "sums" the values of the even/odd values
less than the limit and returns them. Slowest part of the
algorithm is finding the true F(n) values. which is limited to a 
theoretical max of 359 instructions. (limit=2.8e+213)

O(log(log(n)))

Legal bits:
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2017 prosaiccode

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed. [Show more crativity than "p002"!]

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""

from math import log
from sys import argv
from time import time

def __init__(limit=4000000):
    """
    """
    if limit > 8e+307:
        raise Exception("python limit. Use value less than 8e307")
    
    sum_of_even_fibonacci = 0
    # start time
    start = time()
    
    n = int(round(fib_n(limit)) // 3 * 3)
    f = fibonacci(n)
    if f[1][0] <= limit:
        sum_of_even_fibonacci = (f[0][0] + f[0][1] - 1) >> 1
    else:   # catches the rounding errors from fib_n(limit)
        sum_of_even_fibonacci = (f[1][1] - 1) >> 1
    
    # end time
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
    Parameters
    ----------
    v: int
        Fibonacci(n)
    
    Returns
    -------
    return: float
        approximate value of n for v = Fibonacci(n)
    """
    return 2 * log(v * 5 ** .5) / (log( (1 + 5 ** .5) / 2) - log(2 / (1 + 5 ** .5)))

if __name__ == '__main__':
    """
    # tests
    __init__(609)
    __init__(610)    # f(15)
    __init__(611)
    __init__(986)
    __init__(987)    # f(16)
    __init__(988)
    __init__(1596)
    __init__(1597)   # f(17)
    __init__(1598)
    # maximum
    __init__(7e+307) # f(1474.702)
    # worse cases
    __init__(fibonacci(1023)[0][1])
    __init__(fibonacci(1023)[0][1]-1)
    __init__(fibonacci(1023)[0][1]+1)
    __init__(fibonacci(1023)[0][1]+fibonacci(1022)[0][1]-1)
    """
    if len(argv) == 2:
        __init__(argv[1])
    else:
        __init__()
    # """
