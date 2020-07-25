import PySimpleGUI as sg


layout = [
    [sg.Text('por favor insira seu nome e o e-mail')],
    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
    [sg.Text('e-mail', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]


window = sg.Window('Programa de teste', layout)
event, values = window.read()
window.close()
print(event, 'nome: ', values[0], ' e-mail: ', values[1])