

import config
from aiogram import Bot, Dispatcher, types, executor
from random import randrange

bot = Bot(token= config.tokin)
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start", "go"])
async def start(messege: types.Message):
    await messege.answer(f"Ас саламу алейкум {messege.from_user.full_name}\n "
                         f"Сыграем? Я загадал число от 1 до 3 угадайте")
                         
  
n = randrange(1,3)
n = str(n)  

@dp.message_handler()
async def echo_message(messege: types.Message):
    mes = messege.text

    if mes >= n and mes <= n:
        await bot.send_message(messege.from_user.id, "Вы не угадали попробуйте еще раз!")
    else:
        await bot.send_message(messege.from_user.id, "Правильно вы отгадали!")
        
        
executor.start_polling(dp)
      





