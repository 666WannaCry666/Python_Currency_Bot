import telebot

TOKEN = "5002515778:AAEKU5QaeLu5wpcrDdcg_ZxbI3YlKnxHRjc"


bot = telebot.TeleBot(TOKEN)


keys = {
    'рубль': 'RUB',
    'гривна': 'UAH',
    'доллар США': 'USD',
    'евро': 'EUR',
    'фунт стерлингов': 'GBP',
    'иена': 'JPY',
    'юань': 'CNY',
    'шекель': 'ILS'
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите комманду боту в следующем формате:\n \
<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\n \
Чтобы узнать поддерживаемые валюты, введите комманду /values"

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты: "
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


bot.polling()
