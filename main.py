from telegram.ext import updater
import Constants as keys
from telegram.ext import *
import Responses as R
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

print("Bot starting...")

def start_command(update, context):
    update.message.reply_text('Type Something to get started!')
    
def help_command(update, context):
    update.message.reply_text('help ...')

def handle_message(update,context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")
    

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(keys.API_KEY, use_context=True)
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    
    
    # on non command i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    dp.add_error_handler(error)
    
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    
main()