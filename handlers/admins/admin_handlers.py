#
from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter, Text

from loader import dp, bot
from filters.is_admin import AdminFilter

import utils.db_api.sqliter as sqliter


# Отправляем бд со всеми юзерами
@dp.message_handler(AdminFilter(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['bd'], state='*')
async def send_menu(message: types.Message):
    with open("./data/databases/all_users.db", 'rb') as f:
        await bot.send_document(message.chat.id, f)

# Отправляем бд со всеми акками юзеров
@dp.message_handler(AdminFilter(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['acc'], state='*')
async def send_menu(message: types.Message):
    with open("./data/databases/all_users.db", 'rb') as f:
        await bot.send_document(message.chat.id, f)

# Отправляем статистику
@dp.message_handler(AdminFilter(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['stat'], state='*')
async def send_menu(message: types.Message):

    text = await sqliter.get_statistic()
    if text is not False:
        await bot.send_message(message.from_user.id, text)
    else:
        await bot.send_message(message.from_user.id, f"Что-то пошло не так. Смотри логи")

# HELP для админа
@dp.message_handler(AdminFilter(), Text(equals='хелп', ignore_case=True), ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state='*')
async def send_menu(message: types.Message):
    text = "Команды для админа:\n/bd --->\n/acc --->\n/stat --->"
    await bot.send_message(message.from_user.id, text)