import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = "-INPUT-"), 
        sg.Spin(["km to mile", "kg to pound", "sec to min"], key = '-UNITS-'), 
        sg.Button("Convert", key = "-CONVERT-")
    ],

    [
        sg.Text("Output:"), sg.Text(" ", enable_events= True, key="-OUTPUT-")
    ]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_value = values['-INPUT-']
        
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value)) * 0.6214
                    output_string = f'{input_value} kilometers -> {output} miles'
                    window['-OUTPUT-'].update(output_string)
                
                case 'kg to pound':
                    output = round(float(input_value)) * 2.20462
                    output_string = f'{input_value} kilograms -> {output} pounds'
                    window['-OUTPUT-'].update(output_string)
                
                case 'sec to min':
                    output = round(float(input_value)) / 60
                    output_string = f'{input_value} seconds -> {output} mins'
                    window['-OUTPUT-'].update(output_string)



        
        else:
            print("Enter a number!")

        
    


window.close()