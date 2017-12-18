"""
Find n of fibonacci(n)

limit = fibonacci(n)
n = math.log(limit * 5 ** .5) / (math.log(golden ratio) - math.log(1/golden ratio) * 2
The two at the end is because of the power is taken twice.

Ranges of n:
  0-71: exact
  72- : possible to be larger than the actual value by exactly .9% [still trying to find exact but this is close] (floor)
"""
from math import log

