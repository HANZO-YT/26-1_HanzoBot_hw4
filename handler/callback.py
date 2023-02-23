from aiogram import Dispatcher, types
from config import bot


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


def reg_hand_callback(db: Dispatcher):
    db.register_callback_query_handler(quiz2, text='button')
    