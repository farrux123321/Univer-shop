from aiogram.dispatcher.filters.state import State,StatesGroup

class Shopstate(StatesGroup):
    category=State()
    product=State()
    amount=State()