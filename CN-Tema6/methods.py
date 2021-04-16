import numpy
import PySimpleGUI as gui


def horner_method(polinom, x):
    rezultat = polinom[0]
    for i in range(1, len(polinom)):
        rezultat = rezultat * numpy.float64(x) + polinom[i]
    return rezultat


def metoda_celor_mai_mici_patrate(x_barat, x, y, n, m):
    """
    Interpolare prin metoda celor mai mici patrate.
    """
    # rezolvarea sistemului liniar B*a = f

    B = [[0 for i in range(m + 1)] for j in range(m + 1)]
    for j in range(m + 1):
        for i in range(m + 1):
            suma = 0
            for k in range(n + 1):
                B[i][j] += x[k] ** (i + j)

    f = [0 for i in range(m + 1)]
    for i in range(m + 1):
        suma = 0
        for k in range(n + 1):
            suma += (x[k] ** i) * y[k]
        f[i] = suma
    # print("B:", B, B[0][0], "\n")
    # B = numpy.array(B)
    # f = numpy.array(f)
    # B = numpy.array([[sum([x[k] ** (i + j) for k in range(n+1)])
    #             for j in range(0, m + 1)]
    #             for i in range(0, m + 1)])
    # f = numpy.array([sum([y[k] * (x[k] ** i) for k in range(n+1)])
    #         for i in range(0, m + 1)])
    a = numpy.linalg.solve(B, f)
    # print(numpy.allclose(numpy.dot(B, a), f))
    # a = numpy.array(a)

    # print("B:", B)
    # print("a:", a, a[0])
    # print("f:", f)

    f_de_x_barat = horner_method(a, x_barat)
    return f_de_x_barat


def spline_patratice(x_barat, f_derivat_de_a, x, y, n):
    h = [0 for i in range(n+1)]
    A = [0 for i in range(n+1)]
    A[0] = f_derivat_de_a
    for i in range(n):
        h[i] = x[i+1] - x[i]
        A[i+1] = -A[i] + (2 * (y[i+1] - y[i])) / h[i]
    for i in range(n):
        if x[i] < x_barat < x[i+1]:
            S_de_x_barat = (A[i+1] - A[i]) / (2 * h[i]) * ((x_barat - x[i]) ** 2) + A[i] * (x_barat - x[i]) + y[i]
            return S_de_x_barat

def start_interface(text_ex="", message=""):
    gui.theme('DarkAmber')
    layout = [[gui.Text("Enter values for a,b,n")],
              [gui.Text("!!! a must be smaller than b !!!")],
              [gui.Text('Enter a ', size=(15, 1)), gui.InputText()],
              [gui.Text('Enter b', size=(15, 1)), gui.InputText()],
              [gui.Text('Enter n', size=(15, 1)), gui.InputText()],
              [gui.Button("Submit"), gui.Button("Close")]]

    # Create the window
    window = gui.Window(text_ex, layout, size=(650, 300))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == gui.WIN_CLOSED:
            break
        if event == "Submit":
            break
    layout.clear()
    window.close()
    return int(values[0]), int(values[1]), int(values[2])

def initial_set_up(text_ex="",message="", value_x=[], value_y=[], x_barat=0.0):
    gui.theme('DarkAmber')
    layout = [[gui.Text(message, justification='center')],
              [gui.Text("x : " + str(value_x), justification='center')],
              [gui.Text("y : " + str(value_y), justification='center')],
              [gui.Text("x_barat : " + str(x_barat), justification='center')],
              [gui.Button("Close")]]

    # Create the window
    window = gui.Window(text_ex, layout, size=(650, 300))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == gui.WIN_CLOSED:
            break
    layout.clear()
    window.close()

def cerinta_i(text_ex="", message="",message1="", aproximarea="",message2="", f_value="",message3="", dif="",message4="", sum=""):
        gui.theme('DarkAmber')
        layout = [[gui.Text(message, justification='center')],
                  [gui.Text(message1 + str(aproximarea), justification='center')],
                  [gui.Text(message2 + str(f_value), justification='center')],
                  [gui.Text(message3 + str(dif), justification='center')],
                  [gui.Text(message4 +str(sum), justification='center')],
                  [gui.Button("Close")]]

        # Create the window
        window = gui.Window(text_ex, layout, size=(650, 300))

        # Create an event loop
        while True:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button
            if event == "Close" or event == gui.WIN_CLOSED:
                break
        layout.clear()
        window.close()