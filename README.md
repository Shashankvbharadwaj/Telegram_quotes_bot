# Telegram_quotes_bot
 A telegram which sends random motivational quotes every morning
 # Quote of the Day Telegram Bot

This Telegram bot sends a daily inspirational quote to your channel using the Quotable API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShashankvBharadwaj/quote-of-the-day-bot.git
   cd quote-of-the-day-bot

2.Refer to requirements.txt and install dependencies

3.Set up your Telegram bot:

Create a new bot on Telegram:
Open the BotFather on Telegram.
(Use the official one)
Send the /newbot command to create a new bot.
Follow the instructions to choose a name and username for your bot.
Once the bot is created, BotFather will provide you with a unique bot token.
Replace 'YOUR_TELEGRAM_BOT_TOKEN' in the script with your actual bot token.

Important: Disable the ability for others to add your bot to groups:
Open the BotFather again.
Select your bot.
Choose 'Bot Settings'.
Disable 'Group Privacy' to prevent the bot from being added to groups without your consent

use /disable when you create bot token in bot father from others using your bot token 

4.python quote_bot.py

5.Bot Usage
Start the bot by sending the /start command in your Telegram channel.
The bot will send a daily quote to your channel at 8:00 AM.
Customization
You can customize the bot by modifying the send_daily_quote function in the script.
Add your own logic to fetch quotes from a different source if desired.
