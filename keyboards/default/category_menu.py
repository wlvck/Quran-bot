import json

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

with open("D:\Pycharm projects\/aio_names_bot\data\/books_url.json", "r", encoding="utf8") as file:
    read_file = json.load(file)

category_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
for item in read_file:
    button = KeyboardButton(item)
    category_menu.insert(button)
