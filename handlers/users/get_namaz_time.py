from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from keyboards.inline.callback_datas import region_button
from keyboards.inline.region_button import region_buttons
from loader import dp, bot
import requests
from bs4 import BeautifulSoup
import json

region_name_list = []

with open('D:\Pycharm projects/\/aio_names_bot\data\city_list.json', 'r+') as file:
    json_file = json.load(file)
    region_name_list.extend(json_file)


@dp.callback_query_handler(region_button.filter())
async def get_callback_by_region_name(callback: CallbackQuery):
    r_number = callback.data
    r_number = r_number.strip('region_button' ':')
    with open("D:\Pycharm projects/\/aio_names_bot\data\city_list.json", "r") as c_link:
        read_json = json.load(c_link)
        link = 'https://azan.kz/kz' + read_json[region_name_list[int(r_number)]]
        req = requests.get(url=link)
        soup = BeautifulSoup(req.text, 'lxml')
        main_block_list = soup.find('div', class_='main-block-list')
        time = main_block_list.find_all('div', class_='main-block-time')
        n_name = main_block_list.find_all('div', class_='main-block-name')
        namaz_time_dict = {}

        for a, b in zip(n_name, time):
            namaz_time_dict.update({
                a.text.strip(): b.text
            })
        await bot.edit_message_text(text=f'{region_name_list[int(r_number)]} қаласы бойынша намаз уақыты'
                                         f' төмендегідей\n\n'
                                         f'Таң {namaz_time_dict["Таң"]}\n'
                                         f'Күн {namaz_time_dict["Күн"]}\n'
                                         f'Бесін {namaz_time_dict["Бесін"]}\n'
                                         f'Екінті {namaz_time_dict["Екінті"]}\n'
                                         f'Ақшам {namaz_time_dict["Ақшам"]}\n'
                                         f'Құптан {namaz_time_dict["Құптан"]}\n',
                                    message_id=callback.message.message_id,
                                    chat_id=callback.message.chat.id)


@dp.message_handler(Command('location'))
async def send_location(message: types.Message):
    await message.answer(text='Орналасқан жеріңізді көрсетіңіз', reply_markup=region_buttons)
