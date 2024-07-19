import asyncio
from aiogram.types import Message
from aiogram.filters import CommandStart, CommandObject
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery
from aiogram import F, Router
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb

router = Router()


class Reg(StatesGroup):
    age = State()
    name = State()
    child_name = State()
    level = State()
    phone = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    #await asyncio.sleep(2)
    await message.reply('Привет!')
    await message.answer('Меню', reply_markup=kb.main_inline)


@router.callback_query(F.data == 'register')
async def name_reg(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Reg.name)
    await callback.message.answer('Введите ваше имя')
    

@router.message(Reg.name)
async def child_name_reg(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.child_name)
    await message.answer('введите имя ребенка')


@router.message(Reg.child_name)
async def age_reg(message: Message, state: FSMContext):
    await state.update_data(child_name=message.text)
    await state.set_state(Reg.age)
    await message.answer('введите возраст ребенка')


@router.message(Reg.age)
async def level_reg(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Reg.level)
    await message.answer('введите уровень подготовки ребенка', reply_markup=kb.level_kid)


@router.message(Reg.level)
async def phone_reg(message: Message, state: FSMContext):
    await state.update_data(level=message.text)
    await state.set_state(Reg.phone)
    await message.answer('Введите ваш номер телефона ')#, reply_markup=kb.phone_request


@router.message(Reg.phone)
async def over_reg(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer('Запись завершена! Мы вам напишем')
    data = await state.get_data()
    await message.bot.send_message(chat_id=1338310078, text=f'В боте зарегестрировался человек, вот его данные:  \n Имя: {data['name']}\n  Имя ребенка: {data['child_name']}\n  Возраст: {data['age']}\n Уровень подготовки:  {data['level']} \n    номер:  {data['phone']}')

