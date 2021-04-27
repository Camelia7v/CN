import math
import numpy
import methods

epsilon = 10 ** (-8)
h = 10 ** (-5)

F = [1/3, -2, 2, 3]
# F = [1, -6, 13, -12, 4]
F1 = numpy.polyder(F, 1)  # F'

x_stelat = methods.dehghan_hajarian_method(F1, epsilon)
while x_stelat is None:
    x_stelat = methods.dehghan_hajarian_method(F1, epsilon)

if methods.F_derivat_secund(F, x_stelat, h) > 0:
    print(methods.F_derivat_secund(F, x_stelat, h))
    print("Punctul critic x* =", x_stelat,
          "calculat cu metoda Dehghan-Hajarian este punct de minim pentru functia F.")
else:
    print(methods.F_derivat_secund(F, x_stelat, h))
    print("Punctul critic x* =", x_stelat,
          "calculat cu metoda Dehghan-Hajarian NU este punct de minim pentru functia F!")
