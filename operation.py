from tools import *


class trading_operator():
    def price_analysis(self, price_old):
        price = trading_tools()
        try:
            price = price.getBitcoinPrice()
            return price
        except:
            price = price_old
            return price

    def start_declaration(self, account_start):
        sms = send_message()
        message = "Beginnning Operation"
        print('Final Setup Completed')
        print('Notifying Mobile')
        sms.custom(message)
        sms.running(account_start)
        print('Beginning Operation')

    def analysis(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, interval, sample_size):
        sum_y = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
        sum_x = 1 + 2 + 3 + 4 +5 +6 +7 + 8 + 9
        sum_xy = (p1*1) + (p2*(2)) + (p3*(3)) + (p4*(4)) + (p5*5) + (p6*6) + (p7*7) + (p8*8) + (p9*9)
        sum_x2 = 1 + 2**2 + (3)**2 + (4)**2 + 5**2 + 6**2 + 7**2 + 8**2 + 9**2
        sum_y2 = p1**2 + p2**2 + p3**2 + p4**2 + p5**2 + p6**2 + p7**2 + p8**2 + p9**2

        top = (sample_size*(sum_xy))-(sum_x*sum_y)
        bottom = (sample_size*(sum_x2))-(sum_x**2)
        slope = (top/bottom)
        return slope

    def automatic_communication(self, mode, account_value):
        sms = send_message()
        if mode == 1:
            message = "Automated Update"
            sms.custom(message)
            sms.running(account_value)

    def account_value(self, starting_price, current_price, account_value):
        tools = trading_tools()
        percent_difference = tools.percent_calculator(starting_price, current_price)
        new_value = account_value + account_value * percent_difference
        return new_value


class definitions():
    def starting_balance(self):
        account = 1000
        return account

    def interval(self):
        time = 1
        return time

    def sample_size(self):
        size = 9
        return size

    def ami(self):
        #Time is inputed in hours
        time = .5
        time = time*3600
        return time

    def buy_value(self):
        value = .5
        return value

    def sell_value(self):
        value = -.5
        return value
