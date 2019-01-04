# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

#Reutilizamos codigo de problema 7

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    limit = int(n ** 0.5) + 1
    i = 3
    while i < limit:
        if n % i == 0:
            return False
        i = i + 2
    return True


#Primo menor a n
def buscarElPrimo(n):
    i = 9
    primos = [2,3,5,7 ]
    while primos[-1] < n:
        if isPrime(i):
            primos.append(i)
        i = i + 2
    primos.remove(primos[-1])
    return primos


def sumaPrimos(n):
    return sum(buscarElPrimo(n))


print sumaPrimos(2000000)
