import asyncio
from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters.command import Command

admin = Router()

ADMINS = [1338310078]

@admin.message(Command('panel'))
async def admin_panel(message: Message):
    if message.from_user.id == ADMINS[0]:
        await message.answer('Admin Panel:')