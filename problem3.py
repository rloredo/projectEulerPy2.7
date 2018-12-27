# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math as m

def isPrime(n):
    esPrimo = False
    j = 2

    while n % j != 0 and j != m.sqrt(n):
        if j == 2:
            j = 3
        else:
            j = j + 2

    if j == n:
        esPrimo = True

    return esPrimo


#Esta es la solucion pero hay que optimizar porque tarda mucho
def encontrarDivisores(n):
        j = n/2
        if j % 2 == 0:
            j = j + 1
        divisoresPri = -1

        while j - 2 > 0:
            if n % j == 0 and isPrime(j):
                divisoresPri = j
                break
            if j % 10 == 7:
                j = j - 4
            else:
                j = j - 2

        return divisoresPri


#si bien ponen esta solucion, puede no ser, porque en realidad encuentra el minimo no sirve para el maximo
def encontrarDivisoresSq(n):
        j = int(round(m.sqrt(n),0))
        if j % 2 == 0:
            j = j + 1
        divisoresPri = -1

        while j - 2 > 0:
            if n % j == 0 and isPrime(j):
                divisoresPri = j
                break
            if j % 10 == 7:
                j = j - 4
            else:
                j = j - 2

        return divisoresPri

print encontrarDivisoresSq(600851475143)
print encontrarDivisoresSq(90012332)
print encontrarDivisores(90012332)
