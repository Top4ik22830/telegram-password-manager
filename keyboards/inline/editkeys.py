from aiogram import types


# ---------------------------- EDITING BUTTONS -------------------- #
editKeyboard = types.InlineKeyboardMarkup(row_width=2)
one = types.InlineKeyboardButton(text='Доп. инфа (адрес)', callback_data='editWeb_call')
two = types.InlineKeyboardButton(text='Логин', callback_data='editLogin_call')
three = types.InlineKeyboardButton(text='Почту', callback_data='editMail_call')
four = types.InlineKeyboardButton(text='Пароль', callback_data='editPassword_call')
five = types.InlineKeyboardButton(text='Ключи', callback_data='editKeys_call')

editKeyboard.add(one)
editKeyboard.add(two, three)
editKeyboard.add(four, five)