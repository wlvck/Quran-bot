from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

from keyboards.inline.callback_datas import region_button

region_buttons = InlineKeyboardMarkup()
region_buttons.row_width = 3

with open('D:\Pycharm projects/\/aio_names_bot\data\city_list.json', 'r+') as file:
    region_list = []
    reading_file = json.load(file)
    region_list.extend(reading_file)
    for x in range(1, 81, 3):
        region_buttons.add(InlineKeyboardButton(text=f'{region_list[x]}',
                                                callback_data=region_button.new(region_name=f'{x}')),
                           InlineKeyboardButton(text=f'{region_list[x+1]}',
                                                callback_data=region_button.new(region_name=f'{x+1}')),
                           InlineKeyboardButton(text=f'{region_list[x+2]}',
                                                callback_data=region_button.new(region_name=f'{x+2}')))
    region_buttons.add(InlineKeyboardButton(text=f'{region_list[-1]}',
                                            callback_data=region_button.new(region_name=82)))


