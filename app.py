import telebot
from config import keys, TOKEN, API_KEY
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


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


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    try:
        if len(values) > 3:
            raise ConvertionException('Слишком много параметров')

        base, symbol, amount = values

        total_base = CryptoConverter.convert(keys[base], keys[symbol], amount, API_KEY)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f"Цена {amount} {base} в {symbol} - {total_base}"
        bot.reply_to(message, text)


bot.polling()
