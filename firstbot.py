from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print("Called /start")
    update.message.reply_text("Hello my darling! How are you today?")

def talk_to_me(update,context):
    text=update.message.text
    print(text)
    update.message.reply_text(text)
def main():
    mybot= Updater(settings.API_KEY, use_context=True)
    dp =mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))    #dobavljaju obrabot4ik
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Bot started")
    mybot.start_polling()    #proverjaet obnovleniaj dlja bota
    mybot.idle()           #krutisj postojannno


if __name__=="__main__":
    main()
