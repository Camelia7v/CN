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
    rand_nr = random.uniform(x[i - 1], x[n])
    if rand_nr == x[i-1]:
        x[i] = random.uniform(x[i - 1], x[n])
    else:
        x[i] = rand_nr
print("x:", x)

y = list()
for i in range(n+1):
    y.append(f(x[i]))
print("y:", y)

x_barat = random.uniform(x[0], x[n])
while True:
    if x_barat not in x:
        break
    else:
        x_barat = random.uniform(x[0], x[n])
print("x_barat:", x_barat)

m = 3
print("m:", m)

print("aproximarea lui f(x_barat) =", methods.metoda_celor_mai_mici_patrate(x_barat, x, y, n, m))
print("f(x_barat) =", f(x_barat))

# print(methods.horner_method([1, -12, 30], 0))
