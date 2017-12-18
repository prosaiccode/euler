"""p001.py

Dynamic programming approach to the problem stated at 
https://projecteuler.net/problem=1

Can take any number of intervals but you might experience
    unexpected results if the there are number q has a 
    composite already in the set. (q will be removed)
    {2,3,6} results in {2,3}. If you want to count 6 twice
    run a separate test using {6} and add the two results
    together.



Legal bits:
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2017 prosaiccode

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed. [Show more crativity than "p001"!]

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""
from sys import argv
from time import time

def __init__(n = 1000, intervals = {3, 5}):
    """Does the heavy hoisting
    
    >>> __init__(10, {2, 3, 6}   # Interuprted as: __init__(10, {2, 3})
    32
    >>> __init__(10, {1, ...}    # Interuprted as: __ini__(10, {1})
    45
    
    Parameters
    ---------
    n: int > 0
        from 1 to (positive infinity - 1)
        the sum will come from this
    intervals: set
        intervals in which things will be counted by
    
    Returns
    -------
    sum_of_intervals: int
        the sum
    delta_time: int
        the delta in time
    """
    # remove composites contained in the set
    _ = set().union(intervals)
    for a in _:
        for b in _:
            if not a % b and a != b and a in intervals:
                intervals.remove(a)
    
    sum_of_intervals = 0
    # start time
    start = time()
    
    s = list(intervals)
    x = list(gen_products(s, 0))
    for i in x:
        if i[1] % 2:
            sum_of_intervals += sum_of_i_intervals_in_n(n, i[0])
        else:
            sum_of_intervals -= sum_of_i_intervals_in_n(n, i[0])
    
    # end time
    end = time()
    
    delta_time = end - start
    print("time:", delta_time)
    print("sum:", sum_of_intervals)
    return sum_of_intervals, delta_time

def sum_of_i_intervals_in_n(n, i):
    """
    (n - 1) // i = total count
    i * (n - 1) // (i + 1) = average weight
    total count * average weight // 2 == sum
    """
    return i * ((n - 1) // i) * ((n - 1) // i + 1) // 2

def coprimes(argv):
    """This and FizzBuzz magic numbers were used for testing"""
    return set(a * b for a in argv for b in argv if a != b)

def gen_products(lst, idx, scale=1, t=0):
    """
    generates a the partial products and the number of multiplicans
    or multipliers it require to reach that result
    Paramters
    ---------
    lst: list
        list of products
    idx: int
        depth of the recursion to prevent overflow
        also used for indexing the list and scaling
    scale: int
        scale which to multiply the remaining sublists
    t: int
        steps to keep track of the number of multiplicands
        or multipliers used
    """
    if idx == len(lst):
        if scale == 1:
            return
        yield scale, t
        return
    for x in gen_products(lst, idx+1, scale, t):
        yield x
    for x in gen_products(lst, idx+1, scale*lst[idx], t+1):
        yield x

if __name__ == '__main__':
    if len(argv) > 2:
        n = argv[1]
        intervals = set(argv[2:])
        __init__(n, intervals)
    else:
        __init__()
