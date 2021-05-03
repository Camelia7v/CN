import methods
import random


epsilon = 10 ** (-8)
h = 10 ** (-5)
# F = [1/3, -2, 2, 3]
F = [1, -6, 13, -12, 4]


i = 1
x0 = random.uniform(-10, 10)
x_stelat = methods.dehghan_hajarian_method(x0, F, i, h, epsilon)
while x_stelat is None:
    x0 = random.uniform(-10, 10)
    x_stelat = methods.dehghan_hajarian_method(x0, F, i, h, epsilon)

if methods.F_derivat_secund(F, x_stelat, h) > 0:
    print(methods.F_derivat_secund(F, x_stelat, h))
    print("Punctul critic x* =", x_stelat,
          "calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F.")
else:
    print("Punctul critic x* =", x_stelat,
          "calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!")
print("\n")


i = 2
x_stelat = methods.dehghan_hajarian_method(x0, F, i, h, epsilon)

if methods.F_derivat_secund(F, x_stelat, h) > 0:
    print("Punctul critic x* =", x_stelat,
          "calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F.")
else:
    print("Punctul critic x* =", x_stelat,
          "calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!")
