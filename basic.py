from fractions import Fraction

def P(event, space):
    return Fraction(len(event & space), len(space))


D={1,2,3,4,5,6}
even={2,4,6}
print P(even,D)
