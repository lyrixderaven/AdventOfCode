# lol monte carlo for the win :-)
from inputs import TWENTIETH

housenumber = 0

import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

# # Part 1
# while True:
#     housenumber += 1
#     divisors = list(divisorGenerator(housenumber))
#     presents = sum([num * 10 for num in divisors])
#     print housenumber, presents
#     if presents >= TWENTIETH.input:
#         break

# Part 2
while True:
    housenumber += 1
    divisors = list(divisorGenerator(housenumber))
    presents = sum([num * 11 for num in divisors if housenumber / num <= 50])
    print housenumber, presents
    if presents >= TWENTIETH.input:
        break


