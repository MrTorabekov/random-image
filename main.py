import asyncio
import logging
import os

from aiogram import Bot, Dispatcher ,types
from aiogram.filters import Command
from aiogram.types import FSInputFile,InputMediaPhoto
from button import kbd
import random
from datetime import datetime
from aiogram.exceptions import TelegramBadRequest,TelegramServerError

TOKEN = "7163530590:AAEQ_e86WsCKTgOxPtRdY2Vw81-n0MTFCyk"
bot = Bot(TOKEN)
dp = Dispatcher()



@dp.message(Command("start"))
async def on_start(message: types.Message):
    cats_list = os.listdir('cats')
    cat = 'cats/' + random.choice(cats_list)
    photo = FSInputFile(cat)
    await message.answer_photo(photo, reply_markup=kbd.as_markup())


@dp.callback_query()
async def on_callback_query(query: types.CallbackQuery):
    if query.data == "fw":
        print("forward")
    elif query.data == "bw":
        print("backward")
    elif query.data == "rnd":
        cats_list = os.listdir('cats')
        cat = 'cats/' + random.choice(cats_list)
        photoo = FSInputFile(cat)
        try:
            await query.message.edit_media(InputMediaPhoto(media=photoo), reply_markup=kbd.as_markup())
        except (TelegramBadRequest, TelegramServerError):
            await query.answer("Error",show_alert=True)


async def main() -> None:
    print(f"program started at {datetime.now()}")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"program finished at {datetime.now()}")
