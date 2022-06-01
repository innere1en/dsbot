#Бот Discord для просмотра актуального курса криптовалют. Для начала добавляем необходимые библиотеки
import discord
import requests
import asyncio
from discord.ext import commands

#Получаем ответ на HTTPs запрос
btc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=btc&tsyms=USD').json()['USD']
eth = requests.get('https://api.coincap.io/v2/assets/ethereum').json()['data']['priceUsd']
xmr = requests.get('https://min-api.cryptocompare.com/data/price?fsym=xmr&tsyms=USD').json()['USD']
ltc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD').json()['USD']
doge = requests.get('https://min-api.cryptocompare.com/data/price?fsym=doge&tsyms=USD').json()['USD']

client = discord.Client()   #создание экземпляра Client для связи с дискордом

@client.event   #создаем декоратор event для регистрации событий. Т.к. работаем с асинхронной библиотекой, создаем асинхронные функции

@asyncio.coroutine

#при входе бота в режим online, получаем сообщение:
async def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event

async def on_message(message):  #учим бота отвечать на определенные сообщения

    if message.content.lower() == 'btc':
        emb = discord.Embed(title = 'ЦЕНА BITCOIN', color = 0xff0000)   #оформляем вывод сообщения ботом в дискорд
        emb.add_field(name = "Цена:", value = str(btc) + '$', inline = False)
        await message.channel.send(embed = emb)

    if message.content.lower() == 'eth':
        emb = discord.Embed(title = 'ЦЕНА ETHERIUM', color = 0xff0000)
        emb.add_field(name = "Цена:", value = str(eth[:-13]) + '$', inline = False)
        await message.channel.send(embed = emb)

    if message.content.lower() == 'xmr':
        emb = discord.Embed(title = 'ЦЕНА MONERO', color = 0xff0000)
        emb.add_field(name = "Цена:", value = str(xmr) + '$',inline = False)
        await message.channel.send(embed = emb)


    if message.content.lower() == 'ltc':
        emb = discord.Embed(title='ЦЕНА LITECOIN',color=0xff0000)
        emb.add_field(name="Цена:",value=str(ltc)+'$',inline=False)
        await message.channel.send(embed = emb)

    if message.content.lower() == 'doge':
        emb = discord.Embed(title='ЦЕНА DOGECOIN',color=0xff0000)
        emb.add_field(name="Цена:",value=str(doge)+'$',inline=False)
        await message.channel.send(embed = emb)
    await client.process_commands(message)

client.run('OTc5ODU5OTU0ODI1NTYwMTc0.Gisfc7.EMASdRo5PmhIG-htaXu1H1bfzoLwGx9RQZ6PSM')