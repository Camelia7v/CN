import methods
import random


"""
Primul exemplu din tema
 a=1 si b=5
"""
f = lambda x: x ** 2 - 12 * x + 30

print("!!! a must be smaller than b !!!")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = int(input("Enter n: "))

x = [0.0] * (n + 1)
x[0] = a
x[n] = b
for i in range(1, n):
    rand_nr = round(random.uniform(x[i - 1], x[n]), 4)
    if rand_nr == x[i-1]:
        x[i] = round(random.uniform(x[i - 1], x[n]), 4)
    else:
        x[i] = rand_nr
print("x:", x)

y = list()
for i in range(n+1):
    y.append(f(x[i]))
print("y:", y)

x_barat = round(random.uniform(x[0], x[n]), 2)
while True:
    if x_barat not in x:
        break
    else:
        x_barat = round(random.uniform(x[0], x[n]), 2)
print("x_barat:", x_barat)
