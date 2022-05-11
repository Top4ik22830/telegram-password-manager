from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import ChatTypeFilter

from utils.db_api import sqliter
from loader import dp, bot
from states.account_commands import EditAccState


@dp.callback_query_handler(lambda c: c.data, ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=EditAccState.choosCellToEdit)
async def btns_reactions(call: types.CallbackQuery, state: FSMContext):
    
    if call.data == "editWeb_call":
        await EditAccState.choosenWebSite.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши новую доп инфу')

    elif call.data == "editLogin_call":
        await EditAccState.choosenLogin.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши новый логин')

    elif call.data == "editMail_call":
        await EditAccState.choosenMail.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши новую почту')

    elif call.data == "editPassword_call":
        await EditAccState.choosenPassword.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши новый пароль')

    elif call.data == "editKeys_call":
        await EditAccState.choosenKeys.set()
        await bot.delete_message(call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, 'Напиши через пробел(!) новые ключи')