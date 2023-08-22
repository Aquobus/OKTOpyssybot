import pandas as pd
import openpyxl
import random
import OktyBotDB as OBDf
import time
import datetime

def transform_day(time_ctime): #Превращает запись из вида ctime в вид 01-01-0001
    datetime_obj = time.strptime(time_ctime)

    day = datetime_obj.tm_mday
    month = datetime_obj.tm_mon
    year = datetime_obj.tm_year

    formatted_date = f"{month:02d}-{day:02d}-{year}"

    return formatted_date


def is_more_than_7_days(date1, date2): #Возвращает True если между датами больше 7 дней
    date1_obj = datetime.datetime.strptime(date1, "%m-%d-%Y")
    date2_obj = datetime.datetime.strptime(date2, "%m-%d-%Y")

    delta = date1_obj - date2_obj

    if delta.days > 7:
        return True
    else:
        return False


def check_sick(pupil_surname): #Модуль проверяет фамилию человека на наличие болезни, возвращает True есл не болеет
    pupil_sick = OBDf.check_sick()

    if pupil_surname in pupil_sick:
        return False
    else:
        return True


def check_position(pupil_surname): #Модуль проверяет человека на среднее количество дежурств, возвращает True если человек дежурил меньше среднего количества дежурств по группе +1
    pupil_num = int(OBDf.pupil_list[pupil_surname])

    count_duty = int(OBDf.main_df.loc[pupil_num,'count_duty'])

    if count_duty <= OBDf.check_position()+1:
        return True
    else:
        return False


def disbat(surname_pupil): #Модуль возвращает True если фамилия имеет маркер в столбце дисбат
    disbat = OBDf.disbat

    if disbat[int(OBDf.pupil_list[surname_pupil])] == 1:
        return True
    else:
        return False


def change_number_to_surname(number): #Модуль переводит порядковое число человека в его фамилию
    surname = OBDf.pupil_list_back[str(number)]
    return surname


def change_surname_to_number(surname): #Модуль переводит фамилию человека в его порядковый номер
    number = OBDf.pupil_list[surname]
    return number


def set_first_pupil_by_disbat(today): #Модуль подставляет первого человека по дисбату, возвращает либо фамилию если человек был найден
    for i in range(23):
        surname = OBDf.pupil_list_back[str(i)]

        if disbat(surname):
            num = change_surname_to_number(surname)

            last_duty = OBDf.main_df.loc[int(num),'last_duty']

            if is_more_than_7_days(today,last_duty):
                return surname
    return ''


def set_first_pupil_by_random(today): #Модуль возвращает фамилию человека если он прошел проверки, ИСПОЛЬЗУЕТСЯ 1 РАЗ
    stoper = False

    while stoper==False:
        number_pupil = random.randint(0,23)

        surname = change_number_to_surname(number_pupil)

        if check_sick(surname):
            if check_position(surname):

                num = change_surname_to_number(surname)

                last_duty = OBDf.main_df.loc[int(num), 'last_duty']

                if is_more_than_7_days(str(today), last_duty):
                    stoper = True
                    return surname
    return ''


def set_second_pupil_by_star_list(first_pupil_surname,today): #Модуль возвращает фамилию избранного человека, если он прошел проверки
    couple_df = OBDf.pd.read_excel('couples.xlsx',sheet_name=first_pupil_surname)

    star_list = couple_df['surname']
    len_couple_df = len(star_list)

    surnames = couple_df['surname']

    for i in range(len_couple_df):
        var = couple_df.loc[i,'star']

        if var==True:
            surname = surnames[i]

            if check_sick(surname):
                if check_position(surname):
                    num = change_surname_to_number(surname)

                    last_duty = OBDf.main_df.loc[int(num), 'last_duty']

                    if is_more_than_7_days(today, last_duty):
                        return surname
    return ''


