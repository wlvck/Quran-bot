from aiogram import types

from keyboards.inline.region_button import region_buttons
from loader import dp


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply(text='Choose your region',
                        reply_markup=region_buttons)
