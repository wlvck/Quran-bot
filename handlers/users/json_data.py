from aiogram.types import CallbackQuery

from keyboards.inline.list_of_names import *
from loader import dp, bot
import json

numbers = []
numbers.extend(range(1, 100))

with open("D:\Pycharm projects/\/aio_names_bot\data\data.json", 'r', encoding='utf-8-sig') as json_file:
    load_file = json.load(json_file)
    for el in numbers:
        @dp.callback_query_handler(name_callback.filter(greatest_name=f'{el}'))
        async def get_text(callback: CallbackQuery, callback_data: dict):
            get_number_of_name = callback_data.get('greatest_name')
            cancel_button = InlineKeyboardMarkup(row_width=1,
                                                 inline_keyboard=[[
                                                     InlineKeyboardButton(text='Артқа',
                                                                          callback_data=cancel_callback.new(
                                                                              back=f'{get_number_of_name}'))
                                                 ]])
            await callback.answer(cache_time=1)
            await bot.edit_message_text(message_id=callback.message.message_id,
                                        chat_id=callback.message.chat.id,
                                        text=load_file['names'][f'{get_number_of_name}'],
                                        reply_markup=cancel_button)
            for num in numbers[0:11]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=first_page)

            for num in numbers[11:22]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=second_page)

            for num in numbers[22:33]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=third_page)

            for num in numbers[23:44]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=fourth_page)

            for num in numbers[44:55]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=fifth_page)

            for num in numbers[55:66]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=sixth_page)

            for num in numbers[66:77]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=seventh_page)

            for num in numbers[77:88]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=eighth_page)

            for num in numbers[88:99]:
                @dp.callback_query_handler(cancel_callback.filter(back=f'{num}'))
                async def get_previous_page(call: CallbackQuery):
                    await bot.edit_message_text(message_id=call.message.message_id,
                                                chat_id=call.message.chat.id,
                                                text='Алланың көркем есімдерінің тізімі',
                                                reply_markup=ninth_page)
