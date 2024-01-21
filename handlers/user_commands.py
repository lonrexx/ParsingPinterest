from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.types import InputFile
from handlers.downloading import download
import aiofiles

router = Router()

@router.message(Command("start"))
async def greeting(message: Message):
    await message.answer("Привет. Отправь мне ссылку на гифку с пинтереста и я качну ее :)")

@router.message()
async def download_img(message: Message):
    image_title = await download(message.text, message.from_user.id)

    async with aiofiles.open(f"images/{message.from_user.id}_{image_title}.gif", 'rb') as gif_file:
        await message.answer_photo(gif_file)