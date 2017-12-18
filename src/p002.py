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
"""
from math import log