def set_second_pupil_by_random(first_pupil_surname,today): #Модуль возвращает фамилию рандомного друга, если он прошел проверки, ИСПОЛЬЗУЕТСЯ 1 РАЗ!
    couple_df = OBDf.pd.read_excel('couples.xlsx', sheet_name=first_pupil_surname)

    couple_star = list(couple_df['star'])

    for i in range(len(couple_star)):
        if couple_star[i] == True:

            star_pupil = change_number_to_surname(i)
    list_of_all_not_star_friends = list(couple_df['surname']!=star_pupil)

    len_friends = len(list_of_all_not_star_friends)
    random_friend = random.randint(0,len_friends)

    surname_pupil = couple_df.loc[random_friend,'surname']
    not_star_friend = surname_pupil

    if check_sick(not_star_friend):
        if check_position(not_star_friend):
            num = change_surname_to_number(not_star_friend)

            last_duty = OBDf.main_df.loc[int(num), 'last_duty']

            if is_more_than_7_days(today, last_duty):
                return not_star_friend
    return ''


def set_couple_for_day(today): #Модуль собирает пару на 1 день
    first_pupil = ''
    second_pupil = ''

    first_pupil = set_first_pupil_by_disbat(today)
    if first_pupil =='':
        while first_pupil =='':
            first_pupil = set_first_pupil_by_random(today)

    second_pupil = set_second_pupil_by_star_list(first_pupil,today)
    if second_pupil =='':
        counter = 0

        while second_pupil=='':
            second_pupil = set_second_pupil_by_random(first_pupil,today)
            counter +=1

            if counter>10:
                while second_pupil=='':

                    second_pupil_number = random.randint(0,22)
                    second_pupil_surname = change_number_to_surname(second_pupil_number)

                    if check_sick(second_pupil_surname):
                        if check_position(second_pupil_surname):

                            num = change_surname_to_number(second_pupil_surname)
                            last_duty = OBDf.main_df.loc[int(num), 'last_duty']

                            if is_more_than_7_days(str(today), last_duty):
                                second_pupil = second_pupil_surname

    pupil_list_for_day = [first_pupil,second_pupil]
    return pupil_list_for_day


#def synchronizer():  #Не использовать! Еблан перезаписывает таблицу!!!
#    for i in range(23):
#        dataframe = OBDf.main_df
#        surname = dataframe.loc[i,'surname']
#        count_duty_surname = dataframe.loc[i,'count_duty']
#        last_duty_surname = dataframe.loc[i,'last_duty']
#
#        couple_df = OBDf.pd.read_excel('couples.xlsx', sheet_name=surname)
#        len_couple_df = len(list(couple_df['surname']))
#        pupil_surnames_list = []
#        for j in range(len_couple_df):
#            pupil_surnames_list.append(couple_df.loc[j,'surname'])
#        counter = 0
#        for j in pupil_surnames_list:
#            value1 = dataframe.loc[counter,'count_duty']
#            value2 = dataframe.loc[counter,'last_duty']
#            couple_df.loc[counter,'count_duty'] = value1
#            couple_df.loc[counter, 'last_duty'] = value2
#            couple_df.to_excel('couples.xlsx')
#            counter +=1


def set_week(): #Создает неделю с дежурными
    today = time.ctime()
    today = str(transform_day(today))

    week = []
    pupil_list = []
    day = []

    while len(week) != 5:
        while day ==[]:
            try:
                day = set_couple_for_day(today)
            except KeyError:
                pass

        pupil_1 = day[0]
        pupil_2 = day[1]

        if pupil_1 in pupil_list or pupil_2 in pupil_list:
            pass
        else:
            day = [pupil_1,pupil_2]

            pupil_list.append(pupil_1)
            pupil_list.append(pupil_2)

            week.append(day)

            today = datetime.datetime.strptime(str(today), '%m-%d-%Y') + datetime.timedelta(days=1)

        day = []
    return week


for i in range(10):
    print(set_week())