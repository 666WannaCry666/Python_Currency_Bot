import telebot

TOKEN = "5002515778:AAEKU5QaeLu5wpcrDdcg_ZxbI3YlKnxHRjc"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')
