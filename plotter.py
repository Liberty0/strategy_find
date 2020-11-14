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
    MA5 = analysis[8]
    MA10= analysis[9]
    MA20= analysis[10]
    K = analysis[11]
    D = analysis[12]
    
    Balance = Inv_result[0]
    Cash = Inv_result[1]
    Inved_value = Inv_result[2]
    
    fig1 = matplotlib.pyplot.figure()
    ax1 = fig1.add_subplot(511)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax1.plot(Dates[(len(Dates)-1-len(MA20)):(len(Dates)-1)],MA20,'-')
        ax1.plot(Dates[(len(Dates)-1-len(MA10)):(len(Dates)-1)],MA10,'-')
        ax1.plot(Dates[(len(Dates)-1-len(MA5)):(len(Dates)-1)],MA5,'-')
        ax1.plot(Dates,Closes,'-')
        ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        # x-axis for the following plots
        x_axis = np.linspace(0,len(Closes),len(Closes)+1)
        ax1.plot(x_axis[(len(x_axis)-1-len(MA20)):(len(x_axis)-1)],MA20,'-')
        ax1.plot(x_axis[(len(x_axis)-1-len(MA10)):(len(x_axis)-1)],MA10,'-')
        ax1.plot(x_axis[(len(x_axis)-1-len(MA5)):(len(x_axis)-1)],MA5,'-')
        ax1.plot(Closes,'-')
        # ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
        
    ax2 = fig1.add_subplot(512)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax2.plot(Dates[(len(Dates)-1-len(RSI)):(len(Dates)-1)],RSI,'-')
        ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        # ax2.plot(RSI,'-')
        ax2.plot(x_axis[(len(x_axis)-1-len(RSI)):(len(x_axis)-1)],RSI,'-')
    
    # fig2 = matplotlib.pyplot.figure()
    ax3 = fig1.add_subplot(513)
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
        ax3.plot(x_axis[(len(x_axis)-1-len(DIF)):(len(x_axis)-1)],DIF,'-')
        ax3.plot(x_axis[(len(x_axis)-1-len(MACD)):(len(x_axis)-1)],MACD,'-')
        if (Tick == '5m') or (Tick == '10m'):
            HISwidth = 0.5
        elif Tick == '30m':
            HISwidth = .7
        ax31 = ax3.twinx()
        ax31.bar(x_axis[(len(x_axis)-1-len(HIS)):(len(x_axis)-1)],HIS,width=HISwidth)
        # ax3.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    ax4 = fig1.add_subplot(514)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax4.plot(Dates[(len(Dates)-1-len(pDI)):(len(Dates)-1)],pDI,'-')
        ax4.plot(Dates[(len(Dates)-1-len(mDI)):(len(Dates)-1)],mDI,'-')
        ax4.plot(Dates[(len(Dates)-1-len(ADX)):(len(Dates)-1)],ADX,'-')
        ax4.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax4.plot(x_axis[(len(x_axis)-1-len(pDI)):(len(x_axis)-1)],pDI,'-')
        ax4.plot(x_axis[(len(x_axis)-1-len(mDI)):(len(x_axis)-1)],mDI,'-')
        ax4.plot(x_axis[(len(x_axis)-1-len(ADX)):(len(x_axis)-1)],ADX,'-')
        # ax4.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    ax15 = fig1.add_subplot(515)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax15.plot(Dates[(len(Dates)-1-len(K)):(len(Dates)-1)],K,'-')
        ax15.plot(Dates[(len(Dates)-1-len(D)):(len(Dates)-1)],D,'-')
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax15.plot(x_axis[(len(x_axis)-1-len(K)):(len(x_axis)-1)],K,'-')
        ax15.plot(x_axis[(len(x_axis)-1-len(D)):(len(x_axis)-1)],D,'-')
        
    fig3 = matplotlib.pyplot.figure()
    ax31 = fig3.add_subplot(211)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax31.plot(Dates[(len(Dates)-1-len(Inved_value)):(len(Dates)-1)],Inved_value,'-')
        ax31.plot(Dates[(len(Dates)-1-len(Cash)):(len(Dates)-1)],Cash,'-')
        ax31.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Balance,'-')
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax31.plot(Inved_value,'-')
        ax31.plot(Cash,'-')
        ax31.plot(Balance,'-')
    
    Closes_rate = [0] * len(Closes)
    Balance_rate = [0] * len(Balance)
    for i in range(0, len(Closes)):
        Closes_rate[i] = Closes[i] / Closes[len(Closes)-1-len(Balance)]
    for i in range(0,len(Balance)):
        Balance_rate[i] = Balance[i] / Balance[0]
    ax32 = fig3.add_subplot(212)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax32.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Closes_rate[(len(Dates)-1-len(Balance)):(len(Dates)-1)],'C0-',label='Close')
        ax32.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Balance_rate,'C1-',label='Balance')
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax32.plot(Closes_rate[(len(Dates)-1-len(Balance)):(len(Dates)-1)],'C0-',label='Close')
        ax32.plot(Balance_rate,'C1-',label='Balance')

    ax32.legend()
    print('Close change:' + str(Closes_rate[len(Closes_rate)-1]))
    print('Balance change:' + str(Balance_rate[len(Balance_rate)-1]))
        
    # matplotlib.pyplot.plot_date(Dates,Closes)
