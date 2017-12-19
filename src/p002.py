"""
Find n of fibonacci(n)

limit = fibonacci(n)
n = math.log(limit * 5 ** .5) / (math.log((1 + 5 ** .5) / 2) - math.log(2 / (1 + 5 ** .5)) * 2
The two at the end is because of the power is taken twice.

Ranges of n:
  Possible to off by 1 due to rounding.
  It's assumed that `limit` is larger than 1. Since fibonacci(1) and fibonacci(2) are both 1.
  n can't be larger than 1474. Python rounds math.log(fibonacci(1475) * 5 ** .5) to infinity.
  
  The program works through to 8.039528104473e+307  (fibonacci(1475) = 1e+308)
  
sum(fibonacci(0),fibonacci(n)) = fibonacci(n+2) - fibonacci(2)
sum(lucas(1),lucas(n)) = lucas(n+2) - lucas(2)

Only even values:
  if f1 and f2 are even: count all
  else if f1 even and not f2: count f1 + f4 + f7 + f10 ...
  else if f2 even and not f1: count f2 + f5 + f8 + f11 ...
  else: count f3 + f6 + f9 + f12 ...

elses' formula for even values: 4 * f(n-1) + f(n-2)
  recursive sum: sigma from x=1 to k=n//3
"""
from math import log
from sys import argv

def __init__(limit, f1=1, f2=2):
  

def fibonacci(n, f1=1, f2=1):
  A = [[f1, f2], [f2, f2-f1]]
  
  

def fib_n(v):
  return 2 * log(v * 5 ** .5) / (math.log( (1 + 5 ** .5) / 2) - math.log(2 / (1 + 5 ** .5))

if __naim__ == '__main__':
    __init__(4000000)
