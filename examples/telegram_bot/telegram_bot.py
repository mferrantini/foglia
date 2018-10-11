import telepot

from telepot.loop import MessageLoop

# The bot token, you can get that token using
# Telegram's BotFather.
TELEGRAM_BOT_TOKEN = "<YOUR_TELEGRAM_BOT_TOKEN>"

# Telegram Bot Setup
bot = telepot.Bot(TELEGRAM_BOT_TOKEN)

# A method to give to MessageLoop which will
# be executed when the bot receives a message
def on_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    # It's a good practice to check the message
    # content_type, it could be something different
    if content_type == 'text':
        bot.sendMessage(chat_id, "Hello!")

# Using MessageLoop you can specify what
# happens when the bot receives a message
MessageLoop(bot, on_message).run_as_thread()