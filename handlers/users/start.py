import requests
from aiogram import types
from aiogram.types import ContentType
from bs4 import BeautifulSoup

from keyboards.inline.region_button import region_buttons
from loader import dp, bot


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer(text=f'Ас-саляму алейкум уа рахматуллахи уа баракятух {message.from_user.full_name}.\n'
                              f'Бұл бот сізге намаздың басталатын уақытын анықтауға және '
                              f'хабарлауға мүмкіндік береді.\n\n'
                              'Ботты бастау үшін орналасқан жеріңізді көрсетіңіз.',
                         reply_markup=region_buttons)


@dp.message_handler(commands=['book'])
async def send_photo_url(message: types.Message):
    link = 'https://azan.ru/kutub/view/adabyi-168'
    r = requests.get(url=link)
    soup = BeautifulSoup(r.text, 'lxml')
    section = soup.find('section', class_='card document')
    h1 = section.find('h1').text.strip()
    description = section.find('div', class_='document__description document__description_full')
    p = description.find_all('p')
    book = section.find('a', class_='button button_brown').get('href')
    photo = section.find('img', class_='course-author__book-image')
    await bot.send_photo(chat_id=message.chat.id,
                         photo=f'https://azan.ru{photo.get("src")}',
                         caption=f'{h1}\n\n'
                                 f'{p[0].text}\n\n'
                                 f'{p[-1].text}')
    await bot.send_document(chat_id=message.chat.id, document=f'https://azan.ru{book}')