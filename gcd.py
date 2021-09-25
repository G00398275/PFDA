# gcd.py
# Author: Ross Downey
# Revision of While Loops

a = 252
b = 105

while b > 0:
    a, b = b, a % b
print (a)

# Determines the greatest common denominator of a and b.
# Need to use while loop so numbers greater than 0 are only used.
# while b is greater than 0, a becomes b, b becomes a divided by b
