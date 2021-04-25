import PySimpleGUI as sg
import os
from subprocess import call

#help(sg.FolderBrowse)
#help(sg.FileBrowse)

layout = [
    [sg.Text('Введите в левом поле значение высоты лабиринта, в правом - значение ширины. Выберите путь, в котором будет сохранен файл с картинкой')],
    [sg.Input(key = 'height'), sg.Input(key = 'width')],
    [sg.Input(), sg.FolderBrowse('FolderBrowse')],
    [sg.Submit(), sg.Cancel()],
    [sg.Button('Сгенерировать'), sg.Button('Открыть картинку')]
]

window = sg.Window('Test', layout)
while True:
    event, values = window.read()
    #print('event:', event)
    #print('values:', values)
    print('FolderBrowse:', values['FolderBrowse'])
    f = open('utility.txt','w')
    f.write(values['FolderBrowse'] + '\n' + values['height'] + '\n' + values['width'] + '\n')
    f.close()

    if event is None or event == 'Cancel':
        break

    if event == 'Submit':
        foldername = values['FolderBrowse'] or '.'


        print('folder:', foldername)

    if event == 'Сгенерировать':
        call(["python", "Lab.py"])
    if event == 'Открыть картинку':
        with open('utility.txt') as f:
            s = f.readlines()
        filepath = ''.join(s[0:1]).rstrip()
        s1 = "/PILImage.png"
        filepath = filepath + s1
        print(filepath)
        os.startfile(filepath)
window.close()
