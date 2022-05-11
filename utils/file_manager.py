import utils.db_api.sqliter as sqliter

import os
import time
import logging

import random as rd
import pandas as pd

# ----------------------------------------------------------------- ВЫГРУЗКА ВСЕХ АККОВ И ФОРМИРОВАНИЕ ТАБЛИЦЫ

async def create_backup(chatid: int):

    accs = await sqliter.load_all_accs_from_db(chatid)

    try:
        data = {
            'Название сервиса': [],
            'Web-сайт': [],
            'Логин': [],
            'Почта': [],
            'Пароль': [],
            'Ключи': [],
        }

        for acc in accs:
            data['Название сервиса'].append(acc.service_name)
            data['Web-сайт'].append(acc.web_site)
            data['Логин'].append(acc.login)
            data['Почта'].append(acc.mail)
            data['Пароль'].append(acc.password)
            data['Ключи'].append(acc.keys)

        df = pd.DataFrame(data)
        filePath = f'./data/backups/backup_{chatid}.xlsx'

        if os.path.exists(filePath):
            os.remove(filePath)

        df.to_excel(filePath)

        return filePath

    except Exception as e:
        logging.exception("Exception in file_manager --> create_backup:", e)
        return False
    
# Удаляем файл из папки после отправки пользователю
async def delete_backup(filePath: str):
    try:
        if os.path.exists(filePath):
            os.remove(filePath)
            
    except Exception as e:
        logging.exception("Exception in file_manager --> delete_backup:", e)
        return False

# Pasword generator
async def generate_password():
    data = [
        r'!$%^&()+-=:<>?|[]{}',
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '0123456789'
    ]
    password = ''
    step = 0.1

    for i in range(rd.randint(2,3)):
        used = []
        step += 0.013
        while len(used) < 4:
            indx = rd.randint(0,3)
            i = rd.randint(0, len(data[indx])-1)
            password += data[indx][i]
            #print(password)
            if indx not in used:
                used.append(indx)
        time.sleep(step)
    return password