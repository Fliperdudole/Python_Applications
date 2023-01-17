import PySimpleGUI as sg

layout = [
    [sg.Input(key = "-INPUT-"), sg.Spin(["km to mile", "kg to pound"]), sg.Button("Convert")],

    [sg.Text("Output:"), sg.Text(" ", enable_events= True, key="-OUTPUT-")]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Convert":
        print("Test")
    


window.close()