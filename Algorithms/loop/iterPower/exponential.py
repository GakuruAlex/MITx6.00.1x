def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    power = 1
    count = 0
    if exp == 0:
            return 1
    elif exp == 1:
         return base
    else:
        while count < exp:
            power *= abs(base)
            count += 1
    if base < 0 and exp % 2 !=0:
            return -power
    else:
        return power

def main():
     print(iterPower(-2,3))
if __name__ == "__main__":
   main()

