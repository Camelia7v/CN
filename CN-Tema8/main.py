from numpy import NaN

import methods
import random
message1=""
message2=""

epsilon = 10 ** (-8)
h = 10 ** (-5)
F = [1/3, -2, 2, 3]
# F = [1,0,1]
# F = [1, -6, 13, -12, 4]
flag = 1 # no trigo
# flag = False # sin function on F last index
# flag = True # cos function on F last index


i1 = 1
k1 = 0
x0 = random.uniform(-10, 10)
x_stelat1, k1 = methods.dehghan_hajarian_method(x0, F, flag, i1, h, epsilon)

while x_stelat1 is None:
    x0 = random.uniform(-10, 10)
    x_stelat1, k1 = methods.dehghan_hajarian_method(x0, F, flag, i1, h, epsilon)

if methods.F_derivat_secund(F, flag, x_stelat1, h) > 0:
    # print(methods.F_derivat_secund(F, flag, x_stelat1, h))
    message1 = ("Punctul critic x* = %f calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F." % (x_stelat1))
    print("Punctul critic x* =", x_stelat1,
          "calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F.")
else:
    message1 = ("Punctul critic x* = %f calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!" % (x_stelat1))
    print("Punctul critic x* =", x_stelat1,
          "calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!")
print("\n")


i2 = 2
k2 = 0
x_stelat2, k2 = methods.dehghan_hajarian_method(x0, F, flag, i2, h, epsilon)
while x_stelat2 is None:
    x0 = random.uniform(-10, 10)
    x_stelat2, k2 = methods.dehghan_hajarian_method(x0, F, flag, i2, h, epsilon)

if methods.F_derivat_secund(F, flag, x_stelat2, h) > 0:
    # print(methods.F_derivat_secund(F, flag, x_stelat2, h))
    message2 = ("Punctul critic x* = %d calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F." % (x_stelat2))
    print("Punctul critic x* =", x_stelat2,
          "calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F.")
else:
    message2 = ("Punctul critic x* = %d calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!" % (x_stelat2))
    print("Punctul critic x* =", x_stelat2,
          "calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!")

methods.cerinta_interface(x0,i1,i2,k1,k2,x_stelat1,x_stelat2,message1,message2)