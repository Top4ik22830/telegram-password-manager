from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states.create_account import AccountStates
from states.account_commands import (
    SearchAccState, EditAccState,
    DelAccount
    )

from utils.db_api import sqliter
from utils.file_manager import generate_password, create_backup, delete_backup


@dp.callback_query_handler(lambda c: c.data, ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def btns_reactions(call: types.CallbackQuery, state: FSMContext):
    
    if call.data == "add_acc":
        await AccountStates.create_service.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши название сервиса/приложения')
    
    elif call.data == "search_acc":
        await SearchAccState.searchAccStatusOn.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши название сервиса/приложения который надо найти')

    elif call.data == "edit_acc":
        await EditAccState.editAccStatusOn.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши название сервиса/приложения, данные в котором, ты хочешь отредактировать')

    elif call.data == "del_acc":
        await DelAccount.delaccOn.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши название сервиса/приложения который надо удалить')

    elif call.data == "get_accs":
        # TODO: Выгружается файл в папку
        filePath = await create_backup(call.message.chat.id)
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)

        if str(type(filePath)) == "<class 'str'>":
            # TODO: Отправляется человеку
            with open(filePath, 'rb') as f:
                await bot.send_document(call.message.chat.id, f)
            # TODO: Удаляется файл из папки
            await delete_backup(filePath)
        else:
            await bot.send_message(call.message.chat.id, "Что-то пошло не так. Свяжитесь с админом.")

    elif call.data == "generate_passw":
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        passw = await generate_password()
        await bot.send_message(call.message.chat.id, 'Сгенерированный пароль:')
        await bot.send_message(call.message.chat.id, passw)

