import numpy
import methods
import PySimpleGUI as sg


def bulina_inferface(flag, A, L, LT, det_A, x_Chol, norma_obtinuta):
    message1 = "Matricea initiala: " + str(A)
    message2 = "Matricea inferior triunghiulara: " + str(L)
    message3 = "Matricea superior triunghiulara: " + str(LT)
    message4 = "Determinant matrice: " + str(det_A)
    message5 = "Solutia aproximativa a ecuatiei: " + str(x_Chol)
    message6 = "Norma pe baza solutiei: " + str(norma_obtinuta)
    if flag == 1:
        preparation_message = "Rezultatele functiilor implementate: "
        sg.theme('DarkAmber')
        layout = [[sg.Text(preparation_message, justification='center')], [sg.Text(message1, justification='center')],
                  [sg.Text(message2, justification='center')], [sg.Text(message3, justification='center')],
                  [sg.Text(message4, justification='center')],
                  [sg.Text(message5, justification='center')],
                  [sg.Text(message6, justification='center')],
                  [sg.Button("Close")]]

        # Create the window
        window = sg.Window("Interface buline 1-4", layout, size=(1100, 400))
        # Create an event loop
        while True:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button
            if event == "Close" or event == sg.WIN_CLOSED:
                break
        window.close()
    else:
        preparation_message = "Rezultatele functiilor din bibiloteca: "
        sg.theme('DarkAmber')
        message6 = ""
        layout = [[sg.Text(preparation_message, justification='center')], [sg.Text(message1, justification='center')],
                  [sg.Text(message2, justification='center')], [sg.Text(message3, justification='center')],
                  [sg.Text(message4, justification='center')],
                  [sg.Text(message5, justification='center')],
                  [sg.Text(message6, justification='center')],
                  [sg.Button("Close")]]

        # Create the window
        window = sg.Window("Interface buline 5-6", layout, size=(600, 400))
        # Create an event loop
        while True:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button
            if event == "Close" or event == sg.WIN_CLOSED:
                break
        window.close()
    print("========================================")


def bulina6_interface(inversa_chol, inversa_biblo, norma):
    message1 = "Inversa Chol: " + str(inversa_chol)
    message2 = "Inversa Bibliotecii: " + str(inversa_biblo)
    message3 = "Norma inverselor: " + str(norma)
    preparation_message = "Rezultat functie implementata vs Rezultat biblioteca: "
    sg.theme('DarkAmber')
    layout = [[sg.Text(preparation_message, justification='center')], [sg.Text(message1, justification='center')],
              [sg.Text(message2, justification='center')], [sg.Text(message3, justification='center')],
              [sg.Button("Close")]]

    # Create the window
    window = sg.Window("Interface buline 1-4", layout, size=(600, 400))
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    window.close()


def automat(n):
    print("\n Se genereaza valori automat... \n")
    n = n
    A = numpy.random.randint(0, 30, size=(n, n))
    b = numpy.random.randint(10, size=n)
    A_T = numpy.transpose(A)

    while True:
        if numpy.linalg.det(A) > 0 and methods.isSymmetric(A, n):
            break
        else:
            A = numpy.random.randint(0, 30, size=(n, n))
            A_T = numpy.transpose(A)

    print("det(A): ", numpy.linalg.det(A))
    print("A e simetrica? ", methods.isSymmetric(A, n))
    print("AT: ", A_T)
    return A, b, n


def keyboard_input():
    n = int(input("Enter size: "))
    print("Enter the matrix elements: ")
    A = []
    b = []
    # For user input
    for i in range(n):  # randuri
        a = []
        for j in range(n):  # coloane
            a.append(int(input()))
        A.append(a)
    print("Enter the b elements: ")
    for i in range(n):  # coloane
        b.append(int(input()))
    return A, b, n


def file_input():
    print("File format accepted n,A,b")
    filename = str(input("Enter filename: "))
    A = []
    b = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        for i in range(1, n + 1):
            A.append([int(x) for x in lines[i].split(',')])
        b = [int(x) for x in lines[n + 1].split(',')]
    return A, b, n


