import pandas as pd
import openpyxl
import random

pupil_list = {
    'Баюнц':'0',
    'Бурлака':'1',
    'Вердян':'2',
    'Виноградов':'3',
    'Волкова':'4',
    'Володин':'5',
    'Гостюхин':'6',
    'Гузиев':'7',
    'Жильцов':'8',
    'Игнальев':'9',
    'Исаев':'10',
    'Колмаков':'11',
    'Костырин':'12',
    'Лапшин':'13',
    'Лопатюк':'14',
    'Любин':'15',
    'Маилян':'16',
    'Машрабов':'17',
    'Ротарь':'18',
    'Тарасов':'19',
    'Толмачёв':'20',
    'Трифонов':'21',
    'Чулиев':'22',
}
pupil_list_back = {
    '0':'Баюнц',
    '1':'Бурлака',
    '2':'Вердян',
    '3':'Виноградов',
    '4':'Волкова',
    '5':'Володин',
    '6':'Гостюхин',
    '7':'Гузиев',
    '8':'Жильцов',
    '9':'Игнальев',
    '10':'Исаев',
    '11':'Колмаков',
    '12':'Костырин',
    '13':'Лапшин',
    '14':'Лопатюк',
    '15':'Любин',
    '16':'Маилян',
    '17':'Машрабов',
    '18':'Ротарь',
    '19':'Тарасов',
    '20':'Толмачёв',
    '21':'Трифонов',
    '22':'Чулиев',
}
main_df = pd.read_excel('main.xlsx')
pupil_surnames = main_df.loc[0:22,'surname']
pupil_surnames = list(pupil_surnames)
print(pupil_surnames)
sick_list = main_df.loc[0:22,'is_sick']
sick_list = list(sick_list)
now_sick = []
pupil_sick = []
for i in range(len(pupil_surnames)):
    if sick_list[i] == 1:
        now_sick.append(i) #Получаем порядковый номер больных
for i in range(len(now_sick)):
    number = now_sick[i]
    pupil_sick.append(pupil_list_back[str(number)])
print(pupil_sick)


def check_sick(pupil_surname):
    if pupil_surname in pupil_sick:
        return True
    else: False

pers = random.randint(0,22)
pers = pupil_list_back[str(pers)]
print(pers)
print('Чекаем Гришаню')
print(check_sick('Бурлака'))