from telegram.ext import Updater,CommandHandler, CallbackContext, MessageHandler,Filters,CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os 
TOKEN=os.environ['TOKEN']
def start(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id 
    keyboar=ReplyKeyboardMarkup([
       ['Grammar // grammatika',"Dictionary // Lug'at"],
        ['Music in English 🎧','Books in English 📚']
        ])
    bot=context.bot
    bot.sendMessage(
        chat_id=chat_id,
        text='Hello and welcome to our bot!!!',
        reply_markup=keyboar
    )
def Grammar(update: Update, context:CallbackContext):
    chat_id=update.message.chat.id
    keyboar=ReplyKeyboardMarkup([
        ['video tutorial 📹','Documentation 📄'],
        ['Main menu  (Asosiy menu)']
    ])
    bot=context.bot
    bot.sendMessage(
        chat_id=chat_id,
        text='Continue (Davom etish)',
        reply_markup=keyboar
    )
def Documentation(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    keyboar=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='first lesson // 1-dars',callback_data='first lesson')]

    ])
    bot=context.bot
    bot.sendMessage(
       chat_id=chat_id,
       text='Hurmatli foydalanuvchi darslarimiz 0 dan boshlab ketma-ketlikda tuzib chiqilgan. Ingiliz tilini urganishni boshlashingiz mumkin',
       reply_markup=keyboar
    )
     






updater=Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu  (Asosiy menu)'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Grammar // grammatika'),Grammar))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Documentation 📄'),Documentation))

updater.start_polling()
updater.idle()
