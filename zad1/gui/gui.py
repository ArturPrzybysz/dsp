import PySimpleGUI as sg
from zad1.gui.signals_from_gui import create_signals

def showGui():
    layout = [
        [sg.Text('(S1) szum o rozkładzie jednostajnym')],
        [sg.Text('(S2) szum gaussowski')],
        [sg.Text('(S3) sygnał sinusoidalny')],
        [sg.Text('(S4) sygnał sinusoidalny wyprostowany jednopołówkowo')],
        [sg.Text('(S5) sygnał sinusoidalny wyprostowany dwupołówkowo')],
        [sg.Text('(S6) sygnał prostokątny')],
        [sg.Text('(S7) sygnał prostokątny symetryczny')],
        [sg.Text('(S8) sygnał trójkątny')],
        [sg.Text('(S9) skok jednostkowy')],
        [sg.Text('(S10) impuls jednostkowy')],
        [sg.Text('(S11) szum impulsowy')],
        [sg.Text('1'),
         sg.Combo(['S1', 'S2', 'S3', 'S4', 'S5', 'S6',
                   'S7', 'S8', 'S9', 'S10', 'S11'], size=(10, 11)),
         sg.Text('operation'),
         sg.Combo(['+', '-', '*', '/'], size=(5, 4)),
         sg.Text('2'),
         sg.Combo(['S1', 'S2', 'S3', 'S4', 'S5', 'S6',
                   'S7', 'S8', 'S9', 'S10', 'S11'], size=(10, 11))],

        [sg.Text('sampleRate'), sg.InputText()],
        [sg.Text('duration'), sg.InputText()],
        [sg.Text('1 low', size=(10,1)),  sg.InputText(),
         sg.Text('2 low', size=(10,1)), sg.InputText()],
        [sg.Text('1 high', size=(10,1)), sg.InputText(),
         sg.Text('2 high', size=(10,1)), sg.InputText()],
        [sg.Text('1 mean', size=(10,1)), sg.InputText(),
         sg.Text('2 mean', size=(10,1)), sg.InputText()],
        [sg.Text('1 variance', size=(10,1)), sg.InputText(),
         sg.Text('2 variance', size=(10,1)), sg.InputText()],
        [sg.Text('1 amp', size=(10, 1)), sg.InputText(),
         sg.Text('2 amp', size=(10, 1)), sg.InputText()],
        [sg.Text('1 T', size=(10, 1)), sg.InputText(),
         sg.Text('2 T', size=(10, 1)), sg.InputText()],
        [sg.Text('1 t0', size=(10, 1)), sg.InputText(),
         sg.Text('2 t0', size=(10, 1)), sg.InputText()],
        [sg.Text('1 kw', size=(10, 1)), sg.InputText(),
         sg.Text('2 kw', size=(10, 1)), sg.InputText()],
        [sg.Text('1 ts', size=(10, 1)), sg.InputText(),
         sg.Text('2 ts', size=(10, 1)), sg.InputText()],
        [sg.Text('1 occurenceP', size=(10, 1)), sg.InputText(),
         sg.Text('2 occurenceP', size=(10, 1)), sg.InputText()],
        [sg.Text('Histogram interval', size=(15, 1)),
            sg.Slider(range=(1, 50), orientation='h', size=(15, 20), default_value=50)],
        [sg.Checkbox('First'),
         sg.Checkbox('Second'),
         sg.Checkbox('Result')],

        [sg.Button('OK', button_color=('white', 'green')),
         sg.Cancel()]]

    window = sg.Window('Z1', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    button, values = window.Read()
    if button:
        create_signals(values)



