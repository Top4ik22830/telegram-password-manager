from aiogram.dispatcher.filters.state import State, StatesGroup


class AccountStates(StatesGroup):
    create_service = State()
    create_web_site = State()
    create_login = State()
    create_mail = State()
    create_password = State()
    create_keys_on = State()
    end = State()


