# -*- coding: utf-8 -*-

import matplotlib
import numpy as np

def plotter(Tick,date_price,analysis,Inv_result):
    Dates = date_price[0]
    Closes = date_price[1]
    # High = date_price[2]
    # Low = date_price[3]
    
    # Changes = analysis[0]
    RSI = analysis[1]
    DIF = analysis[2]
    MACD = analysis[3]
    HIS = analysis[4]
    pDI = analysis[5]
    mDI = analysis[6]
    ADX = analysis[7]
    
    Balance = Inv_result[0]
    Cash = Inv_result[1]
    Inved_value = Inv_result[2]
    
    fig1 = matplotlib.pyplot.figure()
    ax1 = fig1.add_subplot(411)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax1.plot(Dates,Closes,'-')
        ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax1.plot(Closes,'-')
        # ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    ax2 = fig1.add_subplot(412)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax2.plot(Dates[(len(Dates)-1-len(RSI)):(len(Dates)-1)],RSI,'-')
        ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax2.plot(RSI,'-')
        # ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    
    # fig2 = matplotlib.pyplot.figure()
    ax3 = fig1.add_subplot(413)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax3.plot(Dates[(len(Dates)-1-len(DIF)):(len(Dates)-1)],DIF,'-')
        ax3.plot(Dates[(len(Dates)-1-len(MACD)):(len(Dates)-1)],MACD,'-')
        if Tick == 'd':
            HISwidth = .5
        elif Tick == 'w':
            HISwidth = 3
        elif Tick == 'm':
            HISwidth = 13
        ax3.bar(Dates[(len(Dates)-1-len(HIS)):(len(Dates)-1)],HIS,width=HISwidth)
        ax3.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax3.plot(DIF,'-')
        ax3.plot(MACD,'-')
        if (Tick == '5m') or (Tick == '10m'):
            HISwidth = 0.5
        elif Tick == '30m':
            HISwidth = 1
        ax31 = ax3.twinx()
        ax31.bar(np.linspace(1,len(HIS),len(HIS)),HIS,width=HISwidth)
        # ax3.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    ax4 = fig1.add_subplot(414)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax4.plot(Dates[(len(Dates)-1-len(pDI)):(len(Dates)-1)],pDI,'-')
        ax4.plot(Dates[(len(Dates)-1-len(mDI)):(len(Dates)-1)],mDI,'-')
        ax4.plot(Dates[(len(Dates)-1-len(ADX)):(len(Dates)-1)],ADX,'-')
        ax4.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax4.plot(pDI,'-')
        ax4.plot(mDI,'-')
        ax4.plot(ADX,'-')
        # ax4.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
        
    fig3 = matplotlib.pyplot.figure()
    ax5 = fig3.add_subplot(211)
    ax5.plot(Dates[(len(Dates)-1-len(Inved_value)):(len(Dates)-1)],Inved_value,'-')
    ax5.plot(Dates[(len(Dates)-1-len(Cash)):(len(Dates)-1)],Cash,'-')
    ax5.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Balance,'-')
    
    Closes_rate = [0] * len(Closes)
    Balance_rate = [0] * len(Balance)
    for i in range(0, len(Closes)):
        Closes_rate[i] = Closes[i] / Closes[len(Closes)-1-len(Balance)]
    for i in range(0,len(Balance)):
        Balance_rate[i] = Balance[i] / Balance[0]
    ax6 = fig3.add_subplot(212)
    ax6.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Closes_rate[(len(Dates)-1-len(Balance)):(len(Dates)-1)],'C0-',label='Close')
    ax6.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Balance_rate,'C1-',label='Balance')
    ax6.legend()
    # print(Closes[len(Closes)-1])
        
    # matplotlib.pyplot.plot_date(Dates,Closes)
