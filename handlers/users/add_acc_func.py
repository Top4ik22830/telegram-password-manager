from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter, Text
from aiogram.dispatcher import FSMContext

from utils.db_api import sqliter
from utils.file_manager import generate_password
from utils.create_acc_obj import AccountData
from loader import dp, bot
from states.create_account import AccountStates
from keyboards.default.text_keys import pass_key, markup_yesno, empty


# Сохраняем имя сервиса
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=AccountStates.create_service)
async def service_name_controller(message: types.Message, state: FSMContext):

    await state.update_data(service_name=message.text.lower().strip())
    print(f"удаляем = {message.message_id}")
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.delete_message(message.chat.id, message_id=message.message_id-1)
    # TODO: Вместо сообщения должно появляться всплывающее окно
    await message.answer('Записал название')
    await AccountStates.create_web_site.set()
    await message.answer('Напиши адрес web-сайта или доп. название сервиса. Или поставь прочерк "-"')
    print(f"айди текущ = {message.message_id}")

# Сохраняем web-site
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=AccountStates.create_web_site)
async def web_site_controller(message: types.Message, state: FSMContext):

    await state.update_data(web_site=message.text.lower().strip())
    print(f"удаляем = {message.message_id}")
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.delete_message(message.chat.id, message_id=message.message_id-1)
    # TODO: Вместо сообщения должно появляться всплывающее окно
    await message.answer('Записал доп. информацию')
    await AccountStates.create_login.set()
    await message.answer('Напиши логин')
    print(f"айди текущ = {message.message_id}")

# Сохраняем login
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=AccountStates.create_login)
async def login_controller(message: types.Message, state: FSMContext):

    await state.update_data(login=message.text.lower().strip())
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.delete_message(message.chat.id, message_id=message.message_id-1)
    # TODO: Вместо сообщения должно появляться всплывающее окно
    await message.answer('Записал логин')
    await AccountStates.create_mail.set()
    await message.answer('Напиши почту. Или поставь прочерк "-"')

# Сохраняем mail
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=AccountStates.create_mail)
async def mail_controller(message: types.Message, state: FSMContext):

    await state.update_data(mail=message.text.lower().strip())
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.delete_message(message.chat.id, message_id=message.message_id-1)
    # TODO: Вместо сообщения должно появляться всплывающее окно
    await message.answer('Записал почту')
    await AccountStates.create_password.set()
    await message.answer('Напиши пароль или нажми на кнопку, чтобы я автоматически сгенерировал тебе пароль', reply_markup=pass_key)

# Сохраняем password
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=AccountStates.create_password)
async def password_controller(message: types.Message, state: FSMContext):

    if message.text == "Получить🛠пароль":
        # TODO: Generate a pasword & save in var [DONE]
        passw = await generate_password()
    else:
        passw = message.text.strip()

    await state.update_data(password=passw)
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.delete_message(message.chat.id, message_id=message.message_id-1)
    # TODO: Вместо сообщения должно появляться всплывающее окно
    await message.answer('Записал пароль')
    await AccountStates.create_keys_on.set()
    await message.answer('Напиши все ключи к аккаунту через пробел(!), если есть. Или поставь прочерк -', reply_markup=empty)

# Сохраняем keys
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=AccountStates.create_keys_on)
async def keys_controller(message: types.Message, state: FSMContext):

    await state.update_data(keys=message.text.strip())
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.delete_message(message.chat.id, message_id=message.message_id-1)
    # TODO: Вместо сообщения должно появляться всплывающее окно
    await message.answer('Записал ключи')
    await AccountStates.end.set()
    await message.answer('Проверь свои данные')
    
    data = await state.get_data()
    text = ("Новый аккаунт:\n",
            f"Название:\n{data['service_name']}\n",
            f"Доп. адрес:\n{data['web_site']}\n",
            f"Логин:\n{data['login']}\n",
            f"Почта:\n{data['mail']}\n",
            f"Пароль:\n{data['password']}\n",
            f"Ключи:\n{data['keys']}",)
    
    await message.answer("\n".join(text))
    await message.answer("Всё верно?", reply_markup=markup_yesno)

# Сохраняем в бд или перезапускаем процесс в случае отмены
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=AccountStates.end)
async def cancel_adding(message: types.Message, state: FSMContext):

    if message.text == "➖ Нет":
        # TODO: clear data and states
        # TODO: restart proccess
        await state.finish()
        await AccountStates.create_service.set()
        await bot.delete_message(message.chat.id, message_id=message.message_id-2)
        await bot.delete_message(message.chat.id, message_id=message.message_id-1)
        await bot.delete_message(message.chat.id, message_id=message.message_id)
        await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDbHRhrkPCwIJKsWGL51rhQOI28ZG_IgACAgADSEWjHtkwR19ppkyxIgQ')
        await bot.send_message(message.chat.id, 'Напиши название сервиса/приложения')

    elif message.text == "➕ Да":
        # TODO: save data to DB
        dat = await state.get_data()
        data = AccountData(
                service_name=dat['service_name'], 
                web_site=dat['web_site'], 
                login=dat['login'], 
                mail=dat['mail'], 
                password=dat['password'], 
                keys=dat['keys']
                )
        await sqliter.create_account(message.from_user.id, data)

        # TODO: finish all states [DONE]
        await state.finish()
        
        await bot.delete_message(message.chat.id, message_id=message.message_id-2)
        await bot.delete_message(message.chat.id, message_id=message.message_id-1)
        await bot.delete_message(message.chat.id, message_id=message.message_id)
        await bot.send_message(message.chat.id, 'Аккаунт записан!')
