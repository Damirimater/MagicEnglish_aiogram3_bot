from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, CallbackQuery

ed = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text='да'),
	 KeyboardButton(text='нет')]
],
                    resize_keyboard=True,
                    input_field_placeholder='Select: ')

main_inline = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='WebSite', web_app=WebAppInfo(url='https://magicenglishclub.ru/'))],
     [InlineKeyboardButton(text='Запись на пробное занятие', callback_data='register')]
])

phone_request = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text='Поделиться контакатом', request_contact=True)]
], resize_keyboard=True, input_field_placeholder='Выберите 1 вариант ответа')

level_kid = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Никогда не занимался')], [KeyboardButton(text='Начальный')], [KeyboardButton(text='Продвинутый')]
], resize_keyboard=True, input_field_placeholder='Выберите 1 вариант ответа')