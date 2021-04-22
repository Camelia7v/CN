import methods

epsilon = 10 ** (-8)

a = [1, -6, 11, -6]
n = len(a) - 1

R = methods.calculeaza_intervalul(a)
print("[-R,R]:", "[", -R, ",", R, "]")
