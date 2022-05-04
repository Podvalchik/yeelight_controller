import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import *
from aiogram.types import *
from yeelight import *
import re
from colordict import ColorDict
import time
import datetime

colors = ColorDict()
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'нобярь', 'декабрь']
days = list(map(str, range(1, 32)))
hours = list(map(str, range(24)))
minutes = list(map(str, range(0, 60, 5)))

token = '5106366099:AAFKdHj84sWckXtBmO9XEZVa1ozn05vSxec'
from_path = '/Users/podvalchik/Desktop/music_for_bot'
new_path = '/Users/podvalchik/Desktop/remade_bot'


logging.basicConfig(level = logging.INFO)
bot = Bot(token = token)
dp = Dispatcher(bot)
bulb = Bulb("192.168.217.178")


start_end_btn = KeyboardButton('Вкл/Выкл')
alarm = KeyboardButton('Установить будильник')
kb = ReplyKeyboardMarkup(resize_keyboard = True)
kb.add(start_end_btn, alarm)

yinline_kb = InlineKeyboardMarkup()#resize_keyboard = True)
minline_kb = InlineKeyboardMarkup()
dinline_kb = InlineKeyboardMarkup()
hinline_kb = InlineKeyboardMarkup()
mininline_kb = InlineKeyboardMarkup()

y2022_btn = InlineKeyboardButton('2022', callback_data='2022')
y2023_btn = InlineKeyboardButton('2023', callback_data='2023')
yearrs = [y2022_btn, y2023_btn]
yinline_kb.add(y2022_btn, y2023_btn)
for i in months:
    month_btn = InlineKeyboardButton(f'{i}', callback_data=f'{i}')
    minline_kb.add(month_btn)
for i in days:
    day_btn = InlineKeyboardButton(f'{i}', callback_data=f'{i}')
    dinline_kb.add(day_btn)
for i in hours:
    hour_btn = InlineKeyboardButton(f'{i}', callback_data=f'{i}')
    hinline_kb.add(hour_btn)
for i in minutes:
    minute_btn = InlineKeyboardButton(f'{i}', callback_data=f'{i}')
    mininline_kb.add(minute_btn)
minline_kb.row_width = 2
@dp.message_handler(commands = 'admin')
async def admin(message):
    await message.answer('Выберите режим', reply_markup = kb)

@dp.message_handler(lambda message: message.text == 'Вкл/Выкл')
async def turn(message):
    bulb.toggle()

@dp.message_handler(commands = 'setcolor')
async def changecolor(message):
    try:
        clrs = list(map(int, message.get_args().split(' ')))
        bulb.set_rgb(clrs[0], clrs[1], clrs[2])
    except ValueError:
        await message.answer('Выбери цвет и введи /setcolor red green blue, где red, green, blue - параметры от 0 до 255 \n https://www.rapidtables.com/web/color/RGB_Color.html')

@dp.message_handler(lambda message: message.text == 'Установить будильник')
async def setalarm(message):
    await message.answer("Выберите год", reply_markup=yinline_kb)


@dp.callback_query_handler()
async def process_callback_button1(call):

    if call['message']['text'] == 'Выберите год':
        await call.message.edit_text("Выберите месяц")
        await call.message.edit_reply_markup(minline_kb)
    if call['message']['text'] == 'Выберите месяц':
        await call.message.edit_text("Выберите день")
        await call.message.edit_reply_markup(dinline_kb)
    if call['message']['text'] == 'Выберите день':
        await call.message.edit_text("Выберите час")
        await call.message.edit_reply_markup(hinline_kb)
    if call['message']['text'] == 'Выберите год':
        await call.message.edit_text("Выберите минуты")
        await call.message.edit_reply_markup(mininline_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



