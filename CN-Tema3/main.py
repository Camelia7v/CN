import methods

# memorare matricea b
with open("b.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    p = int(lines[1])
    q = int(lines[1])
    a = list()
    for i in range(4, n+4):
        a.append(float(lines[i][:-1]))
    b = list()
    for i in range(n+5, n+5+n-1):
        b.append(float(lines[i][:-1]))
    c = list()
    for i in range(n+5+n-1+1, n+5+n-1+1+n-1):
        c.append(float(lines[i][:-1]))

print("a: ", len(a), a, "\n")
print("b: ", len(b), b, "\n")
print("c: ", len(c), c, "\n")

# memorare matricea a
with open("a.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    m = methods.create_empty_list_of_lists(n)
    for i in range(2, 7108):
        m[int(lines[i].split(',')[1])].append((float(lines[i].split(',')[0]), int(lines[i].split(',')[2])))


# cautare valori cu aceiasi indici
for linie in range(0, len(m)):
    nr1 = 0
    for tupla in range(0, len(m[linie])-1):
        coloana = m[linie][tupla][1]
        nr = 0
        for tupla_urm in range(tupla+1, len(m[linie])):
            if m[linie][tupla_urm][1] == coloana:
                nr += 1
        if nr > 0:
            nr1 += 1
    # print(nr1)


# eliminare valori cu aceiasi indici
for linie in range(0, len(m)):
    for tupla in range(0, len(m[linie])-1):
        coloana = m[linie][tupla][1]
        for tupla_urm in range(tupla+1, len(m[linie])):
            if tupla_urm == len(m[linie]):
                break
            if m[linie][tupla_urm][1] == coloana:
                y1 = list(m[linie][tupla])
                y2 = list(m[linie][tupla_urm])
                y1[0] += y2[0]
                m[linie][tupla] = tuple(y1)
                m[linie][tupla_urm] = tuple(y2)
                m[linie].remove((m[linie][tupla_urm][0], m[linie][tupla_urm][1]))

print("m: ", len(m), m, "\n")


# lipseste ceva
# adunarea matricelor A+B
aplusb = list(m)
for i in range(0, len(a)):
    for j in range(0, len(aplusb[i])):
        if m[i][j][1] == i:
            x = list(aplusb[i][j])
            x[0] += a[i]
            aplusb[i][j] = tuple(x)
        if m[i][j][1] - i == q:
            x = list(aplusb[i][j])
            x[0] += b[i]
            aplusb[i][j] = tuple(x)
        if i - m[i][j][1] == p:
            x = list(aplusb[i][j])
            x[0] += c[i]
            aplusb[i][j] = tuple(x)

print("A + B: ", "\n", aplusb, "\n")

# memorare matricea aplusb
with open("aplusb.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    aplusb_din_fisier = methods.create_empty_list_of_lists(n)
    for i in range(2, 11143):
        aplusb_din_fisier[int(lines[i].split(',')[1])].append((float(lines[i].split(',')[0]), int(lines[i].split(',')[2])))

print("A + B din fisier: ", "\n", aplusb_din_fisier)
