# greatest common divisor of two positive integers using recursion #

A function to find GCD of two numbers using recursion via Euclidean Algorithm

## Steps of the Euclidean Algorithm ##

Given two integers  a and b (assume a≥b):

Divide a by b and find the remainder r. Mathematically, this is represented as a=bq+r, where q is the quotient and r is the remainder.Replace a with b and b with r.
Repeat the process until b becomes 0. The GCD is the non-zero remainder from the last non-zero division.

### Examples ###

gcd(161, 84) = 7
gcd(228, 132) = 12
gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1
