from time import sleep

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging

from finder import AdFinder


# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
API_TOKEN = "5818946580:AAEfb2VAJj4fhUkE7l5pk24ecfkAIwG_6FQ"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""

    await update.message.reply_text("لینک مورد نظر خود را وارد کنید: ")


async def crawl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    user_id = update.effective_user.id
    url = update.message.text
    finder = AdFinder(url)
    crawling = 10
    while crawling > 0:
        ads = finder.run()
        for ad in ads:
            print(ad)
            message = f'{ad.get("title")} \n {ad.get("url")}'
            if ad["image"]:
                try:
                    await update.message.reply_photo(photo=ad["image"], caption=message)
                except Exception as err:
                    print(err)
            else:
                await update.message.reply_text(message)
        crawling -= 1
        sleep(15)
        print('*' * 200)
    await update.message.reply_text(str(user_id))


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
