from loader import dp,db
from states.shop import Shopstate
from aiogram import types
from aiogram.dispatcher import FSMContext

# @db.message_handler(lambda message:message.text.isdigit(),state=Shopstate.amount)
# async def  get_amount(message:types.Message,state:FSMContext):
#     await message.answer(f"{message.text} ta maxsulot savatingizga qoshildi!")
#     await message.answer(f"Ushbu  tanlang!",reply_markup=markup)
#     await state.finish()
