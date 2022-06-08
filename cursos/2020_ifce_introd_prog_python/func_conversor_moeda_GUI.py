import PySimpleGUI as sg

sg.theme("Topanga")

layout = [
    [sg.Text("Digite a cotação do dólar $: "), sg.Input(key="dolar", do_not_clear=False, size=(10,1))],
    [sg.Text("Digite o valor em real R$: "), sg.Input(key="real", do_not_clear=False, size=(10,1))],
    [sg.Text("Valor a receber em dólar: "), sg.Text(size=(10,1), key="conversao")],
    [sg.Button("Converter", bind_return_key=True), sg.Button("Sair")]
]

window = sg.Window("Conversão de moedas", layout)
while True:
    event, values = window.read()
    if event in (None, "Sair"):
        break    
    window["conversao"].Update(float(values["real"])/float(values["dolar"]))
window.close()