import PySimpleGUI as sg


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
        mesaj="Matricele NU sunt egale!"
        print("\n", "Matricele NU sunt egale!", "\n")
    else:
        mesaj="Matricele SUNT egale!"
        print("\n", "Matricele sunt egale!", "\n")
    return mesaj


def sort_matrix(a):
    sorted_aplusb = list()
    for i in range(0, len(a)):
        d = dict(sorted(a[i].items(), key=lambda j: j[0]))
        sorted_aplusb.append(d)
    return sorted_aplusb


def gui_interface_citire(text_ex=None,message1=None,message2=None,value1=None,value2=None):
    sg.theme('DarkPurple')
    layout = [[sg.Text(message1, justification='center')],
              [sg.Multiline(size=(105, 10), default_text=str(value1),font='courier 10', background_color='black', text_color='white')],
              [sg.Text(message2, justification='center')],
              [sg.Multiline(size=(105, 5), default_text="Vector a:"+str(value2[0]),font='courier 10', background_color='black', text_color='white')],
              [sg.Multiline(size=(105, 5), default_text="Vector b:" + str(value2[1]), font='courier 10',
                            background_color='black', text_color='white')],
              [sg.Multiline(size=(105, 5), default_text="Vector c:" + str(value2[2]), font='courier 10',
                            background_color='black', text_color='white')],
              [sg.Button("Close")]]

    # Create the window
    window = sg.Window(text_ex, layout, size=(800, 600))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    window.close()

def gui_interface_operatii(text_ex=None,message1=None,message2=None,value1=None,value2=None,verificare=None):
    sg.theme('DarkPurple')
    layout = [[sg.Text(message1, justification='center')],
              [sg.Multiline(size=(105, 10), default_text=str(value1),font='courier 10', background_color='black', text_color='white')],
              [sg.Text(message2, justification='center')],
              [sg.Multiline(size=(105, 10), default_text=str(value2), font='courier 10', background_color='black',
                            text_color='white')],
              [sg.Text(verificare, justification='center')],
              [sg.Button("Close")]]

    # Create the window
    window = sg.Window(text_ex, layout, size=(800, 600))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    layout.clear()
    window.close()