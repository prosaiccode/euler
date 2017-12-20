def coprimes(argv):
    return [(a * b for a in argv for b in argv if a != b)]

def product(argv):
    if 0 in argv:
        return 0
    p = 1
    for i in argv:
        p *= i
    return p

def fizz_buzz_magic(argv):
    """
    
    Return
    ------
    magic_number: int
        the number used to represent the whole (assumes starts at 1)
    magic_length: int
        the length of the mask in bits
    magic_shift:
        the distance the masked bits need to be shift to perform a rotational
        shift operation
    magic_mask: bin
        1 to represent the value used. 0 if that value was not used.
    """
    if not argv:
        return 0
    p = product(argv)
    if not p:
        return 0
    magic_length = len(argv)
    magic_number = 0
    for argi in range(magic_length):
        for i in range(1,p+1):
            if not i % argv[argi]:
                magic_number |= (1 << (magic_length * i) + argi)
    magic_number >>= magic_length
    magic_mask = 0
    for i in range(magic_length):
        magic_mask |= 1 << i
    magic_shift = (len(bin(magic_number)) - 2) - magic_length
    return magic_number, magic_length, magic_shift, magic_mask

def e_001_test(n, magic_number, magic_length, magic_shift, magic_mask):
    s = 0
    magic_carry = 0
    for i in range(1,n):
        magic_carry = (magic_number & magic_mask)
        if magic_carry:
            s += i
        magic_number = (magic_number >> magic_length) | (magic_carry << magic_shift)
    return s

n = 1000
s = [3,5]
magic_number, magic_length, magic_shift, magic_mask = fizz_buzz_magic(s)
print(e_001_test(n, magic_number, magic_length, magic_shift, magic_mask))
