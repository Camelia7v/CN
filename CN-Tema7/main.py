import methods

epsilon = 10 ** (-8)

a = [1, -6, 11, -6]
# a = [42, -55, -42, 49, -6]
# a = [8, -38, 49, -22, 3]
# a = [1, -6, 13, -12, 4]
n = len(a) - 1

R = methods.calculeaza_intervalul(a)
print("[-R,R]:", "[", -R, ",", R, "]")

roots = []
x_0 = []
count = 0
while count < n * n:
    k = methods.olver_method(a, R, epsilon)
    if k is not None:
        root = k[0]
        x0 = k[1]
        print(roots)
        if len(roots) >= 1 and root not in roots and abs(roots[len(roots) - 1] - root) > epsilon:
            roots.append(root)
            x_0.append(x0)
            count += 1

            # flag = 1
            # for i in range(len(roots)):
            #     if abs(roots[i] - root) < epsilon:
            #         flag = 0
            # if flag == 1:
            #     roots.append(root)
            #     x_0.append(x0)
            #     count += 1

        elif len(roots) == 0:
            roots.append(root)
            x_0.append(x0)
            count += 1

print("x0:", x_0)
print("roots:", roots)

f = open('exemplu1.txt', 'w')
for x in roots:
    f.write(str(x) + '\n')
f.close()
