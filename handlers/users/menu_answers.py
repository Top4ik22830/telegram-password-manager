from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import ChatTypeFilter

from utils.db_api import sqliter
from keyboards.inline.editkeys import editKeyboard
from loader import dp, bot
from states.account_commands import (
    SearchAccState, EditAccState,
    DelAccount
)


# Удаление аккаунта
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=DelAccount.delaccOn)
async def deleting_acc(message: types.Message, state: FSMContext):

    isCorrect  = False
    curr_service_name = message.text.lower().strip()
    accs = await sqliter.load_all_accs_from_db(message.chat.id)
    # TODO: Cheack a correct data
    for acc in accs:
        if acc.service_name == curr_service_name:
            isCorrect = True
    if isCorrect:
        isDid = await sqliter.del_account(message.chat.id, message.text.lower().strip())
        if isDid:
            await bot.send_message(message.chat.id, 'Акаунт успешно удалён.')
            await state.finish()
        else:
            await bot.send_message(message.chat.id, 'Я не нашел такого аккаунта. Проверь наличие в бэкапе.')
    else:
        await bot.send_message(message.chat.id, 'Я не нашел такого аккаунта. Проверь наличие в бэкапе.')
    

# Поиск аккаунта
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=SearchAccState.searchAccStatusOn)
async def searching_acc(message: types.Message, state: FSMContext):

    account = await sqliter.search_account(message.chat.id, message.text.lower().strip())

    if account is False or account is None:
        await bot.send_message(message.chat.id, 'Я не нашел такого аккаунта. Проверь наличие в бэкапе.')
    else:
        await message.answer("Название:")
        await message.answer(account.service_name)
        await message.answer("Доп. адрес:")
        await message.answer(account.web_site)
        await message.answer("Логин:")
        await message.answer(account.login)
        await message.answer("Почта:")
        await message.answer(account.mail)
        await message.answer("Пароль:")
        await message.answer(account.password)
        await message.answer("Ключи:")
        await message.answer(account.keys)
    await state.finish()

# Редактирование аккаунта
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=EditAccState.editAccStatusOn)
async def searching_acc(message: types.Message, state: FSMContext):

    isCorrect  = False
    curr_service_name = message.text.lower().strip()
    accs = await sqliter.load_all_accs_from_db(message.chat.id)
    # TODO: Cheack a correct data
    for acc in accs:
        if acc.service_name == curr_service_name:
            isCorrect = True
    
    if isCorrect:
        await state.update_data(service_name=curr_service_name)
        await EditAccState.choosCellToEdit.set()
        await bot.delete_message(message.chat.id, message_id=message.message_id-1)
        await bot.delete_message(message.chat.id, message_id=message.message_id)
        await bot.send_message(message.chat.id, 'Выбери, что будем редактировать', reply_markup=editKeyboard)
    else:
        await bot.send_message(message.chat.id, 'Такого аккаунта не существует. Напиши ещё раз или проверь в бэкапе.')
        await bot.send_message(message.chat.id, 'Отменить редактирование ---> /gg')


# Редактирование доп инфы
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=EditAccState.choosenWebSite)
async def searching_acc(message: types.Message, state: FSMContext):
    # TODO: set a new web-site
    service_name = await state.get_data()
    service_name = service_name['service_name']
    await sqliter.edit_web_site(message.chat.id, service_name, message.text.lower().strip())
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.send_message(message.chat.id, 'Доп инфа успешно обновлена')
    await state.finish()

# Редактирование логина
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=EditAccState.choosenLogin)
async def searching_acc(message: types.Message, state: FSMContext):
    # TODO: set a new login
    service_name = await state.get_data()
    service_name = service_name['service_name']
    await sqliter.edit_login(message.chat.id, service_name, message.text.lower().strip())
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.send_message(message.chat.id, 'Логин успешно обновлен')
    await state.finish()

# Редактирование почты
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=EditAccState.choosenMail)
async def searching_acc(message: types.Message, state: FSMContext):
    # TODO: set a new mail
    service_name = await state.get_data()
    service_name = service_name['service_name']
    await sqliter.edit_mail(message.chat.id, service_name, message.text.lower().strip())
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.send_message(message.chat.id, 'Почта успешно обновлена')
    await state.finish()

# Редактирование пароля
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=EditAccState.choosenPassword)
async def searching_acc(message: types.Message, state: FSMContext):
    # TODO: set a new password
    service_name = await state.get_data()
    service_name = service_name['service_name']
    await sqliter.edit_passw(message.chat.id, service_name, message.text.strip())
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.send_message(message.chat.id, 'Пароль успешно обновлен')
    await state.finish()

# Редактирование ключей
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=EditAccState.choosenKeys)
async def searching_acc(message: types.Message, state: FSMContext):
    # TODO: set new keys
    service_name = await state.get_data()
    service_name = service_name['service_name']
    await sqliter.edit_keys(message.chat.id, service_name, message.text.strip())
    await bot.delete_message(message.chat.id, message_id=message.message_id)
    await bot.send_message(message.chat.id, 'Ключи успешно обновлены')
    await state.finish()
