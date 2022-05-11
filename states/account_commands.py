from aiogram.dispatcher.filters.state import State, StatesGroup


class SearchAccState(StatesGroup):
    searchAccStatusOn = State()

class EditAccState(StatesGroup):
    editAccStatusOn = State()
    choosCellToEdit = State()

    choosenWebSite  = State()
    choosenLogin    = State()
    choosenMail     = State()
    choosenPassword = State()
    choosenKeys     = State()

class DelAccount(StatesGroup):
    delaccOn = State()

