#2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

#Con fuerza bruta
def findSmallesDivisible(n):
    i = 2
    number = 10

    while number > 0:
        while number % i == 0 and i < n:
            i = i + 1
        if i == n:
            return number
        else:
            print number
            if n % 10 == 0:
                number = number + 10
            else:
                number = number + 1
            i = 2
#print findSmallesDivisible(20)


#Con factorizacion por primos
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

#Asi como esta no funciona cuando el numero es un cuadrado, V2 si funciona
def findSmallDivByFact(n):
    primosHastaN = []
    noPrimosHastaN = []
    i = 2
    #Hacer lista de primos y no primos
    while i < n:
        if isPrime(i):
            primosHastaN.append(i)
        else:
            noPrimosHastaN.append(i)
        i = i + 1
    #Elegir el mas grande de los no primos factorizable
    #por el mas chico de los primos
    listaFinal = []
    noPrimoGrandeConst = noPrimosHastaN[-1]
    noPrimoGrande = len(noPrimosHastaN) - 1
    while primosHastaN[0] < m.sqrt(noPrimoGrandeConst):
        while m.log(noPrimosHastaN[noPrimoGrande], primosHastaN[0]).is_integer() == False:
            noPrimoGrande = noPrimoGrande - 1
        listaFinal.append(noPrimosHastaN[noPrimoGrande])
        noPrimosHastaN.remove(noPrimosHastaN[noPrimoGrande])
        primosHastaN.remove(primosHastaN[0])
    listaFinal =  listaFinal + primosHastaN
    print listaFinal
    return reduce(lambda x, y: x*y, listaFinal)

#print 'de 20', findSmallDivByFact(20), 'OK'
#print 'de 25', findSmallDivByFact(25), 'Mal, no considera 5^2'
#print 'de 16', findSmallDivByFact(16)



#Para todos los casos incluso cuando el numero es un cuadrado
def findSmallDivByFactV2(n):
    primosHastaN = []
    noPrimosHastaN = []
    i = 2
    #Hacer lista de primos y no primos
    while i <= n:
        if isPrime(i):
            primosHastaN.append(i)
        else:
            noPrimosHastaN.append(i)
        i = i + 1
    #Elegir el mas grande de los no primos factorizable
    #por el mas chico de los primos
    listaFinal = []
    noPrimoGrandeConst = noPrimosHastaN[-1]
    noPrimoGrande = len(noPrimosHastaN) - 1
    while primosHastaN[0] <= m.sqrt(noPrimoGrandeConst):
        while m.log(noPrimosHastaN[noPrimoGrande], primosHastaN[0]).is_integer() == False:
            noPrimoGrande = noPrimoGrande - 1
        listaFinal.append(noPrimosHastaN[noPrimoGrande])
        noPrimosHastaN.remove(noPrimosHastaN[noPrimoGrande])
        primosHastaN.remove(primosHastaN[0])
        noPrimoGrande = noPrimoGrande - 1
    listaFinal =  listaFinal + primosHastaN
    #Usamos reduce para multiplicar por simplicidad. Deberia hacerlo con whiles
    return reduce(lambda x, y: x*y, listaFinal)

print 'de 16', findSmallDivByFactV2(16)
print 'de 25', findSmallDivByFactV2(25)
print 'de 20', findSmallDivByFactV2(20)
