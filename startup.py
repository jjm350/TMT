from tools import *


class startup_tools():
    def connection_check(self):
        price = trading_tools()

        try:
            price = price.getBitcoinPrice()
            running = True
            print(price)
            print('Connection Established')
        except:
            running = False
            print('Connection Error')

        return running

    def server_test(self):
        sms = send_message()
        message = "Telegram Sync"

        try:
            sms.custom(message)
            print('Was Telegram Message Recieved?: (1(Y)/0(N)')
            test = input()
            if test == 1:
                success = True
            else:
                success = False

            print('Telegram Sync')

        except:
            print('Failed to Send Message')
            success = False

        return success
