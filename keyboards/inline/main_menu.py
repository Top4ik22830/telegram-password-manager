from aiogram import types


# ---------------------------- COMMANDS BUTTONS -------------------- #
cmnds_markup = types.InlineKeyboardMarkup(row_width=2)
one = types.InlineKeyboardButton(text='➕ Добавить акк', callback_data='add_acc')
two = types.InlineKeyboardButton(text='🔍 Найти акк', callback_data='search_acc')
three = types.InlineKeyboardButton(text='✏ Редачить акк', callback_data='edit_acc')
four = types.InlineKeyboardButton(text='➖ Удалить акк', callback_data='del_acc')
five = types.InlineKeyboardButton(text='📔 Все акки', callback_data='get_accs')
six = types.InlineKeyboardButton(text='Получить🛠пароль', callback_data='generate_passw')

cmnds_markup.add(one, two)
cmnds_markup.add(three, four)
cmnds_markup.add(five, six)