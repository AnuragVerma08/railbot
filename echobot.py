from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

context = None


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    print('Received /Hi command')
    update.message.reply_text('Hi how can we help you !')

def livetrainstatus(bot, update):
    print('Received live train status command')
    update.message.reply_text('live train status ! click on the link -> https://ateebraza.github.io/train_status.html')

def pnrstatus(bot, update):
    print('Received pnr status command')
    update.message.reply_text('pnr status ! click on the link -> https://ateebraza.github.io/pnr.html')

def trainroute(bot, update):
    print('Received train route command')
    update.message.reply_text('train route ! click on the link -> https://ateebraza.github.io/train_route.html')

def seatavail(bot, update):
    print('Received seat availibility command')
    update.message.reply_text('check seat availibility ! click on the link -> https://ateebraza.github.io/seat_availibility.html')

def trainbwstations(bot, update):
    print('Received train between stations command')
    update.message.reply_text('train between stations ! click on the link -> https://ateebraza.github.io/train_between.html')

def train_name_number(bot, update):
    print('Received train_name_number command')
    update.message.reply_text('train name to number and vice-versa ! click on the link -> https://ateebraza.github.io/train_name.html')

def trainfareenquiry(bot, update):
    print('Received train fare enquiry command')
    update.message.reply_text('train fare enquiry ! click on the link -> https://ateebraza.github.io/train_fare.html')

def trainarrivals(bot, update):
    print('Received train arrivals command')
    update.message.reply_text('train arrivals ! click on the link -> https://ateebraza.github.io/train_arrival.html')

def cancelledtrains(bot, update):
    print('Received cancelled trains command')
    update.message.reply_text('check cancelled trains ! click on the link -> https://ateebraza.github.io/cancel.html')

def rescheduledtrains(bot, update):
    print('Received rescheduled trains command')
    update.message.reply_text('check rescheduled trains ! click on the link -> https://ateebraza.github.io/reschedule.html')

def stationnametocode(bot, update):
    print('Received station name to code command')
    update.message.reply_text('station name to code ! click on the link -> https://ateebraza.github.io/station_code.html')

def stationcodetoname(bot, update):
    print('Received station code to name command')
    update.message.reply_text('station code to name ! click on the link -> https://ateebraza.github.io/station_name.html')

def help(bot, update):
    print('Received /help command')
    update.message.reply_text('Menu: \n 1. /livetrainstatus \n 2. /pnrstatus \n 3. /trainroute \n 4. /seatavail \n 5. /trainbwstations \n 6. /train_name_number \n 7. /trainfareenquiry \n 8. /trainarrivals \n 9. /cancelledtrains \n 10. /rescheduledtrains \n 11. /stationnametocode \n 12. /stationcodetoname')


def echo(bot, update):
    print('Received an update')
    update.message.reply_text('Sorry, we were not able to understand, what you wanted to convey!')


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('576640095:AAHW9ufhFW9MLnUuaM6rZEubnCiz_wHaFjo')  # TODO

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("Hi", start))
    dp.add_handler(CommandHandler("Menu", help))
    dp.add_handler(CommandHandler("livetrainstatus", livetrainstatus))
    dp.add_handler(CommandHandler("pnrstatus", pnrstatus))
    dp.add_handler(CommandHandler("trainroute", trainroute))
    dp.add_handler(CommandHandler("seatavail", seatavail))
    dp.add_handler(CommandHandler("trainbwstations", trainbwstations))
    dp.add_handler(CommandHandler("train_name_number", train_name_number))
    dp.add_handler(CommandHandler("trainfareenquiry", trainfareenquiry))
    dp.add_handler(CommandHandler("trainarrivals", trainarrivals))
    dp.add_handler(CommandHandler("cancelledtrains", cancelledtrains))
    dp.add_handler(CommandHandler("rescheduledtrains", rescheduledtrains))
    dp.add_handler(CommandHandler("stationnametocode", stationnametocode))
    dp.add_handler(CommandHandler("stationcodetoname", stationcodetoname))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
