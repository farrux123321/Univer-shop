from loader import dp,db
from aiogram import types
from states.shop import Shopstate
from keyboards.default.main import main_markup,get_category_markup,get_product_markup
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="🏠 Bosh menu",state="*")
@dp.message_handler(text="⬅️ Orqaga",state=Shopstate.category)
async def back_main_menu(message:types.Message,state:FSMContext):
    await message.answer("Siz asosiy menyudasiz kerakli bolimni tanglang!",reply_markup=main_markup)
    await state.finish()

@dp.message_handler(text="⬅️ Orqaga",state=Shopstate.product)
async def category_redict(message:types.Message):
    markup=await get_category_markup()
    await message.answer("Kerakli bolimni tanlang",reply_markup=markup)
    await Shopstate.category.set()

@dp.message_handler(text="⬅️ Orqaga",state=Shopstate.amount)
async def product_redict(message:types.Message,state: FSMContext):
    data = await state.get_data()
    cat_id= data.get("cat_id")
    products= await db.select_product_by_category(cat_id=cat_id)
    markup= await get_product_markup(products=products)
    await message.answer(f"Ushbu bolimdan kerakli mahsulotni tanlang!",reply_markup=markup)
    await Shopstate.product.set()