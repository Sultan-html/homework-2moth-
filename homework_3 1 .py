import random

from aiogram import Bot, Dispatcher, types, F

from aiogram.filters import CommandStart, Command

from config import token

import asyncio

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: types.Message):
        await message.answer("Привет напиши /random")

@dp.message(Command('random'))
async def random_game(message: types.Message):
    await message.answer("Угадайте загаданное мною число от 1 до 3.")
    
    @dp.message()
    async def handle_guess(user_message: types.Message):
        try:
            user_guess = int(user_message.text)
        except ValueError:
            await message.answer("Пожалуйста, введите число.")
            return

        num = random.randint(1, 3)
        
        if user_guess == num:
            await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg', caption="Поздравляю, вы угадали!")
        else:
            await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg', caption="Увы, вы не угадали. Попробуйте снова!")


async def homework_3_1_():
        await dp.start_polling(bot)


asyncio.run(homework_3_1_())


        






