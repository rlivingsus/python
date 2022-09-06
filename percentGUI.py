#!/usr/bin/python3
# percentGUI.py

import PySimpleGUI as sg

def main():


    left_column = [
        [sg.Text("Initial Value"),
            sg.Input(size=(14,1), enable_events=True, key="-IVALUE-")],
        [sg.Text("End Value"),
            sg.Input(size=(14,1), enable_events=True, key="-EVALUE-")],
        [sg.Text(size=(25,1), key="-OUTPUT-")],
        [sg.Button("Compute %")]
    ]

    right_column = [
        [sg.Button("Exit")]
    ]

    #layout
    layout = [
        [sg.Column(left_column),
            sg.VSeperator(),
            sg.Col(right_column)]
    ]

    #create the window
    window = sg.Window("% value changed calculator", layout)

    #event loop
    while True:
        event, values = window.read()
        #end the program if user closes window or
        #presses Exit button only
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        #if the 'Compute %' button is pressed
        if event == "Compute %":
            try:
                num1 = float(values["-IVALUE-"])
                num2 = float(values["-EVALUE-"])
                num3 = (((num2 - num1)/num1)*100)
                string1 = f'{num3:.2f}'
                window["-OUTPUT-"].update("% changed is " + string1)
            except ValueError:
                #sg.popup("Warning", "Wrong format for a float number !", elem=window["-OUTPUT-"])
                sg.popup("Warning", "Wrong format for a float number !", window["-OUTPUT-"])

    window.close()

if __name__ == '__main__':
    main()
