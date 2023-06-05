from loader import db,dp
from aiogram import types
from keyboards.default.main import get_product_markup,get_category_markup
from states.shop import Shopstate

@dp.message_handler(state=Shopstate.category)
async def get_products(message:types.Message):
    category=await db.select_category(title=message.text)
    if category:
        products= await db.select_product_by_category(cat_id=category['id'])
        if products:
            markup= await get_product_markup(products=products)
            await message.answer(f"{category['title']} bolimdan kerakli mahsulotni tanlang!",reply_markup=markup)
            await Shopstate.next()
        else:
            await message.answer(f"{category['title']} bolimda hozircha mahsulot yoq uzr!")
    else:
        markup= await get_category_markup() 
        await message.answer("Bunday topilmadi!",reply_markup=markup)


