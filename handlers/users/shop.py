from loader import db,dp
from aiogram import types
from keyboards.default.main import  get_category_markup
from states.shop import Shopstate

@dp.message_handler(text="🛍Katalog")
async def get_cats(message:types.Message):
    markup=await get_category_markup()
    await message.answer("Kerakli bolimni tanlang",reply_markup=markup)
    await Shopstate.category.set()

