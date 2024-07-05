def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    common_divisor: int = min(abs(a), abs(b))
    if common_divisor == 1:
        return 1
    else:
        while common_divisor > 0:
            if a % common_divisor == 0 and b % common_divisor == 0:
                return common_divisor
            else:
                common_divisor -= 1
