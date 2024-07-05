# Function isIn(char, aStr) #

Test if char is in aStr using recursion

## Assumptions ##

char will be a single character and aStr will be a string that is in alphabetical order.

## Return ##

a boolean value.

## Tests ##

using pytest
isIn('a', '') = False
isIn('q', 'ccdeeijlmoppqqtuuvy') = True #odd
isIn('x', 'x') = True #odd
isIn('v', 'acdhjlopqsvwy') = True #odd
sIn('m', 'fgijnnpptwxxxy') = False #even
isIn('c', 'cffggkssuvxxyz') = True #even
isIn('p', 'acdhrrs') = False #odd
isIn('y', 'korstz') = False #even
isIn('h', 'adiloqqvvyz') = False #odd
