# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from stacks import *

def esPalin(n):
    n = str(n)
    if len(n) % 2 != 0:
        return False
    else:
        i = 0
        mitad = len(n)/2
        stack1 = stack()
        str1 = ''
# Invertir la primera mitad del numero con una stack
        while i < mitad:
            stack1.pile(n[i])
            i = i + 1
        while stack1.empty() != True:
            str1 = str1 + stack1.top()
            stack1.unpile()

        str2 = n[mitad:len(n)]

        #Comparar mitades y devolver si es palindrome o no
        if str1 == str2:
            return True
        else:
            return False

#n indica el número de dígitos, para este problema n = 3
def buscarLargerPalinProd(n):
    j = ''
    i = 0
    while i < n:
        j = j + '9'
        i = i + 1

    j = int(j)
    c = j
    k = j
    listaPalin = []
    while k > 1:
        j = c
        while j > 0:
            if esPalin(j*k):
                listaPalin.append([j*k, j, k])
            j = j - 1
        k = k - 1
    return max(listaPalin)



print buscarLargerPalinProd(3)
