#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def findSum(n):
    sum = 0
    i = 0
    while i < n:
        if i % 5 == 0 or i % 3 == 0:
            sum = sum + i
        i = i + 1
    return sum

print findSum(1000)
print findSum(10)
