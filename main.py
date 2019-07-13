#========================================
# The Money Tree (TMT)
# Justin Myers

from startup import *
from operation import *
import time


#======== Start ===========
print('Initializing')
start = startup_tools()

print('Connection Test')
running = start.connection_check()
running = start.server_test()

print('Testing Complete')

if running == True:
    print('Initial Setup')
    time_metric = time.time()
    master = trading_operator()
    define = definitions()
    original_value = define.starting_balance()
    mode = 2
    size = define.sample_size()
    interval = define.interval()
    ami_def = define.ami()
    sell_value = define.sell_value()
    buy_value = define.buy_value()
    p10 = 0
    trans = 0
    p1 = p2 = p3 = p4 = p9 = master.price_analysis(p10)
    print_value = original_value
    sp_count = 3
    sp = 0
    nc = 0

    master.start_declaration(original_value)
    while running:
        p1 = master.price_analysis(p9)
        time.sleep(interval)
        p2 = master.price_analysis(p1)
        time.sleep(interval)
        p3 = master.price_analysis(p2)
        time.sleep(interval)
        p4 = master.price_analysis(p3)
        time.sleep(interval)
        p5 = master.price_analysis(p4)
        time.sleep(interval)
        p6 = master.price_analysis(p5)
        time.sleep(interval)
        p7 = master.price_analysis(p6)
        time.sleep(interval)
        p8 = master.price_analysis(p7)
        time.sleep(interval)
        p9 = master.price_analysis(p8)
        skip = False

        p4_mod = p8 - (p8*.15)

        if skip == False:
            slope = master.analysis(p1, p2, p3, p4, p5, p6, p7, p8, p9, interval, size)

            if mode == 1:
                value = master.account_value(purchase_price, p9, original_value)
                if (slope <= sell_value):
                    sp = sp + 1
                if (purchase_price >= p9):
                    sp = sp + 1
                if (purchase_price <= p4_mod):
                    sp = sp + 1
                if (slope <= 0):
                    nc = nc + 1
                if nc == 2:
                    sp = sp + 1
                    nc = 0

                if (sp >= sp_count):
                    trans = trans + 1
                    mode = 2
                    original_value = value
                    print_value = original_value
                    sp = 0
                else:
                    print_value = value

            if mode == 2:
                if (slope >= buy_value):
                    trans = trans + 1
                    mode = 1
                    purchase_price = p9

        current_time = time.time()
        ami = (time_metric + ami_def)
        if (current_time >= ami):
            time_metric = time.time()
            master.automatic_communication(1,value)

        print('=======')
        print(p9)
        print(slope)
        print(trans)
        print(print_value)

        sp = 0






print('Closing TMT')
