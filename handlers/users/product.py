from loader import db,dp
from aiogram import types
from states.shop import Shopstate
from keyboards.default.main import numbers_markup
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=Shopstate.product)
async def send_product(message:types.Message,state:FSMContext):
    product= await db.select_product(title=message.text)
    await state.update_data(data={'cat_id':product['cat_id']})
    markup= await numbers_markup()
    image_url=product['image']
    caption=f"<b>{product['title']} ({product['quantity']})ta bor! - {product['price']} so'm </b>\n\n<i>{product['description']}</i> "
    await message.answer_photo(photo=image_url,caption=caption,reply_markup=markup)
    await Shopstate.next()