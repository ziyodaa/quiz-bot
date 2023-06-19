import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6053601984:AAFYDj7RDenkdFFaNwKmUqFAw3KSfLb78EY'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(text= "Matematika")
async def echo(message: types.Message):
    
    await message.answer_poll(
        question= "18x9",
        options=["162", '148', "156", "168"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)

    await message.answer_poll(
        question= "36x3",
        options=["120", '170', "109", "108"],
        is_anonymous=False,
        correct_option_id=3,
        type="quiz"
    )
    await asyncio.sleep(5)

    await message.answer_poll(
        question= "12x8",
        options=["90", '96', "92", "92"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    await message.answer_poll(
        question= "9x6",
        options=["64", '52', "54", "68"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    await message.answer_poll(
        question= "88:8",
        options=["11", '10', "12", "18"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    await message.answer_poll(
        question= "16:2",
        options=["2", '4', "6", "8"],
        is_anonymous=False,
        correct_option_id=3,
        type="quiz"
    )
    await asyncio.sleep(5)


    await message.answer_poll(
        question= "124:2",
        options=["64", '58', "62", "56"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    await message.answer_poll(
        question= "190:2",
        options=["95", '85', "90", "80"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    await message.answer_poll(
        question= "270:3",
        options=["80", '90', "70", "85"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
                                         

# @dp.message_handler(text= "o")
# async def echo(message: types.Message):
    
#     await message.answer_poll(     
#         question= "Kim yaxshi",
#         options=["Olim", 'Hakim', "Tohir", "Eldor"],
#         is_anonymous=False,
#         allows_multiple_answers=True
#     )



# @dp.message_handler(text= "t")
# async def echo(message: types.Message):
    
#     await message.answer_poll(
#         question= "Kim yaxshi",
#         options=["Olim", 'Hakim', "Tohir", "Eldor"],
#         is_anonymous=False,
#         correct_option_id=3,
#         type="quiz"
#     )




@dp.message_handler()
async def echo(message: types.Message):
    
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)