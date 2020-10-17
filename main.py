# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import matplotlib
# import price_change as chg

## Inputs
Market = "TW" # TW or US
Code = "2330"
Tick = "D" # m: minuts; H: hour; D: day; 


date_price = scr.price_scraper(Market, Code)

Dates_str = date_price[0]
Closes = date_price[1]
High = date_price[2]
Low = date_price[3]

analysis = ana.analysis(Closes,High,Low)
Changes = analysis[0]
RSI = analysis[1]
DIF = analysis[2]
MACD = analysis[3]
HIS = analysis[4]
pDI = analysis[5]
mDI = analysis[6]
ADX = analysis[7]

fig1 = matplotlib.pyplot.figure()
ax1 = fig1.add_subplot(211)
ax1.plot(Dates_str,Closes,'-')
ax2 = fig1.add_subplot(212)
ax2.plot(Dates_str[0:len(RSI)],RSI,'-')

fig2 = matplotlib.pyplot.figure()
ax3 = fig2.add_subplot(211)
ax3.plot_date(Dates_str[0:len(DIF)],DIF,'-')
ax3.plot_date(Dates_str[0:len(MACD)],MACD,'-')
ax3.bar(Dates_str[0:len(HIS)],HIS)
ax4 = fig2.add_subplot(212)
ax4.plot_date(Dates_str[0:len(pDI)],pDI,'-')
ax4.plot_date(Dates_str[0:len(mDI)],mDI,'-')
ax4.plot_date(Dates_str[0:len(ADX)],ADX,'-')
# matplotlib.pyplot.plot_date(Dates,Closes)