from loader import db,dp
from aiogram import types
from states.shop import Shopstate
from keyboards.default.main import numbers_markup

@dp.message_handler(state=Shopstate.product)
async def send_product(message:types.Message):
    product= await db.select_product(title=message.text)
    markup= await numbers_markup()
    image=product['image']
    caption=f"<b>{product['title']} ({product['quantity']})ta bor! - {product['price']} so'm </b>\n\n<i>{product['description']}</i> "
    await message.answer_photo(photo=image,caption=caption,reply_markup=markup)
    await Shopstate.next()