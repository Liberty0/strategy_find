# -*- coding: utf-8 -*-

import price_scraper as scr
import matplotlib
# import price_change as chg

date_price = scr.price_scraper()

Dates = date_price[0]
Closes = date_price[1]

# print(Prices)
# fig1 = matplotlib.pyplot.figure()
# ax1 = fig1.add_subplot(211)
# ax1.plot_date(Dates,Closes)
matplotlib.pyplot.plot_date(Dates,Closes)