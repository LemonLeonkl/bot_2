from bot_logic import gen_pass
from duck import get_duck_image_url
from animal import get_animal_image_url
import telebot
import os, random
    
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8060051360:AAHkrPOAy6zfIL6b0QZKHumvXf4x2Q6jMlg")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['duck'])
def duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['animal'])
def animal(message):
    image_url = get_animal_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['password'])
def send_pass(message):
    password = gen_pass(10)
    bot.reply_to(message, password)

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    image_name = random.choice(os.listdir('images'))
    with open(f'images/{image_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.polling()
