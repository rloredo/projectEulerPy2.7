# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.


#Utilizamos la formula de suma de Gauss y de suma de cuadradoDeSuma
#De manera iterativa (efectivamente calculando las sumatorias) se puede hacer
#pero obviamente seria menos eficiente
def diferenciaSumaCuadrados(n):
    cuadradoDeSuma = ((n*(n+1))/2)*((n*(n+1))/2)
    sumaDeCuadrados = (n*(n+1)*(2*n + 1))/6
    return cuadradoDeSuma - sumaDeCuadrados

print diferenciaSumaCuadrados(100)
