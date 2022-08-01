import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler

from modules.configs.text import ru
from modules.configs.configuration_builder import get_config


config = get_config()
# stateChecker = StateChecker()

# callback to /start
def start(update, context):
    if update.message.chat.type == 'private' and update.message.from_user.is_bot == False:
        update.message.reply_text(ru['hello'])

# callback to 
def text(update, context):
    if update.message is None:
        return update.message.reply_text(ru['use_button'])


def replyHelp(update, context):
    update.message.reply_text(ru['help'])


def main():
    updater = Updater(config['BOT_TOKEN'], use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", replyHelp))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
