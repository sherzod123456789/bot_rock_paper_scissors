from aiogram.types import ReplyKeyboardMarkup


def generate_stone_paper_seazers():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = ['Камень', 'Ножницы', 'Бумага']
    keyboard.add(*btn)
    return keyboard

