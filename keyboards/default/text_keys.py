from aiogram import types


# ---------------------------- BUTTONS -------------------- #
pass_key = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1,
                                              resize_keyboard=True)
pass_key.add(types.InlineKeyboardButton(text='Получить🛠пароль'))


markup_yesno = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2,
                                         resize_keyboard=True)
yes_btn = types.KeyboardButton('➕ Да')
no_btn = types.KeyboardButton('➖ Нет')
markup_yesno.add(yes_btn, no_btn)


empty = types.ReplyKeyboardRemove()