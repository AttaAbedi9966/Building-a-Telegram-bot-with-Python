import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler,filters

import time


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):




    await update.message.reply_text("سلام به ربات تست خوش آمدید.")
    await context.bot.send_photo(chat_id=update.effective_chat.id,photo=open('1.jpg','rb'),caption='✅تصویر مورد نظر شما ارسال شد')

    await context.bot.send_voice(chat_id=update.effective_chat.id,voice=open('voice1.ogg','rb'),caption='ویس تقدیم شما')


    # await context.bot.send_message(chat_id=update.effective_chat.id, text="سلام چطوری؟")



async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("سلام فانکشن تست انجام شد")


async def robot1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text= update.message.text
    print(text)

    if text=='چطوری' :

        await update.message.reply_text("من خوب هستم شما چطوری")

    if text=='ساعت' or text=='saat' or text=='clock' :
        t= time.time()
        realtime=time.ctime(t)
        await update.message.reply_text(realtime)




async def image(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print(update.message)

    photo = await  update.message.photo[-1].get_file()
    await photo.download_to_drive("image1.jpg")
    

    await update.message.reply_text("عکس شما دریافت شد.")



async def voice(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print(update.message)

    voice = await  update.message.voice.get_file()
    await voice.download_to_drive('voice1.ogg')
    

    await update.message.reply_text("ویس شما دریافت شد")







application = ApplicationBuilder().token('your token').build()
start_handler = CommandHandler('start' , start)
application.add_handler(start_handler)
start_handler = CommandHandler('test' , test)
application.add_handler(start_handler)

new_h= MessageHandler( filters.TEXT , robot1)
application.add_handler(new_h)

new_h= MessageHandler( filters.PHOTO , image)
application.add_handler(new_h)

new_h= MessageHandler( filters.VOICE , voice)
application.add_handler(new_h)



application.run_polling()


