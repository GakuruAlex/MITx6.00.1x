def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    L , R = 0, len(aStr)

    mid = int((L + R) / 2)
    if R == 0:
        return False
    elif char == aStr[mid]:
            return True
    while R != 1:
        if char < aStr[mid]:
                    return isIn(char, aStr[L:mid])
        else:
                    return isIn(char, aStr[mid:R+1])

    return False

def main():
    print(isIn("z", ""))

if __name__ == "__main__":
    main()
