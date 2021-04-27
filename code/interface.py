import PySimpleGUI as sg
import os
from subprocess import call
import random
from PIL import Image, ImageGrab, ImageDraw

layout = [
    [sg.Text('Ширина'),sg.Input(key = 'height'), sg.Text('Высота'), sg.Input(key = 'width')],
    [sg.Text('Введите название картинки'), sg.Input(key = 'kartinka')],
    [sg.Text('Задайте путь. Там будет сохранена картинка')],
    [sg.Input(), sg.FolderBrowse('Поиск')],
    [sg.Button('Отправить')],
    [sg.Button('Сгенерировать'), sg.Button('Открыть картинку')],
    [sg.Button('Закрыть')]
]

window = sg.Window('Лабиринт', layout)
while True:
    event, values = window.read()
    p = os.getcwd()
    print('FolderBrowse:', values['Поиск'])
    f = open('utility.txt','w')
    if values['kartinka'] == '.':
        values['kartinka'] = 'picture'
    f.write(values['Поиск'] + '\n' + values['height'] + '\n' + values['width'] + '\n' + values['kartinka']+ '\n' + p)
    f.close()

    if event is None or event == 'Закрыть':
        break

    if event == 'Отправить':
        foldername = values['Поиск'] or p


        print('folder:', foldername)


    if event == 'Сгенерировать':
        call(["python", "Lab.py"])
    if event == 'Открыть картинку':
        with open('utility.txt') as f:
            s = f.readlines()
        filepath = ''.join(s[0:1]).rstrip()
        if not filepath:
            filepath = p
        s1 =''.join(s[3:4]).rstrip()
        
        filepath1 = filepath + '//' + s1 + '.png'
        print(filepath1)
        print(p)
        os.startfile(filepath1)
window.close()
