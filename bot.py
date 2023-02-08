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
        [InlineKeyboardButton(text='first lesson // 1-dars', callback_data='first lesson')],
        [InlineKeyboardButton(text='second lesson // 2-dars',callback_data='second lesson')],


    ])
    bot=context.bot
    bot.sendMessage(
       chat_id=chat_id,
       text='Hurmatli foydalanuvchi darslarimiz 0 dan boshlab ketma-ketlikda tuzib chiqilgan. Ingiliz tilini urganishni boshlashingiz mumkin',
       reply_markup=keyboar
    )
def Dictionary(update: Update, context=CallbackContext):
    chat_id=update.message.chat.id
    keyboar=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='hafta kunlari // days of the week',callback_data='hafta kunlari')],
        [InlineKeyboardButton(text='fasllar // seasons (sizns)',callback_data='fasllar')],
        [InlineKeyboardButton(text='ranglar // colors (colors)',callback_data='colors')]
    ])
    bot=context.bot
    bot.sendMessage(
        chat_id=chat_id,
        text="Lug'atlar mavzular buyicha tuzib chiqilgan.",
        reply_markup=keyboar
    )
def query(update: Update, context: CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat_id
    data=query.data
    bot=context.bot
  
    if data=='hafta kunlari':
       bot.sendPhoto(photo="https://happydays365.org/wp-content/uploads/2021/06/Days-of-the-Week-in-Uzbek-1.png",chat_id=chat_id)
        
    elif data=='fasllar':
       bot.sendPhoto(photo="https://www.woodwardenglish.com/wp-content/uploads/2020/01/seasons-in-english.jpg",chat_id=chat_id)
    elif data=='colors':
        bot.sendPhoto(photo="https://englishgrammarhere.com/wp-content/uploads/2019/12/Color-Name-List-List-Of-Colors.png",chat_id=chat_id)   
    query.answer('No')

 






updater=Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu  (Asosiy menu)'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Grammar // grammatika'),Grammar))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Documentation 📄'),Documentation))
updater.dispatcher.add_handler(CallbackQueryHandler(query))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Dictionary // Lug'at"),Dictionary))


updater.start_polling()
updater.idle()
