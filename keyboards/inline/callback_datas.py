from aiogram.utils.callback_data import CallbackData

name_callback = CallbackData('name', 'greatest_name')
cancel_callback = CallbackData('cancel', 'back')
go_to = CallbackData('go_to', 'page')
region_button = CallbackData('region_button', 'region_name')
support_callback = CallbackData('ask_support', 'messages', 'user_id', 'as_user')
cancel_support = CallbackData('cancel_support', 'user_id')
