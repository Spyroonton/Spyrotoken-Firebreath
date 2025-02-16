import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Game data
chests = [
    {"id": 1, "health": 100, "opened": False},
    {"id": 2, "health": 100, "opened": False},
    {"id": 3, "health": 100, "opened": False},
]

# Function to start the game
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Shoot Chest 1", callback_data='shoot_1')],
        [InlineKeyboardButton("Shoot Chest 2", callback_data='shoot_2')],
        [InlineKeyboardButton("Shoot Chest 3", callback_data='shoot_3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Spyro the Dragon Game! Choose a chest to shoot flames at:', reply_markup=reply_markup)

# Function to handle chest shooting
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    chest_id = int(query.data.split('_')[1])
    chest = next(c for c in chests if c["id"] == chest_id)

    if chest["opened"]:
        query.edit_message_text(text=f"Chest {chest_id} is already opened.")
    else:
        chest["health"] -= 25
        if chest["health"] <= 0:
            chest["opened"] = True
            query.edit_message_text(text=f"Chest {chest_id} has been opened!")
        else:
            query.edit_message_text(text=f"Chest {chest_id} health: {chest['health']}")

# Function to handle errors
def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    # Replace 'Firebreath' with your actual bot token
    updater = Updater("Firebreath", use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
