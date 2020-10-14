# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import matplotlib
# import price_change as chg

date_price = scr.price_scraper()

Dates_str = date_price[0]
Closes = date_price[1]

analysis = ana.analysis(Closes)
Changes = analysis[0]
RSI = analysis[1]
DIF = analysis[2]
MACD = analysis[3]
HIS = analysis[4]

fig1 = matplotlib.pyplot.figure()
ax1 = fig1.add_subplot(311)
ax1.plot_date(Dates_str,Closes,'-')
ax2 = fig1.add_subplot(312)
ax2.plot_date(Dates_str[0:len(RSI)],RSI,'-')
ax3 = fig1.add_subplot(313)
ax3.plot_date(Dates_str[0:len(DIF)],DIF,'-')
ax3.plot_date(Dates_str[0:len(MACD)],MACD,'-')
ax3.bar(Dates_str[0:len(HIS)],HIS)
# matplotlib.pyplot.plot_date(Dates,Closes)