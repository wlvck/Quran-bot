from aiogram.dispatcher import FSMContext

from keyboards.inline.callback_datas import support_callback
from keyboards.inline.inline_support import support_keyboard
from loader import dp, bot
from aiogram.dispatcher.filters import Command
from aiogram import types


@dp.message_handler(Command('support'))
async def support_def(message: types.Message):
    text = 'Кері байланыс жасау үшін төмендегі батырманы басыңыз'
    keyboard = await support_keyboard(messages='one')
    await message.answer(text=text, reply_markup=keyboard)


@dp.callback_query_handler(support_callback.filter(messages='one'))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    user_id = int(callback_data.get('user_id'))

    await call.message.answer(text='Сұрағыңызды осында жазыңыз')
    await state.set_state('wait_for_support_message')
    await state.update_data(second_id=user_id)


@dp.message_handler(state='wait_for_support_message', content_types=types.ContentTypes.ANY)
async def send_to_support(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get('second_id')
    await bot.send_message(second_id,
                           f'Жаңа хабарлама!📩\n\n')
    keyboard = await support_keyboard(messages='one', user_id=message.from_user.id)
    await message.copy_to(second_id, caption='Төмендегі батырманы басу арқылы жауап бере аласың⤵️',
                          reply_markup=keyboard)
    await message.answer(text='Хабарлама жіберілді')
    await state.reset_state()

