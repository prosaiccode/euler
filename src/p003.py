"""p003.py

Dynamic programming approach to the problem stated at 
https://projecteuler.net/problem=3

As dynamic as this problem allows.
Would need a quantum computer to truly improve this

O(n ** .5)

Legal bits:
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2017 prosaiccode

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed. [Show more crativity than "p003"!]

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""

from sys import argv
from time import time

def __init__(n):
    """
    """

def gcpf(n):
    """
    """
    limit = n ** .5
    p = 2
    while not n & 1:
        n >>= 1
    if n > 1:
        p = 3
        while n > 1 and p < limit:
            if n % p:
                p += 2
            else:
                n //= p
    if n > 1:
        return int(n)
    return p
        

if __name__ == '__main__':
    pass
