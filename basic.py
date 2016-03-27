from fractions import Fraction
from math import factorial
import itertools
import random

"""
Goal : urn contains 23 balls, 8 white, 6 blue, 9 red
       6 balls are selected at radom

       What's the prob that of each of the following outcomes:
       - all balls are red
       - 3 are blue, 2 are white, 1 is red
       - exactly 4 are white
"""
def P(event, space):
    """Probability of an event given a sample space of equiprobable outcomes
    . Event can be either a set of outcomes or a predicate to be applied over
    the sample space"""
    if is_predicate(event):
        event = such_that(event, space)

    return Fraction(len(event & space), len(space))

is_predicate = callable

def such_that(predicate, collection):
    """Apply predicate over each element of the collection and return the filtered
    collection"""
    return {e for e in collection if predicate(e) }

def cross(A, B):
    "Ways of concatenating 1 item from collection A with another from C"
    return {a + b
            for a in A for b in B}

def combos(items, n):
    "All combinations of n items, each combo as a concatenated string"
    return {' '.join(combo)
            for combo in itertools.combinations(items, n)}

def choose(n, c):
    return factorial(n) / (factorial(n-c)*factorial(c))

#Generate the contents of the urn(total 23 balls)
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789') 
print urn, len(urn)

#Generate combinations of picking 6 balls from the urn
U6 = combos(urn, 6)

#Prob of selecting 6 red balls from the urn
red6 = {s for s in U6 if s.count('R') == 6}
print P(red6, U6)

#Prob of 3B, 2W , 1R
b3w2r1 = {s for s in U6 if
                        s.count('B') == 3 and s.count('W') == 2 and s.count('R') == 1}
print P(b3w2r1, U6)

def even(n):
    return n % 2 == 0

print random.sample(U6, 10)
print choose(4,2)

#Prob of selecting 6 red balls from the urn
red6 = {s for s in U6 if s.count('R') == 6}
print P(red6, U6)

#Generate all possible outcomes when 3 die are rolled
D = {1,2,3,4,5,6}
D3 = {(d1, d2, d3) for d1 in D for d2 in D for d3 in D}

#Find prob that the sum of a 3 die roll is prime
def prime_sum(outcome):
    return is_prime(sum(outcome))

def is_prime(n):
    return n > 1 and not any(n % i == 0 for i in range(2, n))

print P(prime_sum, D3)

#Test code
even_roll={2,4,6}
print "Expected prob:", P(even_roll,D)
print "Expected prob(same as above):", P(even, D)

