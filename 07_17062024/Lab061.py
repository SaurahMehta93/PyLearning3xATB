# Factorial
import math

n = 5
fact = 1
#result = math.factorial(n)
#print(result)

#for i in range(1, n+1):
#    fact = fact * i

#print(fact)

while(n > 0):
    fact = fact * n
    n = n - 1

print(fact)