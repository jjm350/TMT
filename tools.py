import requests, json
from time import sleep

class send_message():

    def running(self, current_value):
        value = current_value
        bot_message = "Currently Running: Value in Account = $%s" %value
        bot_token = '742821837:AAE2BhNVs61AN44VynPstT2-zKMkNml9tvg'
        bot_chatID = '841481087'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)

        return response.json()

    def start(self):
        bot_message = "Began Operation"
        bot_token = '742821837:AAE2BhNVs61AN44VynPstT2-zKMkNml9tvg'
        bot_chatID = '841481087'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)

        return response.json()


    def custom(self, message):
        bot_message = message
        bot_token = '742821837:AAE2BhNVs61AN44VynPstT2-zKMkNml9tvg'
        bot_chatID = '841481087'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)

        return response.json()

class trading_tools():
    def getBitcoinPrice(self):
        URL = 'https://www.bitstamp.net/api/ticker/'
        try:
            r = requests.get(URL)
            priceFloat = float(json.loads(r.text)['last'])
            return priceFloat
        except requests.ConnectionError:
            print "Error querying Bitstamp API"

    def percent_calculator(self, purchase, price):
        difference = (price - purchase)
        percent = difference/purchase
        return percent

    def avg_slope(self, p1, p2, p3, p4, p5):
        s1 = p5 - p4
        s2 = p4 - p3
        s3 = p3 - p2
        s4 = p2 - p1
        s5 = (p5 - p1)

        sum = s1 + s2 + s3 + s4 + s5
        average = sum/5
        return average
