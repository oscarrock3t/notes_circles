import telebot
from telebot import types
import theory
from Key_scale_msg import KeyScaleMsg

API_TOKEN = '6037526162:AAEm7tkUzI8U8uDb9VdE9ZOAED8aAU-Ygw0'

bot = telebot.TeleBot(API_TOKEN)

_messages = {}


@bot.message_handler(commands=['start'])
def command_help(message):
    print(f'Пользователь {message.from_user.first_name} нажал start')
    bot.send_message(message.chat.id,
                     reply_markup=get_notes_markup(), text='Выбирай тональность')


@bot.callback_query_handler(func=lambda call: call.data.startswith('cb_note'))
def user_choice_note(call):
    print(f'Пользователь {call.from_user.first_name} выбрал тональность '
          f'{call.data}')
    _messages.setdefault(call.message.id, KeyScaleMsg())
    _messages[call.message.id].key = call.data.split('_')[-1]
    bot.edit_message_text('Выбери лад', call.from_user.id,
                          message_id=call.message.id,
                          reply_markup=get_scale_markup())


@bot.callback_query_handler(func=lambda call: call.data.startswith('cb_scale'))
def user_choice_scale(call):
    print(f'Пользователь {call.from_user.first_name} выбрал лад '
          f'{call.data}')
    _messages[call.message.id].scale = call.data.split('_')[-1]
    _messages[call.message.id].notes = theory.get_scale(
        _messages[call.message.id].key,
        _messages[call.message.id].scale
    )
    text = f'Тональность: {_messages[call.message.id].key}\n' \
           f'Лад: { _messages[call.message.id].scale}\n' \
           f'Ноты:\n{" ".join(_messages[call.message.id].notes)}'
    bot.edit_message_text(text, call.from_user.id,
                          message_id=call.message.id)


def get_notes_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 4
    markup.add(*[types.InlineKeyboardButton(value, callback_data=f'cb_note_'
                                                                 f'{value}')
                 for key, value in enumerate(theory.notes)])
    return markup


def get_scale_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 4
    markup.add(*[types.InlineKeyboardButton(value, callback_data=f'cb_scale_'
                                                                 f'{value}')
                 for key, value in enumerate(theory.scales.keys())])
    return markup


bot.infinity_polling()
