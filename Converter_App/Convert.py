import PySimpleGUI as sg

layout = [[]]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break



window.close()