if __name__ == '__main__':
    # bulina7
    print("Choices: ")
    print("0 -> foloseste un set de date predefinit")
    print("1 -> genereaza date automat")
    print("2 -> introdu date de la tastatura")
    print("3 -> foloseste datele dintr-un fisier")
    choice = int(input("\n Enter a choice: "))
    if choice == 1:
        # generare automata
        result = automat(3)
        A = result[0]
        b = result[1]
        n = result[2]
    elif choice == 2:
        # tastatura
        result = keyboard_input()
        A = result[0]
        b = result[1]
        n = result[2]
    elif choice == 3:
        # fisier
        result = file_input()
        A = result[0]
        b = result[1]
        n = result[2]
    else:
        # raman variabilele predefinite
        epsilon = 10 ** (-10)  # float(sym.expand(input("Enter epsilon: ")))  # Precizia calculelor
        n = 3  # int(input("Enter n: "))  # Dimensiunea sistemului
        A = [[4, 2, 8],
             [2, 10, 10],
             [8, 10, 21]]
        A_init = [[4, 2, 8],
                  [2, 10, 10],
                  [8, 10, 21]]
        b = [12, 6, 3]
        b_init = [12, 6, 3]

    A_init = A
    b_init = b
    print("A: ", A)
    print("b: ", b, "\n")

    # Vectorul ce contine diagonala principala din A
    d = methods.diag_principala(A, n)
    AUX = A
    for i in range(len(A)):
        AUX[i][i] = numpy.float64(A[i][i])
    A = AUX

    # bulina1
    # Descompunerea LLT (descompunerea/factorizarea Cholesky)
    if numpy.linalg.det(A) > 0 and methods.isSymmetric(A, n):
        L = methods.fill_with_zeros(n)
        for j in range(0, n):
            for i in range(0, n):
                if i == j:
                    L[i][j] = numpy.float64(methods.calcul_elem_diagonal(i, L, A))
                    if L[i][j] == 0:
                        print("Matricea A nu poate fi descompusa! L nu poate fi calculat!")
                        break
                elif j < i:
                    L[i][j] = numpy.float64(methods.calcul_restul_elem(i, j, L, A))
        LT = numpy.transpose(L)
        print("L: ", L)
        print("LT: ", LT)

        # bulina2
        # Calcularea determinantului matricii A (det A = det L * det LT = det L ** 2)
        det_A = methods.calcul_determinant(L, n)
        print("det(A): ", det_A)

        # bulina3
        # Solutiile aproximative a sistemului Ax = b
        y_Chol = methods.calcul_x_Chol_substitutia_directa(L, b, n)
        x_Chol = methods.calcul_x_Chol_substitutia_inversa(LT, y_Chol, n)
        print("Solutia sistemului : ", x_Chol)

        # bulina4
        # Calculul normei pentru solutie bulina3
        norma_obtinuta = methods.calcul_norma(A_init, x_Chol, b_init)
        print("Norma pentru x_Chol1 : ", norma_obtinuta)
        # GUI
        bulina_inferface(1, A, L, LT, det_A, x_Chol, norma_obtinuta)

        # bulina5
        # descompunerea Cholesky si calcul x_Chol cu numpy
        L_numpy = numpy.linalg.cholesky(A_init)
        LT_numpy = numpy.transpose(L_numpy)
        x_Chol_numpy = numpy.linalg.solve(A, b)
        det_A_numpy = numpy.linalg.det(A)
        print("Descompunerea Cholesky lib")
        print("L :", L_numpy)
        print("LT :", LT_numpy)
        print("Solutia Cholesky :", x_Chol_numpy)
        print("Norma ", methods.calcul_norma(A_init, x_Chol_numpy, b_init))

        # bulina6
        inversa_chol = methods.inversa(n, L, LT)
        inversa_biblo = numpy.linalg.inv(A)
        norma_inverse = numpy.linalg.norm(inversa_chol - inversa_biblo)
        print("Inversa Chol : ", inversa_chol)
        print("Inversa Biblio : ", inversa_biblo)
        print("Norma inverselor : ", norma_inverse)
        # GUI
        bulina_inferface(2, A_init, L_numpy, LT_numpy, det_A_numpy, x_Chol_numpy, None)
        bulina6_interface(inversa_chol, inversa_biblo, norma_inverse)
    else:
        print("Matricea introdusa NU este pozitiv definita sau simetrica!!!")
