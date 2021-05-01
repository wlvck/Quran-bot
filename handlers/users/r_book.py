import urllib.parse

import requests
from aiogram import types
import json

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bs4 import BeautifulSoup

from keyboards.default.category_menu import category_menu
from loader import dp, bot


@dp.message_handler(commands=['r_books'])
async def send_photo_url(message: types.Message):
    await message.answer('Келесі санаттардың бірін таңдаңыз', reply_markup=category_menu)

    #
    # r = requests.get(url=link)
    # soup = BeautifulSoup(r.text, 'lxml')
    # section = soup.find('section', class_='card document')
    # h1 = section.find('h1').text.strip()
    # description = section.find('div', class_='document__description document__description_full')
    # p = description.find_all('p')
    # book = section.find('a', class_='button button_brown').get('href')
    # photo = section.find('img', class_='course-author__book-image')
    # await bot.send_photo(chat_id=message.chat.id,
    #                      photo=f'https://azan.ru{photo.get("src")}',
    #                      caption=f'{h1}\n\n'
    #                              f'{p[0].text}\n\n'
    #                              f'{p[-1].text}')
    # await bot.send_document(chat_id=message.chat.id, document=f'https://azan.ru{book}')


with open("D:\Pycharm projects\/aio_names_bot\data\/books_url.json", "r", encoding="utf8") as file:
    read_file = json.load(file)

all_books_list = []
list_of_categories = read_file.keys()
for i in list_of_categories:
    a = read_file[i].keys()
    for x in a:
        all_books_list.append(x.strip())

for item in read_file:
    @dp.message_handler(text=f'{item}')
    async def send_message(message: types.Message):
        keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for books in read_file[message.text]:
            buttons = KeyboardButton(text=books)
            keyboard.insert(buttons)
        cancel_button = KeyboardButton(text='Артқа')
        keyboard.insert(cancel_button)
        await message.answer(text='Кітапты таңдаңыз', reply_markup=keyboard)
        #
        # for book in all_books_list:
        #     @dp.message_handler(text=book)
        #     async def send_book(msg: types.Message):
        #         url_for_book = read_file[message.text][msg.text]
        #         r = requests.get(url=url_for_book)
        #         soup = BeautifulSoup(r.text, 'lxml')
        #         section = soup.find('section', class_='card document')
        #         h1 = section.find('h1').text.strip()
        #         # description = section.find('div', class_='document__description document__description_full')
        #         user_book = section.find('a', class_='button button_brown').get('href')
        #         photo = section.find('img', class_='course-author__book-image')
        #         await bot.send_photo(chat_id=message.chat.id,
        #                              photo=f'https://azan.ru{photo.get("src")}',
        #                              caption=f'{h1}\n\n')
        #         await bot.send_document(chat_id=message.chat.id, document=f'https://azan.ru{user_book}')


@dp.message_handler(text='Артқа')
async def back_to_menu(m: types.Message):
    await m.answer(text='Келесі санаттардың бірін таңдаңыз', reply_markup=category_menu)


@dp.message_handler()
async def send_message(message: types.Message):
    check_count = []
    for book in all_books_list:
        if message.text == book.strip():
            check_count.append(book)
            if len(check_count) == 1:
                li = []
                for category in read_file.values():
                    for key, link in category.items():
                        if message.text == key.strip():
                            li.append(link)
                            if len(li) == 1:
                                r = requests.get(url=link)
                                url = 'https://azan.ru'
                                soup = BeautifulSoup(r.text, 'lxml')
                                section = soup.find('section', class_='card document')
                                h1 = section.find('h1').text.strip()
                                book = section.find('a', class_='button button_brown').get('href')
                                photo = section.find('img', class_='course-author__book-image')
                                await bot.send_photo(chat_id=message.chat.id,
                                                     photo=f'{url+urllib.parse.quote(photo.get("src"))}',
                                                     caption=f'{h1}\n\n')
                                await bot.send_document(chat_id=message.chat.id,
                                                        document=f'{url+urllib.parse.quote(book)}')

                            else:
                                continue
            else:
                continue
