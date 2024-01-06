import logging
import csv
import os

import asyncio
import pendulum
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the configuration from the .env file
load_dotenv()
local_tz = os.getenv("TIMEZONE")
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
if not bot_token:
    raise ValueError('Telegram Bot token not found in environment variable TELEGRAM_BOT_TOKEN')

bot = Bot(token=bot_token)
dp = Dispatcher()


# Define the handler function for the /start command
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start command.
    """
    await message.reply(
        f"""
        Hi! I'm your bot.
        Please send me a message with name, URL and tags separated by commas.
        -- Deployed Version: {os.getenv('GIT_HASH')}"
        """
    )


# Define the handler function for the messages containing name, URL and tags
@dp.message(Command("add"))
async def process_message(message: types.Message):
    """
    This handler will be called for every message, except for the /start command.
    """
    message_text = message.text
    message_text = message_text.replace("/add", "").strip()

    # Split the message by Newline
    parts = message_text.split('\n')
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


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
