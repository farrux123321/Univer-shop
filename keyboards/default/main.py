from loader import db,dp
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_markup=ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.add(KeyboardButton(text="🛍Katalog"))
main_markup.row("🛒Buyurtmalarim","❔Savol-jvob")
main_markup.row("Uzimda-sotish","Toshirish-punlari")

async def get_category_markup():
    categories=await db.select_all_cats()
    markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    for category in categories:
        markup.insert(KeyboardButton(text=category['title']))
    return  markup

async def get_product_markup(products):
    markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    for product in products:
        markup.insert(KeyboardButton(text=product['title']))
    return markup