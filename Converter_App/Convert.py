import PySimpleGUI as sg

layout = [
    [sg.Text("Text"), sg.Spin(['Kilometers','Meters'])],

    [sg.Button("Convert", key = "-BUTTON1-")],

    [sg.Input()],
    
    [sg.Text("Test Button"), sg.Button("Button", key = "-BUTTON2-")]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-BUTTON1-":
        print("Button Pressed")

    if event == "-BUTTON2-":
        print("Test Button Pressed")


window.close()