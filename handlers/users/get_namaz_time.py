from aiogram.types import CallbackQuery
from keyboards.inline.callback_datas import region_button
from loader import dp, bot
import requests
from bs4 import BeautifulSoup
import json

region_name_list = []

with open('D:\Pycharm projects/\/aio_names_bot\data\city_list.json', 'r+') as file:
    json_file = json.load(file)
    region_name_list.extend(json_file)
print(len(region_name_list))


@dp.callback_query_handler(region_button.filter())
async def get_callback_by_region_name(callback: CallbackQuery):
    r_number = callback.data
    r_number = r_number.strip('region_button' ':')
    await callback.message.answer(text=f'You have choose')
    print(region_name_list[82])

