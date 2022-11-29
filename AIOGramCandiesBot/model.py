# Здесь храним все перменные и методы для их чтения и установки (а-ля работа с классами)
from random import randint
from aiogram import types
import asyncio
import view
import commands
from bot import bot

dealerCandies = 150
turnCandies = 0
playerCandies = 0
botCandies = 0
first_turn = None
coin = 0


def set_coinFlip():
    global coin
    coin = randint(0,1)

def get_coinFlip():
    global coin
    return coin

async def set_firstTurn(message: types.Message):
    global first_turn
    first_turn = await view.first_turn(message)

def get_firstTurn():
    global first_turn
    return first_turn

async def game(message: types.Message):
    global dealerCandies
    global botCandies
    global playerCandies
    frst = get_firstTurn()
    if frst == 0:
        await view.bot_turn_message(message)
        await botTurn(message, dealerCandies)
    else:
        await playerTurn(message, dealerCandies)
    return

async def botTurn(message: types.Message, dealerCandies):
    global turnCandies
    turnCandies = 0
    if dealerCandies == 28:
        turnCandies = 28
    elif dealerCandies == 30:
        turnCandies = 1
    elif dealerCandies < 28:
        turnCandies = dealerCandies
    else:
        turnCandies = randint(1,28)
    dealerCandies = dealerCandies - turnCandies
    await bot.send_message(message.from_user.id, f'Бот походил на {turnCandies} конфет')
    await bot.send_message(message.from_user.id, f'Осталась {dealerCandies} шт')
    return  

async def playerTurn(message, dealerCandies):
    global turnCandies
    turnCandies = 0
    await view.player_turn_message(message)

    turnCandies = message.text
    #тут ловит текст /play ...
    print(f"Игрок походил на {turnCandies} конфет")
        
    return 

# def playerTurn(playerCandies, dealerCandies):
#     turnCandies = 0
#     print(f"Сейчас у вас {playerCandies} конфет. Всего осталось {dealerCandies} конфет")
#     print("Cколько вы хотите взять?")
#     while turnCandies <= 0 or turnCandies > 28:
#         turnCandies = int(input("Введите количество от 1 до 28:\n"))
# #   print(turnCandys)
#     return turnCandies

# def botTurn(botCand, dealerCandies):
#     turnCand = 0
#     print(f"Сейчас у бота {botCand} конфет. Всего осталось {dealerCandies} конфет")
#     print()
#     if dealerCandies == 28:
#         turnCand = 28
#     elif dealerCandies == 30:
#         turnCand = 1
#     elif dealerCandies < 28:
#         turnCand = dealerCandies
#     else:
#         turnCand = randint(1,28)
#     print(f"Бот взял {turnCand} конфет")
#     print()
#     print(f"Сейчас у бота {botCand + turnCand}")
#     return turnCand


# while True:
#     if turn == 0:
#         print("\n__________________________________________________\n" + "\nХод игрока 1" + "\n" + "__________________________________________________\n")
#         turnR = 0
#         turnR = playerTurn(player1Candies, candies)
#         player1Candies = player1Candies + turnR
#         candies = candies - turnR
#         if candies == 0:
#             player1Candies = player1Candies + player2Candies + botCandies
#             player2Candies = 0
#             botCandies = 0
#             print(f"\n$$$$$$$$$$$$$$$$$$$$$$ Вы выиграли! Вам достается {player1Candies} конфет $$$$$$$$$$$$$$$$$$$$$$\n")
#             break
#         turn = 1
#     else:
#         print("\n__________________________________________________\n" + "\nХод бота" + "\n" + "__________________________________________________\n")
#         turnR = 0
#         turnR = botTurn(botCandies, candies)
#         botCandies = botCandies + turnR
#         candies = candies - turnR
#         if candies == 0:
#             botCandies = botCandies + player1Candies
#             player1Candies = 0
#             print(f"\n$$$$$$$$$$$$$$$$$$$$$$ Бот выиграл! Ему достается {botCandies} конфет $$$$$$$$$$$$$$$$$$$$$$\n")
#             break
#         turn = 0