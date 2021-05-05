from numpy import NaN

import methods
import random


epsilon = 10 ** (-8)
h = 10 ** (-5)
F = [1/3, -2, 2, 3]
# F = [1,0,1]
# F = [1, -6, 13, -12, 4]
flag = 1 # no trigo
# flag = False # sin function on F last index
# flag = True # cos function on F last index


i = 1
x0 = random.uniform(-10, 10)
x_stelat1 = methods.dehghan_hajarian_method(x0, F, flag, i, h, epsilon)

while x_stelat1 is None:
    x0 = random.uniform(-10, 10)
    x_stelat1 = methods.dehghan_hajarian_method(x0, F, flag, i, h, epsilon)

if methods.F_derivat_secund(F, flag, x_stelat1, h) > 0:
    # print(methods.F_derivat_secund(F, flag, x_stelat1, h))
    print("Punctul critic x* =", x_stelat1,
          "calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F.")
else:
    print("Punctul critic x* =", x_stelat1,
          "calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!")
print("\n")


i = 2
x_stelat2 = methods.dehghan_hajarian_method(x0, F, flag, i, h, epsilon)

if methods.F_derivat_secund(F, flag, x_stelat2, h) > 0:
    # print(methods.F_derivat_secund(F, flag, x_stelat2, h))
    print("Punctul critic x* =", x_stelat2,
          "calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F.")
else:
    print("Punctul critic x* =", x_stelat2,
          "calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!")
