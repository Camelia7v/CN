import methods
import random
import numpy as np
import matplotlib.pyplot as plt


"""
Primul exemplu din tema
 a=1 si b=5
"""
f = lambda x: x ** 2 - 12 * x + 30
# f = lambda x: 2 * (x ** 3) - 3 * x + 15

# print("!!! a must be smaller than b !!!")
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# n = int(input("Enter n: "))
userInput=methods.start_interface("Setare valori initiale")
a=userInput[0]
b=userInput[1]
n=userInput[2]

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

methods.initial_set_up("Tema 6","Valori intiale",x,y,x_barat)
"""
CERINTA 1
"""

print("\n CERINTA 1 \n")

# Se vor folosi valori ale lui m mai mici ca 6.
m = 5
print("m:", m)

P_de_x_barat = methods.metoda_celor_mai_mici_patrate(x_barat, x, y, n, m)
print("P(x_barat), aproximarea lui f(x_barat) =", P_de_x_barat)
print("f(x_barat) =", f(x_barat))
print("|P(x_barat) - f(x_barat)| =", abs(P_de_x_barat - f(x_barat)))
dif=abs(P_de_x_barat - f(x_barat))
suma = 0
for i in range(n+1):
    P_de_x = methods.metoda_celor_mai_mici_patrate(x[i], x, y, n, m)
    suma += abs(P_de_x - y[i])
print("Suma =", suma)


print(methods.horner_method([1, -12, 30], 0))
methods.cerinta_i("Tema 6","Cerinta 1 \n m:" + str(m) ,"P(x_barat), aproximarea lui f(x_barat) = ",P_de_x_barat,"f(x_barat) = ",f(x_barat), "|P(x_barat) - f(x_barat)| = ",dif, "Suma = ", suma)
"""
CERINTA 2
"""

print("\n CERINTA 2 \n")

f_derivat = lambda x: 2 * x - 12
f_derivat_de_a = f_derivat(a)
print("f'(a) =", f_derivat_de_a)

S_de_x_barat = methods.spline_patratice(x_barat, f_derivat_de_a, x, y, n)
print("S(x_barat), aproximarea lui f(x_barat) =", S_de_x_barat)
print("f(x_barat) =", f(x_barat))
print("|S(x_barat) - f(x_barat)| =", abs(S_de_x_barat - f(x_barat)))
dif2=abs(S_de_x_barat - f(x_barat))

methods.cerinta_i("Tema 6","Cerinta 2 ","f'(a) = ",f_derivat_de_a,"S(x_barat), aproximarea lui f(x_barat) = ",S_de_x_barat,"f(x_barat) = ",f(x_barat),"|S(x_barat) - f(x_barat)| =",dif2)

"""
BONUS
"""
x1 = np.arange(a, b, 0.01)
y1 = x1 ** 2 - 12 * x1 + 30
y2 = list()
for i in x1:
    y2.append(methods.metoda_celor_mai_mici_patrate(i, x, y, n, m))
y3 = list()
for i in x1:
    y3.append(methods.spline_patratice(i, f_derivat_de_a, x, y, n))

# plotting the points
plt.plot(x1, y1, label="f(x)", linewidth=7.0)
# plt.plot(x1, y2, label="P_m(x)")
plt.plot(x1, y3, label="S_f(x)", linewidth=2.0)

# naming the axis
plt.xlabel('x - axis')
plt.ylabel('y - axis')

# giving a title
plt.title('The three graphs')

# show a legend on the plot
plt.legend()
# show the grid
plt.grid(True)
# show the plot
plt.show()
