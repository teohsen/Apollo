import logging
import csv
import os
import pendulum
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the configuration from the .env file
load_dotenv()
local_tz = os.getenv("TIMEZONE")
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
if not bot_token:
    raise ValueError('Telegram Bot token not found in environment variable TELEGRAM_BOT_TOKEN')

# Initialize the bot with the token from the configuration
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


# Define the handler function for the /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start command.
    """
    await message.reply("Hi! I'm your bot. Please send me a message with name, URL and tags separated by commas.")


# Define the handler function for the messages containing name, URL and tags
@dp.message_handler(commands=['add'])
async def process_message(message: types.Message):
    """
    This handler will be called for every message, except for the /start command.
    """
    if message.text.startswith('/add'):
        # Strip the command name from the message
        message.text = message.text.replace('/add', '').strip()

    # Split the message by Newline
    parts = message.text.split('\n')
    if len(parts) != 3:
        logging.info("Invalid Inputs")
        await message.reply("Please send me a message with name, URL and tags separated by new line.")
        return

    # Extract the name, URL and tags from the message
    name = parts[0].strip()
    url = parts[1].strip()
    tags = [tag.strip() for tag in parts[2].split()]
    timestamp = pendulum.now("UTC").to_iso8601_string()

    # Append the data to the CSV file
    with open(os.getenv('PATH_TO_DATA'), mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, url, ','.join(tags), timestamp, timestamp])

    # Send a confirmation message to the user
    await message.reply("Bookmark has been saved.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
