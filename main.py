# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import matplotlib

## Inputs
Market = "TW" # TW or US
Code = "2330"
Tick = "D" # m: minuts; H: hour; D: day; 


date_price = scr.price_scraper(Market, Code)

Dates = date_price[0]
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
ax1.plot(Dates,Closes,'-')
if Market == "US":
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
elif Market == "TW":
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
ax2 = fig1.add_subplot(212)
ax2.plot(Dates[0:len(RSI)],RSI,'-')
if Market == "US":
    ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
elif Market == "TW":
    ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))

fig2 = matplotlib.pyplot.figure()
ax3 = fig2.add_subplot(211)
ax3.plot(Dates[0:len(DIF)],DIF,'-')
ax3.plot(Dates[0:len(MACD)],MACD,'-')
if Market == "US":
    ax3.bar(Dates[0:len(HIS)],HIS,width=0.4)
    ax3.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
elif Market == "TW":
    ax3.bar(Dates[0:len(HIS)],HIS,width=0.0001)
    ax3.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
ax4 = fig2.add_subplot(212)
ax4.plot(Dates[0:len(pDI)],pDI,'-')
ax4.plot(Dates[0:len(mDI)],mDI,'-')
ax4.plot(Dates[0:len(ADX)],ADX,'-')
if Market == "US":
    ax4.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
elif Market == "TW":
    ax4.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    
# matplotlib.pyplot.plot_date(Dates,Closes)
