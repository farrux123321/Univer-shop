from loader import db,dp
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_markup=ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.add(KeyboardButton(text="🛍Katalog"))
main_markup.row("🛒Buyurtmalarim","❔Savol-jvob")
main_markup.row("Uzimda-sotish","Toshirish-punlari")

back_button=KeyboardButton(text="⬅️ Orqaga")
main_menu_button=KeyboardButton(text="🏠 Bosh menu")
cart_button=KeyboardButton(text="🗑 Savat")
checkout_button=KeyboardButton(text="🛒 Rasmiylashtirish")


async def get_category_markup():
    categories=await db.select_all_cats()
    markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    for category in categories:
        markup.insert(KeyboardButton(text=category['title']))
    markup.add(cart_button,checkout_button)
    markup.add(back_button,main_menu_button)
    return  markup

async def get_product_markup(products):
    markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    for product in products:
        markup.insert(KeyboardButton(text=product['title']))
    markup.add(cart_button,checkout_button)
    markup.add(back_button,main_menu_button)
    return markup

async def numbers_markup(number=9):
    markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    for i in range(1,number+1):
        markup.insert(KeyboardButton(text=str(i)))
    markup.add(cart_button,back_button)
    return markup