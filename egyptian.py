# egyptian algorithm #

from fractions import Fraction
def egypt(rational):
    if rational <= 0 or rational >= 1:
        raise Exception("Rational number out of range" , rational)
    result = []
    while True:
        if rational.numerator == 1:
            result.append(str(rational))
            return result
        unitFraction = Fraction(1, rational.denominator / rational.numerator + 1)
        result.append(str(unitFraction))
        rational = rational - unitFraction
k = Fraction(6,14)
s = egypt(k)
for i in xrange(len(s)-1):
    print "%s +"%(s[i]),
print s[len(s)-1]
