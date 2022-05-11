from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards.inline.main_menu import cmnds_markup

import utils.db_api.sqliter as sqliter


@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state='*')
async def bot_start(message: types.Message):

    # await message.answer(f"{message}")

    # TODO: добавляем ко всем юзерам в бд
    await sqliter.add_new_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name
    )

    # TODO: создаем бд под юзера
    await sqliter.create_table_for_user(message.from_user.id)
    
    with open('data/img/hello.jpg', 'rb') as f:
            photo = f.read()
            await bot.send_photo(message.chat.id, photo, caption=f"Привет, {message.from_user.full_name}!")
    await message.answer(f"Я твой карманный менеджер для твоих аккаунтов. Набери команду /edem чтобы открыть меню.")
    
# Отправляем главное меню
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['edem'], state='*')
async def send_menu(message):
    # TODO: отправляем меню
    with open('data/img/menu.jpg', 'rb') as f:
        photo = f.read()
        await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDbHRhrkPCwIJKsWGL51rhQOI28ZG_IgACAgADSEWjHtkwR19ppkyxIgQ')
        await bot.send_photo(message.chat.id, photo, reply_markup=cmnds_markup)


# Сбрасываем все процессы
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['gg'], state='*')
async def send_menu(message: types.Message, state: FSMContext):
    # TODO: отправляем меню
    await state.finish()
    await message.answer(f"Всё отменил. Чтобы открыть меню, введи /edem")








