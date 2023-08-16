import pandas as pd
import openpyxl
import random
import OktyBotDB as OBDf

def check_sick(pupil_surname):
    pupil_sick = OBDf.check_sick()
    if pupil_surname in pupil_sick:
        return True
    else: False

def check_position(pupil_surname):
    pupil_num = int(OBDf.pupil_list[pupil_surname])
    count_duty = int(OBDf.main_df.loc[pupil_num,'count_duty'])
    if count_duty <= OBDf.check_position():
        return True
    else:
        return False

def couple(pupil_surname,star):
    if star == True:
        return_list = OBDf.couple(pupil_surname)
        cbs = return_list[2]
        couple_surname = cbs.loc[return_list[0],'surname']
        if check_sick(couple_surname) != True:
            if check_position(couple_surname) == True:
                return couple_surname
        else:
            return 0
    else:
        while True:
            lenn = OBDf.couple(pupil_surname)[1]
            diap = len(lenn)
            counter = 0
            for i in lenn:
                if i==True:
                    num = counter
            random_number = random.randint(0,diap)
            while random_number == num:
                random_number = random.randint(0,diap)
            couple_surname = OBDf.pupil_list_back[str(random_number)]
            if check_sick(couple_surname) != True:
                if check_position(couple_surname) == True:
                    return couple_surname

def disbat(surname_pupil):
    disbat = OBDf.disbat
    if disbat[int(OBDf.pupil_list[surname_pupil])] == 1:
        return True
    else:
        return False

def first_pupil():
    for i in range(22):
        surname = OBDf.pupil_list_back[str(i)]
        if disbat(surname) == True:
            if check_sick(surname) != True:
                if check_position(surname) == True:
                    return surname
    while True:
        random_pupil = random.randint(0, 22)
        fst_pupil_surname = OBDf.pupil_list_back[str(random_pupil)]
        if check_sick(fst_pupil_surname) != True:
            if check_position(fst_pupil_surname) == True:
                return fst_pupil_surname

def get_person():
    pupil_list = []
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    week_list = [d1,d2,d3,d4,d5]
    all_pupil_surnames = []
    for i in range(5):
        counter = 0
        while True:
            fst_pupil_surname = first_pupil()
            snd_pupil_surname = couple(fst_pupil_surname,False)
            print('Строка 81 ',fst_pupil_surname)
            print('Строка 82', snd_pupil_surname)
            if fst_pupil_surname not in all_pupil_surnames:
                if snd_pupil_surname not in all_pupil_surnames:
                    all_pupil_surnames.append(fst_pupil_surname)
                    all_pupil_surnames.append(snd_pupil_surname)
                    week_list[i].append(fst_pupil_surname)
                    week_list[i].append(snd_pupil_surname)
            if counter > 100:
                message = 'Бля братан не могу, в Бахмуте ебашимся'
                return message
            counter +=1

print(check_sick('Бурлака'))
print(get_person())