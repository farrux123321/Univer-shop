from loader import db,dp
from aiogram import types
from keyboards.default.main import  get_product_markup,get_category_markup
from states.shop import Shopstate

@dp.message_handler(state=Shopstate.category)
async def get_product(message:types.Message):
    category=await db.select_category(title=message.text)
    if category:
        await message.answer(F"{category['title']} bolimidan kerakli mahsulotni tanglang!",reply_markup=markup)
        products=await db.select_product_by_category(cat_id=category['id'])
        markup=await db.create_table_product(products=products)
        Shopstate.next()
    else:
        markup = get_category_markup()
        await message.answer("Quyidagi kategoriyalardan birini tanglang",reply_markup=markup)

