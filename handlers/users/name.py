from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from keyboards.inline.list_of_names import *
from keyboards.inline.callback_datas import *


@dp.message_handler(Text('/name'))
async def name(message: Message):
    await message.answer(text='Алланың көркем есімдерінің тізімі',
                         reply_markup=first_page)


@dp.callback_query_handler(go_to.filter(page='page_1'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Алланың көркем есімдерінің тізімі ',
                                reply_markup=first_page)


@dp.callback_query_handler(go_to.filter(page='page_2'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Алланың көркем есімдерінің тізімі ',
                                reply_markup=second_page)


@dp.callback_query_handler(go_to.filter(page='page_3'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Алланың көркем есімдерінің тізімі ',
                                reply_markup=third_page)


@dp.callback_query_handler(go_to.filter(page='page_4'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Алланың көркем есімдерінің тізімі ',
                                reply_markup=fourth_page)


@dp.callback_query_handler(go_to.filter(page='page_5'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Fifth page',
                                reply_markup=fifth_page)


@dp.callback_query_handler(go_to.filter(page='page_6'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Алланың көркем есімдерінің тізімі ',
                                reply_markup=sixth_page)


@dp.callback_query_handler(go_to.filter(page='page_7'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Алланың көркем есімдерінің тізімі ',
                                reply_markup=seventh_page)


@dp.callback_query_handler(go_to.filter(page='page_8'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Алланың көркем есімдерінің тізімі ',
                                reply_markup=eighth_page)


@dp.callback_query_handler(go_to.filter(page='page_9'))
async def filter_(callback: CallbackQuery):
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                text='Алланың көркем есімдерінің тізімі ',
                                reply_markup=ninth_page)
