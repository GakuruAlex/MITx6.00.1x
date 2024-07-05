def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    a, b = max(abs(a),abs(b)), min(abs(a),abs(b))

    if b == 0:
        return a
    else:
        r = a % b
        a,b = b, r
        return gcdRecur(a, b)


def main():
    print(gcdRecur(6,12))

if __name__ == "__main__":
    main()