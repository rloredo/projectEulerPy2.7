
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isPythTripl(a,b,c):
    return a**2 + b**2 == c**2 and (a < b and b < c)

#Encontrar triplete que sume n
def findPyth(n):
    a = 1
    b = 1
    # Iterar a y b
    while a < n:
        while b < n - a:
            # Encontrar c como la resta
            c = n - a - b
            # Si c es < b no cumple condicion y no vale la pena chequear
            if c < b:
                break
            #Chequear si es triplete
            if isPythTripl(a, b, c):
                return str(a) + ' + ' + str(b) + ' + ' + str(c) + ' = ' + str(a+b+c) + '  producto: ' + str(a*b*c)
            b = b + 1
        a = a + 1
        b = a


print findPyth(1000)
