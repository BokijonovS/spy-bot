from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('6996348885:AAHfwtQz0S2E9Hg9bzRZIe4NsQn5-Bus-7I')

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu alaykum {full_name}")

@bot.message_handler(commands=['help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, "Qanday yordam kerakligi haqida yozing")

@bot.message_handler(commands=['tutorial'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Bot siz tashlagan rasm va boshqa multimedialarni guruxga tashlab berish uchun ishlatiladi")

@bot.message_handler(content_types=['text', 'photo', 'video', 'animation'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    print(chat_id)
    bot.copy_message(-4162893066, chat_id, message.message_id)


bot.polling()