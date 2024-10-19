import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

dp = Dispatcher()
@dp.message(F.text == 'Urban')
async def urban_message(message):
    await message.answer('Urban message')


@dp.message(Command('start'))
async def start_message(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')


@dp.message()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


# if __name__ == "__main__":
api = '7390509811:AAGZ9MzIsp66MgyqTlE52aFIwIACb8WJfbc'
bot = Bot(token=api)
asyncio.run(dp.start_polling(bot))