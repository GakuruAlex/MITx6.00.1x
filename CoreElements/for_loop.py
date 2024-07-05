school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0
chars = []
for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        chars.append(char)
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print(chars)
print('numCons is: ' + str(numCons))
 