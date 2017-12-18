"""
Find n of fibonacci(n)

limit = fibonacci(n)
n = math.log(limit * 5 ** .5) / (math.log(golden ratio) - math.log(1/golden ratio) * 2
This loses precision after fibonacci(71) = 308,061,521,170,129 due to python's limitation with
floating point percision.
Alternatives include using Decimal but that's still limited to 424999998
And using that eats up computation time.
n should still only be off by a very small % at very large n's. And the small
amount of error shouldn't affect n by more than 1 in either direction.
To check the matrix table will be used to quickly find the exact 
since the worse case should only require one extra step.
"""
from math import log

