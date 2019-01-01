
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isPythTripl(a,b,c):
    return a**2 + b**2 == c**2 and (a < b and b < c)

print isPythTripl(3,4,5)


#Encontrar triplete que sume n
def findPyth(n):
    for a in range(1, n):
        for b in range(a, n - a):
            c = n - a - b
            if c < b:
                break
            if isPythTripl(a, b, c):
                return str(a) + ' + ' + str(b) + ' + ' + str(c) + ' = ' + str(a+b+c) + '  producto: ' + str(a*b*c) 

print findPyth(1000)
