from aiogram import types

from loader import dp


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer(text=f'Ас-саляму алейкум уа рахматуллахи уа баракятух {message.from_user.full_name}.\n'
                              f'Бұл бот сізге намаздың басталатын уақытын анықтауға '
                              f'мүмкіндік береді.\n\n'
                              'Ботты бастау үшін /location командасы арқылы орналасқан жеріңізді көрсетіңіз.')

