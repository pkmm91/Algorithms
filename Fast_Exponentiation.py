Fast Exponentiation

Pyhton code
 
 
def fast_exponentiation(a , n):
    if n == 0:
        return 1
    if n == 1:
        return a
    t = fast_exponentiation(a , n/2)
    return ( t * t * fast_exponentiation(a , n%2))
             
base = input("Enter the base: ")
exponent = input("Enter the exponent: ")
print "Result is: %s"%(fast_exponentiation(base , exponent))
