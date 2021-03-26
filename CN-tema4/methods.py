import math
import numpy
import PySimpleGUI as sg

epsilon = 10 ** (-13)


def create_empty_list_of_dicts(n):
    return [{} for i in range(0, n)]


def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        p = int(lines[1])
        q = int(lines[2])
        a = list()
        for i in range(4, n + 4):
            a.append(float(lines[i][:-1]))
        c = list()
        for i in range(n + 5, n + 5 + n - p):
            c.append(float(lines[i][:-1]))
        b = list()
        for i in range(n + 5 + n - p + 1, n + 5 + n - p + 1 + n - q):
            b.append(float(lines[i][:-1]))
    matrix = list()
    matrix.append(a)
    matrix.append(b)
    matrix.append(c)
    return n, q, p, matrix


def convert_vectors_in_sparse_matrix_list(a, b, c, n, q, p):
    matrix = create_empty_list_of_dicts(n)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j:
                matrix[i][j] = a[i]
            if j - i == q:
                matrix[i][j] = b[i]
            if i - j == p:
                matrix[i][j] = c[j]
    return matrix


def read_vector_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = list()
        for i in range(2, n + 2):
            a.append(float(lines[i]))
    return a

def read_vector_norm(filename):
    a=list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(0, 5):
            a.append(float(lines[i]))
    return a
def check_diagonala(a):
    for i in range(len(a)):
        if abs(a[i]) < epsilon:
            return "STOP"
    return "GO"


def verificare_posibilitate_calul(matrix):
    verificare = list()
    verificare.append(check_diagonala(matrix[0]))
    if "STOP" in verificare:
        print("Nu se poate calcula solutia! Diagonala cu elemente zero...")
        exit()
    else:
        return


def fill_with_zeros(n):
    return [0.0 for j in range(n)]


def calcul_norma(a, x, f, n):
    x = numpy.array(x)
    b = fill_with_zeros(n)
    # calculam b = a * x
    for i in range(len(a)):
        suma = 0
        for k in a[i].keys():
            suma += a[i][k] * x[k]
        b[i] = suma
    print("A * x ~= f:", "\n", b)
    # calculam z = b - f
    z = numpy.array(numpy.subtract(b, f))
    return numpy.linalg.norm(z, numpy.inf)


def gauss_seidel(a, f, n, p, q):
    # initiere vector x
    x = [0.0] * n
    delta_x = 1
    epsilon = 10 ** (-13)
    k_max = 10000
    k = 0

    # conditiile de terminare
    while (k <= k_max) and (delta_x >= epsilon) and (delta_x <= 10 ** 13):
        elem_diag = 1.0

        for i in range(0, n):
            suma1 = 0.0
            suma2 = 0.0

            # calcularea sumelor necesare pe baza formulei
            for j in a[i].keys():
                if j == i - p:
                    suma1 += x[j] * a[i][j]
                elif j == i + q:
                    suma2 += a[i][j] * x[j]
                if j == i:
                    elem_diag = a[i][j]

            x_curent = (f[i] - suma1 - suma2) / elem_diag
            x_anterior = x[i]

            # calcul norma
            norma = pow(x_curent - x_anterior, 2)
            delta_x = math.sqrt(norma)

            x[i] = abs(x_curent)
            k += 1
    return x


def write_solution_to_file(filename, x):
    file = open(filename, "w")
    for item in x:
        file.write("%s\n" % item)
    file.close()
    print("\nSolutia ", filename, " a fost memorata\n")
    return


def gui_interface_norme(solutii):
    sg.theme('DarkPurple')
    message = "Normele solutiilor obtinute : \n"
    message0 = "Solutia 1 : "
    message1 = "Solutia 2 : "
    message2 = "Solutia 3 : "
    message3 = "Solutia 4 : "
    message4 = "Solutia 5 : "

    layout = [[sg.Text(message, justification='center')],
              [sg.Text(message0, justification='center')],
              [sg.Multiline(size=(105, 2), default_text=str(solutii[0]), font='courier 10', background_color='black',
                            text_color='white')],
              [sg.Text(message1, justification='center')],
              [sg.Multiline(size=(105, 2), default_text=str(solutii[1]), font='courier 10', background_color='black',
                            text_color='white')],
              [sg.Text(message2, justification='center')],
              [sg.Multiline(size=(105, 2), default_text=str(solutii[2]), font='courier 10', background_color='black',
                            text_color='white')],
              [sg.Text(message3, justification='center')],
              [sg.Multiline(size=(105, 2), default_text=str(solutii[3]), font='courier 10', background_color='black',
                            text_color='white')],
              [sg.Text(message4, justification='center')],
              [sg.Multiline(size=(105, 2), default_text=str(solutii[4]), font='courier 10', background_color='black',
                            text_color='white')],
              [sg.Button("Close")]]

    # Create the window
    window = sg.Window("Tema 4 - CN", layout, size=(800, 600))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    layout.clear()
    window.close()


def gui_interface_bonus(solutie, norma):
    sg.theme('DarkPurple')
    message = "Solutie bounus"
    message0 = "Normele solutiei obtinute : \n"

    layout = [[sg.Text(message, justification='center')],
              [sg.Multiline(size=(105, 2), default_text=str(solutie), font='courier 10', background_color='black',
                            text_color='white')],
              [sg.Text(message0, justification='center')],
              [sg.Multiline(size=(105, 2), default_text=str(norma), font='courier 10', background_color='black',
                            text_color='white')],
              [sg.Button("Close")]]

    # Create the window
    window = sg.Window("Tema 4 - Bonus", layout, size=(800, 300))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    layout.clear()
    window.close()
