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
        [InlineKeyboardButton(text='fasllar // seasons',callback_data='fasllar')],
        [InlineKeyboardButton(text='ranglar // colors',callback_data='colors')],
        [InlineKeyboardButton(text='oylar // months', callback_data='months')],
        [InlineKeyboardButton(text='kiyimlar // clothes',callback_data='clothes')],
        [InlineKeyboardButton(text='aksessuarlar //accessories', callback_data='accessories')],
        [InlineKeyboardButton(text='mebellar // furniture', callback_data="furniture")],
        [InlineKeyboardButton(text='idishlar // dishes', callback_data='dishes')],
        [InlineKeyboardButton(text='ovqatlar // foods', callback_data='foods')],
        [InlineKeyboardButton(text='mevalar // fruits', callback_data='fruits')],
        [InlineKeyboardButton(text="o'quv qurollari // educational materials", callback_data='educational materials')],
        [InlineKeyboardButton(text='maktab fanlari // school subjects', callback_data='school subjects')],
        [InlineKeyboardButton(text='mehnat anjomlari // working tools', callback_data='working tools')],
        [InlineKeyboardButton(text="bog'dagi mehnat anjomlari // gardening tools", callback_data='gardening tools')],
        [InlineKeyboardButton(text='tana azolari // body parts', callback_data='body parts')],
        [InlineKeyboardButton(text='yovvoyi hayvonlar //  wild animals', callback_data='wild animals')],
        [InlineKeyboardButton(text='uy hayvonlari // domestic animals', callback_data='domestic animals')]

    







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
    elif data=='months':
        bot.sendPhoto(chat_id=chat_id, photo='https://www.woodwardenglish.com/wp-content/uploads/2017/11/months-of-the-year-english.jpg')
    elif data=='clothes':
        bot.sendPhoto(chat_id=chat_id, photo='https://www.oysterenglish.com/images/clothing-vocabulary-words.jpg')
    elif data=='accessories':
        bot.sendPhoto(chat_id=chat_id, photo='https://vocabularypoint.com/wp-content/uploads/2022/08/Clothes-And-Accessories-Vocabulary.png')
    elif data=='furniture':
        bot.sendPhoto(chat_id=chat_id, photo='https://static.islcollective.com/storage/preview/201911/766x1084/names-of-furniture-picture-dictionaries_119749_1.jpg')
    elif data=='dishes':
        bot.sendPhoto(chat_id=chat_id, photo='https://i.pinimg.com/474x/5b/a4/af/5ba4af7da194ce985b6d3db29f85c404.jpg')
    elif data=='foods':
        bot.sendPhoto(chat_id=chat_id, photo='https://vocabularypoint.com/wp-content/uploads/2022/05/all-food-names-in-english.png')
    elif data=='fruits':
        bot.sendPhoto(chat_id=chat_id, photo='https://urduesl.com/wp-content/uploads/2021/02/Fruit-Names-737x1024.png') 
    elif data=='educational materials':
        bot.sendPhoto(chat_id=chat_id, photo='https://loveenglish.org/wp-content/uploads/2019/10/School-Supplies-2.jpg')
    elif data=='school subjects':
        bot.sendPhoto(chat_id=chat_id, photo='https://i.pinimg.com/736x/eb/e8/93/ebe89312ba54777cd5b2ae8a11912a0f.jpg')
    elif data=='working tools':
        bot.sendPhoto(chat_id=chat_id, photo='https://i.pinimg.com/originals/74/0e/d1/740ed18eb44431e3f5e3c73f833f0940.jpg')
    elif data=='gardening tools':
        bot.sendPhoto(chat_id=chat_id, photo='https://i.ytimg.com/vi/lK31eOjWy1A/maxresdefault.jpg')
    elif data=='body parts':
        bot.sendPhoto(chat_id=chat_id, photo='http://cdn.shopify.com/s/files/1/0460/3153/6296/products/22x28-19.png?v=1600075638')
    elif data=='wild animals':
        bot.sendPhoto(chat_id=chat_id, photo='https://i.pinimg.com/originals/6f/7a/1e/6f7a1e0b49e9b112aebcfba465882733.jpg')
    elif data=='domestic animals':
        bot.sendPhoto(chat_id=chat_id, photo='https://i.pinimg.com/736x/ca/2b/94/ca2b943d3b717d1f76936acf28cf61fc.jpg')
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
