import requests
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual value
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Quotable API endpoint
QUOTABLE_API_URL = 'https://api.quotable.io/random'

def send_daily_quote(context):
    quote_response = requests.get(QUOTABLE_API_URL)

    if quote_response.status_code == 200:
        quote_data = quote_response.json()
        quote = quote_data['content']
        author = quote_data['author']
        context.bot.send_message(chat_id=context.job.context, text=f"Quote of the Day: '{quote}' - {author}")
    else:
        print(f"Error fetching quote: {quote_response.status_code}, {quote_response.text}")

def start(update, context):
    update.message.reply_text("Welcome to the Quote of the Day bot!")

def main():
    #updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    updater = Updater(bot=bot, use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Set up scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_daily_quote, 'cron', hour=8, minute=0, context=updater.bot._default_context)

    # Start the scheduler
    scheduler.start()

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()

    
    
    


    