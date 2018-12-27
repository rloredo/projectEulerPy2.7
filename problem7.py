#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

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



#Primos excepto 2 son impares y excepto 5 no terminan en 5
#Aca busca todos los primos y devuelve el ultimo
#Para mas eficiencia se puede usar un contador,
#pero se pierde la gracia de calcular todos los primos
def buscarElPrimo(n):
    i = 9
    primos = [1,2,3,5,7 ]
    while len(primos) <= n:
        if isPrime(i):
            primos.append(i)
        i = i + 2
    return primos[-1]


print buscarElPrimo(10001)
