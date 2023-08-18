import os, sys
import random
import pandas as pd
from functions.OktyBotDB import *
from openpyxl import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MAIN_PATH = os.environ.get("MAIN_PATH")
COUPLES_PATH = os.environ.get("COUPLES_PATH")
BLACKLIST_PATH = os.environ.get("BLACKLIST_PATH")

def check_sick(pupil_surname): #Модуль проверяет фамилию человека на наличие болезни, возвращает True есл не болеет
    pupil_sick = check_sick()
    if pupil_surname in pupil_sick:
        return False
    else:
        return True

def check_position(pupil_surname): #Модуль проверяет человека на среднее количество дежурств, возвращает True если человек дежурил меньше среднего количества дежурств по группе +1
    pupil_num = int(pupil_list[pupil_surname])
    count_duty = int(main_df.loc[pupil_num,'count_duty'])
    if count_duty <= check_position()+1:
        return True
    else:
        return False

def disbat(surname_pupil): #Модуль возвращает True если фамилия имеет маркер в столбце дисбат
    disbat = disbat
    if disbat[int(pupil_list[surname_pupil])] == 1:
        return True
    else:
        return False

def change_number_to_surname(number): #Модуль переводит порядковое число человека в его фамилию
    surname = pupil_list_back[str(number)]
    return surname

def change_surname_to_number(surname): #Модуль переводит фамилию человека в его порядковый номер
    number = pupil_list[surname]
    return number

def set_first_pupil_by_disbat(): #Модуль подставляет первого человека по дисбату, возвращает либо фамилию если человек был найден
    for i in range(22):
        surname = pupil_list_back[str(i)]
        if disbat(surname):
            return surname
    return ''

def set_first_pupil_by_random(): #Модуль возвращает фамилию человека если он прошел проверки, ИСПОЛЬЗУЕТСЯ 1 РАЗ
    stoper = False
    while stoper==False:
        number_pupil = random.randint(0,22)
        surname = change_number_to_surname(number_pupil)
        if check_sick(surname):
            if check_position(surname):
                stoper == True
                return surname
    return ''

def set_second_pupil_by_star_list(first_pupil_surname): #Модуль возвращает фамилию избранного человека, если он прошел проверки
    couple_df = pd.read_excel(MAIN_PATH,sheet_name=first_pupil_surname)
    len_couple_df = couple_df['star'].count()
    surnames = couple_df['surname']
    for i in range(len_couple_df):
        if couple_df.loc[i,'star']==True:
            surname = surnames[i]
            if check_sick(surname):
                if check_position(surname):
                    return surname
    return ''

def set_second_pupil_by_random(first_pupil_surname): #Модуль возвращает фамилию рандомного друга, если он прошел проверки, ИСПОЛЬЗУЕТСЯ 1 РАЗ!
    couple_df = pd.read_excel(COUPLES_PATH, sheet_name=first_pupil_surname)
    couple_star = list(couple_df['star'])
    for i in range(len(couple_star)):
        if couple_star[i] == True:
            star_pupil = change_number_to_surname(i)
    list_of_all_not_star_friends = list(couple_df['surname']!=star_pupil)
    len_friends = len(list_of_all_not_star_friends)
    random_friend = random.randint(0,len_friends)
    not_star_friend = change_number_to_surname(random_friend)
    if check_sick(not_star_friend):
        if check_position(not_star_friend):
            return not_star_friend
    return ''


def set_couple_for_day(): #Модуль собирает пару на 1 день
    first_pupil = ''
    second_pupil = ''

    first_pupil = set_first_pupil_by_disbat()
    if first_pupil =='':
        while first_pupil =='':
            first_pupil = set_first_pupil_by_random()
    second_pupil = set_second_pupil_by_star_list(first_pupil)
    if second_pupil =='':
        counter = 0
        while second_pupil=='':
            second_pupil = set_second_pupil_by_random(first_pupil)
            counter +=1
            if counter>10:
                while second_pupil=='':
                    second_pupil_number = random.randint(0,22)
                    second_pupil_surname = change_number_to_surname(second_pupil_number)
                    if check_sick(second_pupil_surname):
                        if check_position(second_pupil_surname):
                            second_pupil = second_pupil_surname
    pupil_list_for_day = [first_pupil,second_pupil]
    return pupil_list_for_day



# for i in range(50):
    print(set_couple_for_day())

def id_to_name(member_id: str) -> None: # функция просто возвращает имя и фамилию пользователя в зависимости от его id
    dataframe = pd.read_excel(MAIN_PATH)
    id_col = dataframe.loc[0:22, 'telegramID']
    for i in range(len(id_col)):
        # print(dataframe.at[i, 'telegramID']) - ОТЛАДКА
        # print(type(dataframe.at[i, 'telegramID'])) - ОТЛАДКА
        if str(dataframe.at[i, 'telegramID']) == member_id:
            name = dataframe.at[i, "name"]
            print(f'Нашёлся пидарас!): {name}')
            return name

def add_to_blacklist(banned_id: int) -> None:
    wb = load_workbook(BLACKLIST_PATH)
    main_sheet = wb.active
    main_sheet['B2'].value = banned_id
    wb.save(BLACKLIST_PATH)

    return 0

def is_in_group(userid: int) -> bool:
    dataframe = pd.read_excel(MAIN_PATH)
    id_col = list(dataframe.loc[0:22, 'telegramID'])
    return True if userid in id_col else False

print(is_in_group(0))