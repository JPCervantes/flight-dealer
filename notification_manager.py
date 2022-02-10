import os
import requests

# VAR ENV - TELEGRAM
BOT_TELEGRAM_TOKEN = os.environ.get('BOT_TELEGRAM_TOKEN')
BOT_CHAT_ID = os.environ.get('BOT_CHAT_ID')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def get_info(self):
        """This method gets and order the info to print it out."""


    def check_price(self, question_price, actual_price):
        """ This method checks the price, return True if actual price is lower than question_price. """
        if int(question_price) > int(actual_price):
            return True

    def send_message(self, destiny, response_price, Outbound_Date, Inbound_Date):

        telegram_message = f'Nuevo precio mínimo para vuelo \nCDMX - {destiny}.' \
                  f' \nPrecio de: ${response_price} MXN' \
                  f'\nSaliendo el {Outbound_Date} \ny regresando el {Inbound_Date}'

        bot_token = BOT_TELEGRAM_TOKEN
        bot_chatID = BOT_CHAT_ID
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
                    + bot_chatID + '&parse_mode=Markdown&text=' + telegram_message
        response = requests.post(send_text)
        print(response)
