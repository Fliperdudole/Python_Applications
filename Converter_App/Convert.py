import PySimpleGUI as sg

layout = [
    [sg.Text("Text"), sg.Spin(['Kilometers','Meters'])],
    [sg.Button("Convert")],
    [sg.Input()],
    [sg.Text("Test Button"), sg.Button("Test Button")]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()