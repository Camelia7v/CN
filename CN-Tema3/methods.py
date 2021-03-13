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
        print("\n", "Matricele NU sunt egale!", "\n")
    else:
        print("\n", "Matricele sunt egale!", "\n")


def sort_matrix(a):
    sorted_aplusb = list()
    for i in range(0, len(a)):
        d = dict(sorted(a[i].items(), key=lambda j: j[0]))
        sorted_aplusb.append(d)
    return sorted_aplusb
