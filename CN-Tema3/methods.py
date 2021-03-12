def create_empty_list_of_dicts(n):
    return [{} for i in range(0, n)]


def verifying_two_dictionaries(a, b):
    if len(a) != len(b):
        return False
    for i in a.keys():
        if abs(a[i] - b[i]) > 10 ** (-13):
            return False
    return True


def equal(A, B):
    count = 0
    for i in range(0, len(A)):
        if verifying_two_dictionaries(B[i], A[i]) is False:
            count += 1
    if count > 0:
        print("\n", "Matricele nu sunt egale", "\n")
    else:
        print("\n", "Matricele sunt egale", "\n")


def sort_matrix(a):
    sorted_aplusb = list()
    for i in range(0, len(a)):
        d = dict(sorted(a[i].items(), key=lambda j: j[0]))
        sorted_aplusb.append(d)
    return sorted_aplusb


# # cautare valori cu aceiasi indici
# for linie in range(0, len(m)):
#     nr1 = 0
#     for tupla in range(0, len(m[linie]) - 1):
#         coloana = m[linie][tupla][1]
#         nr = 0
#         for tupla_urm in range(tupla + 1, len(m[linie])):
#             if m[linie][tupla_urm][1] == coloana:
#                 nr += 1
#         if nr > 0:
#             nr1 += 1
#     # print(nr1)
#
# # eliminare valori cu aceiasi indici
# for linie in range(0, len(m)):
#     for tupla in range(0, len(m[linie]) - 1):
#         coloana = m[linie][tupla][1]
#         for tupla_urm in range(tupla + 1, len(m[linie])):
#             if tupla_urm == len(m[linie]):
#                 break
#             if m[linie][tupla_urm][1] == coloana:
#                 y1 = list(m[linie][tupla])
#                 y2 = list(m[linie][tupla_urm])
#                 y1[0] += y2[0]
#                 m[linie][tupla] = tuple(y1)
#                 m[linie][tupla_urm] = tuple(y2)
#                 m[linie].remove((m[linie][tupla_urm][0], m[linie][tupla_urm][1]))
