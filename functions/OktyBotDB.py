import os
import pandas as pd
import openpyxl
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MAIN_PATH = os.environ.get("MAIN_PATH")
COUPLES_PATH = os.environ.get("COUPLES_PATH")
BLACKLIST_PATH = os.environ.get("BLACKLIST_PATH")

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
    'Игнатьев':'9',
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
    '9':'Игнатьев',
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

main_df = pd.read_excel(MAIN_PATH)

pupil_count_duty = main_df.loc[0:22,'count_duty']
pupil_count_duty = list(pupil_count_duty)

disbat = main_df.loc[0:22,'dizbat']
disbat = list(disbat)

pupil_surnames = main_df.loc[0:22,'surname']
pupil_surnames = list(pupil_surnames)

sick_list = main_df.loc[0:22,'is_sick']
sick_list = list(sick_list)

def check_sick():
    now_sick = []
    pupil_sick = []
    for i in range(len(pupil_surnames)):
        if sick_list[i] == 1:
            now_sick.append(i) #Получаем порядковый номер больных
    for i in range(len(now_sick)):
        number = now_sick[i]
        pupil_sick.append(pupil_list_back[str(number)])
    return pupil_sick

def check_position():
    middle_num = 0
    for i in range(22):
        num = int(pupil_count_duty[i])
        middle_num += num
    middle_num /= 22
    return middle_num


