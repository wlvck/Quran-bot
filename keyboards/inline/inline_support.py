from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import cancel_support, support_callback
from data.config import ADMINS
from loader import dp


async def check_support_available(support_id):
    state = dp.current_state(chat=support_id, user=support_id)
    state_str = str(
        await state.get_state()
    )
    if state_str == 'in_support':
        return
    else:
        return support_id


async def get_support_manager():
    admin = ADMINS
    for manager in admin:
        manager = await check_support_available(manager)
        if manager:
            return manager
    else:
        return


async def support_keyboard(messages, user_id=None):
    if user_id:
        contact_id = int(user_id)
        as_user = 'no'
        text = 'Жауап қайтару'
    else:
        contact_id = await get_support_manager()
        as_user = 'yes'

        if messages == 'many' and contact_id is None:
            return False
        elif messages == 'one' and contact_id is None:
            contact_id = ADMINS[0]

        if messages == 'one':
            text = 'Админге хабарлама жолдау'
        else:
            text = 'Make conversation with manager'

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=text, callback_data=support_callback.new(messages=messages,
                                                                                    user_id=contact_id,
                                                                                    as_user=as_user)))

    if messages == 'many':
        keyboard.add(
            InlineKeyboardButton(
                text='Cancel',
                callback_data=cancel_support.new(
                    user_id=contact_id
                )
            )
        )

    return keyboard

