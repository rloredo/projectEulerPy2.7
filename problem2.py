# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


# Solucion

#Crear lista de fibo pares de valores menores a n
def crearFiboParMenorA(n):
    listaInicial = [2 , 8]
    i = 1
    while listaInicial[i] < n:
        listaInicial.append(4 * listaInicial[i] + listaInicial[i - 1])
        i = i + 1
    listaInicial.remove(listaInicial[len(listaInicial)-1])
    return listaInicial


#Print suma de los valores menores a 4 millones
print sum(crearFiboParMenorA(4000000))



#Otras cosas para el razonamiento
# Encontrar el n termino  de la secuencia. Recursivo
def fiboRec(n):
    if n == 0:
        n = 0
    elif n == 1:
        n = 1
    else:
        n = fiboRec(n-1) + fiboRec(n-2)
    return n

# Encontrar el n termino par de la secuencia. Recursivo
def fiboRecPares(n):
    if n == 0:
        n = 2
    elif n == 1:
        n = 8
    else:
        n = 4 * fiboRec(n-1) + fiboRec(n-2)
    return n

#Crear la lista de cantidad terminos
def listaFibo(cantidad):
    lista = []
    i = 0
    while i < cantidad + 1:
        lista.append(fiboRec(i))
        i = i + 1
    return lista

# Crear lista fibo todos
def crearFibo(cantidad):
    listaInicial = [0, 1]
    i = 1
    while i < cantidad + 1:
        listaInicial.append(listaInicial[i] + listaInicial[i - 1])
        i = i + 1
    listaInicial.remove(listaInicial[0])
    return listaInicial


#Crear lista fibo pares
def crearFiboPares(cantidad):
    listaInicial = [2, 8]
    i = 1
    while i < cantidad + 1:
        listaInicial.append(4 * listaInicial[i] + listaInicial[i - 1])
        i = i + 1
    return listaInicial

#Crear lista de fibo de valores menores a n
def crearFiboMenorA(n):
    listaInicial = [1 , 1]
    i = 1
    while listaInicial[i] < n:
        listaInicial.append(listaInicial[i] + listaInicial[i - 1])
        i = i + 1
    listaInicial.remove(listaInicial[len(listaInicial)-1])
    return listaInicial
