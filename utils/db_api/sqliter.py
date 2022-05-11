import os
import sqlite3
import logging

from aiogram.types import user

from utils.create_acc_obj import AccountData

"""
ШАБЛОН ФУНКЦИИ
def func():
    try:
        pass
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> XXX:", e)
            return False
"""


# Создаем таблицу юзеру
async def create_table_for_user(chatid: int):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS chat_{} (
                    "service_name"	TEXT UNIQUE,
                    "web_site"	TEXT,
                    "login"	TEXT,
                    "mail"	TEXT,
                    "password"	TEXT,
                    "keys"	TEXT
                    );""".format(chatid)
        cur.execute(query)
        conn.commit()
        conn.close()
        return True

    except Exception as e:
        logging.exception("Exception in sqliter --> create_table_for_user:", e)
        return False

# Создаем запись и добавляем пустой аккаунт
async def create_account(chatid: int, account: object):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"INSERT OR IGNORE INTO chat_{chatid} VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, (
                    account.service_name,
                    account.web_site,
                    account.login,
                    account.mail,
                    account.password,
                    str(account.keys),
                    ))
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> create_account:", e)
            return False

# Удаляем таблицу
async def delete_table(chatid: int):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"DROP TABLE IF EXISTS chat_{chatid}"
        cur.execute(query)
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> delete_table:", e)
            return False


# Редактируем адрес сайта(приложения)
async def edit_web_site(chatid: int, service_name: str, web_site: str):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"UPDATE chat_{chatid} SET web_site = '{web_site}' WHERE service_name == '{service_name}'"
        cur.execute(query)
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> edit_web_site:", e)
            return False

# Редактируем login
async def edit_login(chatid: int, service_name: str, login: str):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"UPDATE chat_{chatid} SET login = '{login}' WHERE service_name == '{service_name}'"
        cur.execute(query)
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> edit_login:", e)
            return False

# Редактируем почту
async def edit_mail(chatid: int, service_name: str, mail: str):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"UPDATE chat_{chatid} SET mail = '{mail}' WHERE service_name == '{service_name}'"
        cur.execute(query)
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> edit_mail:", e)
            return False

# Редактируем пароль
async def edit_passw(chatid: int, service_name: str, passw: str):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"UPDATE chat_{chatid} SET password = '{passw}' WHERE service_name == '{service_name}'"
        cur.execute(query)
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> edit_passw:", e)
            return False

# Редактируем ключи
async def edit_keys(chatid: int, service_name: str, keys):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"UPDATE chat_{chatid} SET keys = '{keys}' WHERE service_name == '{service_name}'"
        cur.execute(query)
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> edit_passw:", e)
            return False

# Ищем аккаунт юзера
async def search_account(chatid: int, service_name: str):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"SELECT * FROM chat_{chatid} WHERE service_name == '{service_name}'"
        cur.execute(query)
        data = cur.fetchall()
        conn.close()

        account = AccountData(
                data[0][0], 
                web_site=data[0][1], 
                login=data[0][2], 
                mail=data[0][3], 
                password=data[0][4], 
                keys=data[0][5]
                )
        return account

    except Exception as e:
            logging.exception("Exception in sqliter --> search_account:", e)
            return False

# Удаляем аккаунт
async def del_account(chatid: int, service_name: str):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"DELETE FROM chat_{chatid} WHERE service_name == '{service_name}'"
        cur.execute(query)
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> del_account:", e)
            return False


# Выгружаем все аккаунты из БД юзера
async def load_all_accs_from_db(chatid: int):
    try:
        conn = sqlite3.connect('./data/databases/users.db')
        cur = conn.cursor()
        query = f"SELECT * FROM chat_{chatid}"
        cur.execute(query)

        data = cur.fetchall()
        accounts = []
        conn.close()

        for i in range(len(data)):
            account = AccountData(
                    data[i][0], 
                    web_site=data[i][1], 
                    login=data[i][2], 
                    mail=data[i][3], 
                    password=data[i][4], 
                    keys=data[i][5]
                    )
            accounts.append(account)

        return accounts

    except Exception as e:
            logging.exception("Exception in sqliter --> load_all_accs_from_db:", e)
            return False


# Добавляем нового юзера ко всем | БД - all_users
async def add_new_user(
        chatid: int,
        username: str,
        fname: str,
        lname: str):
    try:
        conn = sqlite3.connect('./data/databases/all_users.db')
        cur = conn.cursor()
        query = "INSERT OR IGNORE INTO 'users' VALUES (?, ?, ?, ?)"
        cur.execute(query, (chatid, username, fname, lname))
        conn.commit()
        conn.close()
        return True

    except Exception as e:
            logging.exception("Exception in sqliter --> add_new_user:", e)
            return False


# Считаем количество юзеров в боте
async def get_statistic():
    try:
        conn = sqlite3.connect('./data/databases/all_users.db')
        cur = conn.cursor()
        query = f"SELECT * FROM users"
        cur.execute(query)

        users_amount = len(cur.fetchall())
        conn.close()

        ending = ""
        if 21 > users_amount > 9:
            ending = "пользователей"
        else:
            if users_amount%10 == 1 or users_amount == 1:
                ending = "пользователь"
            elif (5 > users_amount%10 > 1) or (5 > users_amount > 1):
                ending = "пользователя"
            else:
                ending = "пользователей"

        return f"Сейчас в боте зарегистрировано {users_amount} {ending}"

    except Exception as e:
            logging.exception("Exception in sqliter --> load_all_accs_from_db:", e)
            return False
