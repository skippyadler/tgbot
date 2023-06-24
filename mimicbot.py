import telebot

MIMIC_BOT_TOKEN = "beveryveryquiet"

mimic_bot = telebot.TeleBot(MIMIC_BOT_TOKEN)

@mimic_bot.message_handler(func=lambda msg: True)
def text_mimic(message):
    mimic_bot.reply_to(message, message.text)

mimic_bot.infinity_polling()