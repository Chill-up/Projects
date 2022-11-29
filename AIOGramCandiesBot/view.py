# Сюда все функции отправляющие сообщения
from aiogram import types
import asyncio
from bot import bot


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки\n'
                           f'\nДля начала игры введите команду /play')


async def bot_turn_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ходит бот')
    await asyncio.sleep(1)

async def player_turn_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ходит игрок')
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, введите кол-во конфет, которое хотите взять.\n От 1 до 28\n')
    await asyncio.sleep(1)

async def info_message(message: types.Message):
    await bot.send_message(message.from_user.id, f'На столе 150 конфет. Каждый игрок по по очереди берет от 1 до 28 шт\n\n\
\nТот игрок, кто взял последнюю конфету, забирает их все и побеждает.\n \
\nСначала кидаем кости и выясним у кого первый ход! ')
    await asyncio.sleep(3)

async def first_turn(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бросок бота.')
    b = await message.answer_dice()
    #print(b)
    await asyncio.sleep(4)
    await bot.send_message(message.from_user.id, 'Бросок игрока.')
    p = await message.answer_dice()
    #print(p)
    await asyncio.sleep(4)
    if b.dice.value == p.dice.value:
        await bot.send_message(message.from_user.id, 'Ничья! Перебрасываем')
        await first_turn(message)
    elif b.dice.value > p.dice.value:
        await bot.send_message(message.from_user.id, 'Первый ход у бота')
        return 0
    else:
        await bot.send_message(message.from_user.id, 'Первый ход у игрока')
        return 1
