import numpy
import methods

epsilon = 10 ** (-8)

# a = [1, -6, 11, -6]
# a = [42, -55, -42, 49, -6]
# a = [8, -38, 49, -22, 3]
a = [1, -6, 13, -12, 4]
n = len(a) - 1

R = methods.calculeaza_intervalul(a)
print("[-R,R]:", "[", -R, ",", R, "]")

roots = []
x_0 = []
count = 0
while count < n:
    k = methods.olver_method(a, R, epsilon)
    if k is not None:
        root = k[0]
        x0 = k[1]
        if len(roots) >= 1 and root not in roots and abs(roots[len(roots) - 1] - root) > epsilon:
            roots.append(root)
            x_0.append(x0)
            count += 1
        elif len(roots) == 0:
            roots.append(root)
            x_0.append(x0)
            count += 1

print("x0:", x_0)
print("roots:", roots)
methods.cerinta_interface("Tema 7", "Intervalul [-R,R]: ", "[" + str(-R) + "," + str(R) + "]", "x0 : ", x_0, "roots: ",
                          roots)

# f = open('exemplu1.txt', 'w')
# for x in roots:
#     f.write(str(x) + '\n')
# f.close()


p = a
p1 = numpy.polyder(a)  # p'
p2 = numpy.polyder(a, 2)  # p"

# 1
gcd_value = methods.polynomials_gcd(p, p1, 2, epsilon)
# x-2
# gcd_value = methods.polynomials_gcd(p1, p2,0,epsilon)

print("p:", p)
print("p':", p1)
print('p":', p2)
print(gcd_value)

# methods.bonus_interface("Bonus","Polinomul p' :", p1,"Polinomul p'' :", p2,"Rezultatul gcd:", gcd_value)
