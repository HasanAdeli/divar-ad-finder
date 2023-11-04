from time import sleep
from random import randint

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging

from finder import AdFinder


# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Your API TOKEN
API_TOKEN = "Your API TOKEN"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""

    await update.message.reply_text("لینک مورد نظر خود را وارد کنید: ")


async def crawl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    user_id = update.effective_user.id
    url = update.message.text
    finder = AdFinder(url)
    while True:
        try:
            ads = finder.run()
            for ad in ads:
                message = f'{ad.get("title")} \n\n\n {ad.get("url")}'
                await update.message.reply_photo(photo=ad["image"], caption=message)
        except Exception as err:
            print(err)

        sleep(randint(30, 60))


def main() -> None:
    """Start the bot."""

    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stop", start))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'^https://divar\.ir/.*$'), crawl))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
