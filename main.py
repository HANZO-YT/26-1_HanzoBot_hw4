from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

@db.message_handler(commands=['start', 'hello'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}')
    await massage.answer('Это ансвер')
    await massage.reply(massage.from_user.first_name)

@db.message_handler(commands=['quiz'])
async def quiz1(massage: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    ques = 'Откуда мем?'
    answer = [
        'Бетмен',
        'Spider-Man',
        'GigaChad',
        'Спанч Боб'
    ]
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(massage.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='GigaChad',
        reply_markup=markup
    )

@db.callback_query_handler(text='button')
async def quiz2(call: types.CallbackQuery):
    ques = 'Что за Манхва?'
    answer = [
        'Целитель, пожирающий яд',
        'Поднятие уровня в одиночку>',
        'Мир после разрушения',
        'Прирожденный наёмник'
    ]
    photo = open('media/Solo_Leveling.png', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Это Поднятие уровня в одиночку'
    )

@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('что-то еще?')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
