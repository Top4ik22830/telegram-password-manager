from data.config import get_admins
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types.message import Message


class AdminFilter(BoundFilter):
    
    async def check(self, message: Message):
        ADMINS = await get_admins()
        user = message.from_user.id
        return user in ADMINS