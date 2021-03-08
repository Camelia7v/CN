"""
CN-Tema1
grupa 3A5
Lupancu Viorica-Camelia
Potoroaca Ana-Maria
"""

import math
import random
import numpy as np
import time
import methods
import PySimpleGUI as sg


def calcul_u():
    for i in range(1000, 0, -1):
        u = pow(10, -i)
        if 1.0 + u != 1.0:
            return u


def ex2_plus():
    u = calcul_u()
    a = 1.0
    b = u / 10
    c = u / 10

    z = a + b
    x = b + c
    if z + c != a + x:
        print("Operatia + nu este asociativa")
        print("==========================================")
        message = "Valorile utilizate pentru a demostra inegalitatea (a+b)+c!=a+(b+c) sunt\n"
        message = message + "a = " + str(a) + "\n" + "b = " + str(b) + "\n" + "c = " + str(c) + "\n"
        value = "Dupa calculare, valorile adunarilor sunt " + str(z + c) + "!=" + str(a + x)
        conlusion = "Operatia + nu este asociativa"
        sg.theme('DarkAmber')
        layout = [[sg.Text(message, justification='center')], [sg.Text(value, justification='center')],
                  [sg.Text(conlusion, justification='center')], [sg.Button("Close")]]

        # Create the window
        window = sg.Window("Interface exercitiu 2a", layout, size=(600, 400))

        # Create an event loop
        while True:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button
            if event == "Close" or event == sg.WIN_CLOSED:
                break
        window.close()
        return
    else:
        print("Operatia + este asociativa")


def ex2_inm():
    u = calcul_u()
    a = random.uniform(1.5, 1.9)
    b = u / random.uniform(1.5, 1.9)
    c = u / random.uniform(1.5, 1.9)
    z = a * b
    x = b * c
    count = 0
    while z * c == a * x:
        a = random.uniform(1.5, 1.9)
        b = u / random.uniform(1.5, 1.9)
        c = u / random.uniform(1.5, 1.9)
        z = a * b
        x = b * c
        count = count + 1
        print(count)
    print("Values of a,b,c : ", a, b, c)
    print(z * c, "!=", a * x)
    print("Operatia x nu este asociativa")
    print("==========================================")

    message = "Valorile utilizate pentru a demostra inegalitatea (axb)xc!=ax(bxc) sunt\n"
    message = message + "a = " + str(a) + "\n" + "b = " + str(b) + "\n" + "c = " + str(c) + "\n"
    value = "Dupa calculare, valorile inmultirilor sunt " + str(z + c) + "!=" + str(a + x)
    conlusion = "Operatia x nu este asociativa. Numarul de incercari pana la gasirea valorilor a fost de " + str(count)
    sg.theme('DarkAmber')
    layout = [[sg.Text(message, justification='center')], [sg.Text(value, justification='center')],
              [sg.Text(conlusion, justification='center')], [sg.Button("Close")]]

    # Create the window
    window = sg.Window("Interface exercitiu 2b", layout, size=(600, 400))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    window.close()
    return


def gui_interface_ex1(param):
    message = "Valoare precizia masina reprezinta cel mai mic numar pozitiv u > 0, de forma u = 10^(-m)"
    value = "Dupa calculare, coeficentul m are valaore 15, iar valoare obtinuta pentru u este " + str(param)
    sg.theme('DarkAmber')
    layout = [[sg.Text(message, justification='center')], [sg.Text(value, justification='center')],
              [sg.Button("Close")]]

    # Create the window
    window = sg.Window("Interface exercitiu 1", layout, size=(600, 400))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    window.close()


def ex3():
    epsilon = 10 ** (-13)

    print("Rezultatele pentru pi/3:")
    print("->tan standard:          ", math.tan(math.pi / 3))
    print("->my_tan1:               ", methods.lentz_algorithm(math.pi / 3, epsilon))
    print("->my_tan2 fara reducere: ", methods.maclaurin_approximation(math.pi / 3))
    print("->my_tan2  cu  reducere: ", methods.reducere_tan(math.pi / 3, methods.maclaurin_approximation), "\n")

    generated_numbers = []
    my_tan1_values = []
    my_tan2_values = []
    standard_tan_values = []
    errors1 = []
    errors2 = []
    errors3 = []
    preparation_message = ""
    message1 = "Valorile comparatie dintre my_tan1 si tan standard"
    message2 = "Valorile comparatie dintre my_tan2 si tan standard"
    message3 = "Valorile comparatie dintre my_tan1 si my_tan2"
    for i in range(1, 10001):
        preparation_message = "Se genereaza random cele 10000 de valori...."
        x = random.uniform(- math.pi / 2, math.pi / 2)
        generated_numbers.append(x)
        preparation_message = preparation_message + "\nValorile au fost generate"

    preparation_message += "\nCalcularea functiilor pentru fiecare valoare in parte...."

    start_time = time.time()
    for x in generated_numbers:
        standard_tan = math.tan(x)
        standard_tan_values.append(standard_tan)
    run_time1 = time.time() - start_time

    start_time = time.time()
    for x in generated_numbers:
        my_tan1 = methods.lentz_algorithm(x, epsilon)
        my_tan1_values.append(my_tan1)
    run_time2 = time.time() - start_time

    start_time = time.time()
    for x in generated_numbers:
        my_tan2 = methods.reducere_tan(x, methods.maclaurin_approximation)
        my_tan2_values.append(my_tan2)
    run_time3 = time.time() - start_time

    # my_tan1 and standard_tan
    for i in range(0, len(generated_numbers) - 1):
        err1 = abs(standard_tan_values[i] - my_tan1_values[i])
        errors1.append(err1)

    # my_tan2 and standard_tan
    for i in range(0, len(generated_numbers) - 1):
        err2 = abs(standard_tan_values[i] - my_tan2_values[i])
        errors2.append(err2)

    # my_tan1 and my_tan2
    for i in range(0, len(generated_numbers) - 1):
        err3 = abs(my_tan1_values[i] - my_tan2_values[i])
        errors3.append(err3)

    # mediile erorilor pentru fiecare comparatie
    err_avg1 = np.mean(errors1)
    err_avg2 = np.mean(errors2)
    err_avg3 = np.mean(errors3)

    preparation_message += "\nTimpii de executie : \n" + "->tan standard : " + str(run_time1)
    preparation_message += "\n->my_tan1 : " + str(run_time2)
    preparation_message += "\n->my_tan2 : " + str(run_time3)

    message1 += "\nMedia erorilor este : " + str(err_avg1)
    message2 += "\nMedia erorilor este : " + str(err_avg2)
    message3 += "\nMedia erorilor este : " + str(err_avg3)

    ps_message = "Timpul de executie se refera la timpul de rulare a functiei pentru cele 10000 de valori"

    sg.theme('DarkAmber')
    layout = [[sg.Text(preparation_message, justification='center')], [sg.Text(message1, justification='center')],
              [sg.Text(message2, justification='center')], [sg.Text(message3, justification='center')],
              [sg.Text(ps_message, justification='center')],
              [sg.Button("Close")]]

    # Create the window
    window = sg.Window("Interface exercitiu 1", layout, size=(600, 400))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    window.close()
    print("==========================================")


if __name__ == '__main__':
    calcul_u()
    gui_interface_ex1(calcul_u())
    ex2_plus()
    ex2_inm()
    ex3()
