import requests
import urllib.parse
from aiogram import types
from bs4 import BeautifulSoup

from loader import bot

from data.config import ADMINS
from loader import dp


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer(text=f'Ас-саляму алейкум уа рахматуллахи уа баракятух {message.from_user.full_name}.\n'
                              f'Бұл бот сізге намаздың басталатын уақытын анықтауға '
                              f'мүмкіндік береді.\n\n'
                              f'/start - Ботты қосу\n'
                              '/location - Орналасқан қалаңыз бойынша намаз уақыты\n'
                              '/name - Алланың 99 көркем есімдері \n'
                              '/r_books - Орысша діни кітаптарды жүктеу\n')
    for admins in ADMINS:
        await bot.send_message(admins, text=f'{message.from_user.full_name}, запустил(a) бот')



