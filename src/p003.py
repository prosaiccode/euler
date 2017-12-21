"""p003.py

Dynamic programming approach to the problem stated at 
https://projecteuler.net/problem=3

As dynamic as this problem allows.
Would need a quantum computer to truly improve this
Pollard's_rho_algorithm
    Trial division is faster for smaller n values or if the 
    primes are not close to the square root of the value.
Quantum computing has a better algorithm
    
O(n^.25)    # pulled from Wikipedia
Trial division O(n^.5)

Legal bits:
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2017 prosaiccode

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed. [Show more creativity than "p003"!]

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""

from sys import argv
from time import time

def __init__(n=6008514751431):
    """
    """
    if n < 2:
        raise Exception("Why you do this?")
    # start
    start = time()
    
    gp = 1
    x, y, cycle, prime_factor = 2, 2, 2, 1
    
    # GET RID OF THE TWOS!!!!
    while not n & 1:
        n >>= 1
    if n == 1:
        prime_factor = gp = 2
    
    while prime_factor == 1:
        for _ in range(cycle):
            if prime_factor > 1:
                break
            x = (x * x + 1) % n
            prime_factor = gcd(x - y, n)
        cycle <<= 1
        y = x
        if prime_factor != 1:
            if gp < prime_factor:
                gp = prime_factor
            n = int(n / prime_factor)
            if n != 1:
                prime_factor = 1
    
    end = time()
    
    prime_factor = gp
    
    delta_time = end - start
    print("time:", delta_time)
    print("factor:", prime_factor)
    return prime_factor, delta_time

def gcd(a, b):
    """
    """
    while b:
        _ = a % b
        a = b
        b = _
    return a

if __name__ == '__main__':
    if len(argv) == 2:
        __init__(argv[1])
    else:
        __init__()
