"""p004.py

Dynamic programming approach to the problem stated at 
https://projecteuler.net/problem=4

Just a bit of multiplication table knowledge applied.

O(length)
    length = log_10 (factors)

Legal bits:
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2017 prosaiccode

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed. [Show more creativity than "p004"!]

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""

from sys import argv
from time import time


def __init__(length=3):
    """
    """
    if length <= 0:
        raise Exception("What you talkin' about?")
    
    
    palindrome = ""
    # start time
    start = time()
    
    hl = round(length / 2)
    if length % 2:
        if length != 1:
            maximum = int('9' * length)
            palinprime = maximum
            while not palindrome:
                palinprime -= 1
                composidrome = int(str(palinprime) + str(palinprime)[::-1])
                i = int(composidrome ** .5)
                while composidrome / i < maximum:
                    if composidrome // i == composidrome / i:
                        palindrome = str(composidrome)
                        break;
                    r = i % 10
                    if r in {1, 3, 9}:
                        i -= 2
                    elif r in {4, 5, 6, 7, 8}:
                        i -= (r - 3)
                    else:
                        i -= 1   
        else:
            palindrome = '9'
    else:
        palindrome += '9' * hl
        palindrome += '0' * hl
        palindrome += palindrome[::-1]
    # end time
    end = time()
    
    delta_time = end - start
    print("time:", delta_time)
    print("palindrome:", palindrome)
    return palindrome, delta_time

if __name__ == '__main__':
    if len(argv) == 2:
        __init__(argv[1])
    else:
        __init__(5)

