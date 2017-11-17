def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    common_multiple = 1
    factor = 2
    while factor <= max(a,b):
        if (a % factor == 0 and b % factor == 0):
            common_multiple *= factor
            a /= factor
            b /= factor
        elif (a % factor == 0):
            common_multiple *= factor
            a /= factor
        elif (b % factor == 0):
            common_multiple *= factor
            b /= factor
        else:
            factor += 1
            
    return common_multiple

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    bitset = 0
    num_digits = 0 
    digit_counter = 1
    if n == 0:
        return 1
    
    while n > 0:
        shifter = 1
        ones_place = n % 10
        shifter = shifter << ones_place
        bitset |= shifter
        n //= 10
    for i in range(0,10):
        num_digits += digit_counter & bitset
        bitset = bitset >> 1
    return num_digits
