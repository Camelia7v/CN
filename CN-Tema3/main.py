import copy
import methods

# memorare matricea b
with open("b.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    p = int(lines[1])
    q = int(lines[2])
    a = list()
    for i in range(4, n + 4):
        a.append(float(lines[i][:-1]))
    b = list()
    for i in range(n + 5, n + 5 + n - 1):
        b.append(float(lines[i][:-1]))
    c = list()
    for i in range(n + 5 + n - 1 + 1, n + 5 + n - 1 + 1 + n - 1):
        c.append(float(lines[i][:-1]))

# print("a: ", len(a), a, "\n")
# print("b: ", len(b), b, "\n")
# print("c: ", len(c), c, "\n")


# memorare matricea a
with open("a.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    m = methods.create_empty_list_of_dicts(n)
    for i in range(2, 7108):
        if int(lines[i].split(',')[2]) in m[int(lines[i].split(',')[1])]:
            aux = m[int(lines[i].split(',')[1])].get(int(lines[i].split(',')[2]))
            m[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = aux + float(lines[i].split(',')[0])
        else:
            m[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])

# print("m: ", len(m), m, "\n")


# adunarea matricelor A + B
aplusb = copy.deepcopy(m)
for i in range(0, len(aplusb)):
    for j in aplusb[i].keys():
        if i == j:
            aux = aplusb[i].get(j)
            aplusb[i][j] = aux + a[i]
        if j - i == q:
            aux = aplusb[i].get(j)
            aplusb[i][j] = aux + b[i]
        if i - j == p:
            aux = aplusb[i].get(j)
            aplusb[i][j] = aux + c[j]

for i in range(0, len(a)):
    for j in aplusb[i].keys():
        if i != j and i not in aplusb[i] and a[i] != 0.0:
            aplusb[i][i] = a[i]
            break

for i in range(0, len(b)):
    for j in aplusb[i].keys():
        if i + 1 != j and i + 1 not in aplusb[i] and b[i] != 0.0:
            aplusb[i][i + 1] = b[i]
            break

for i in range(0, len(c)):
    for j in aplusb[i + 1].keys():
        if i != j and i not in aplusb[i + 1] and c[i] != 0.0:
            aplusb[i + 1][i] = c[i]
            break

# print("A + B: ", "\n", aplusb, "\n")


# sortare apusb
sorted_aplusb = methods.sort_matrix(aplusb)

# print("sorted A + B", "\n", sorted_aplusb, "\n")


# memorare matricea aplusb
with open("aplusb.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    aplusb_din_fisier = methods.create_empty_list_of_dicts(n)
    for i in range(2, 11143):
        aplusb_din_fisier[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])

# print("A + B din fisier: ", "\n", methods.sort_matrix(aplusb_din_fisier))


# verificare adunare
verificare1 = methods.equal(aplusb_din_fisier, sorted_aplusb)


# inmultirea matricelor A * B
aorib = methods.create_empty_list_of_dicts(n)
for i in range(0, len(m)):
    for j in range(0, len(m)):
        suma = 0
        for k in m[i].keys():
            if k == j:
                suma += m[i].get(k) * a[j]
            if j - k == q:
                if j >= q:
                    suma += m[i].get(k) * b[j-q]
                else:
                    suma += 0
            if k - j == p:
                if j < len(c):
                    suma += m[i].get(k) * c[j]
                else:
                    suma += 0
        if suma != 0:
            aorib[i].update({j: suma})

# print("A * B: ", "\n", aorib)


# memorare matricea aorib
with open("aorib.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    aorib_din_fisier = methods.create_empty_list_of_dicts(n)
    for i in range(2, 21285):
        aorib_din_fisier[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])

# print("A * B din fisier: ", "\n", aorib_din_fisier)

verificare2 = methods.equal(aorib, aorib_din_fisier)

methods.gui_interface_citire("Citirea matricilor rare", "Matricea A", "Cei 3 vectori ai matricii B", m, (a, b, c))
methods.gui_interface_operatii("Adunarea matricilor rare", "Matricea A+B", "Rezultatul din fisier",
                               methods.sort_matrix(aplusb),
                               methods.sort_matrix(aplusb_din_fisier), verificare1)
methods.gui_interface_operatii("Inmultirea matricilor rare", "Matricea A*B", "Rezultatul din fisier",
                               methods.sort_matrix(aorib),
                               methods.sort_matrix(aorib_din_fisier), verificare2)
