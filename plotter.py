# -*- coding: utf-8 -*-

import matplotlib
# from matplotlib.dates import bytespdate2num, num2date
# from matplotlib.ticker import Formatter
import numpy as np

# def MyFormatter(Formatter):
#     def __init__(self,dates,fmt='%Y-%m-%d'):
#         self.dates = dates
#         self.fmt = fmt
    
#     def __call__(self,x,pos=0):
#         'Return the label for time x at position pos'
#         ind = int(np.round(x))
#         if ind >= len(self.dates) or ind < 0:
#             return ''
#         return num2date(self.dates[ind]).strftime(self.fmt)

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
    CCO = analysis[13]
    
    Balance = Inv_result[0]
    Cash = Inv_result[1]
    Inved_value = Inv_result[2]
    
    # formatter = MyFormatter(Dates)
    
    fig1 = matplotlib.pyplot.figure(figsize=(15,10))
    ax1 = fig1.add_subplot(311)
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
        
    ax2 = fig1.add_subplot(312)
    ax2.set_title("RSI")
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax2.plot(Dates[(len(Dates)-1-len(RSI)):(len(Dates)-1)],RSI,'-')
        ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        # ax2.plot(RSI,'-')
        ax2.plot(x_axis[(len(x_axis)-1-len(RSI)):(len(x_axis)-1)],RSI,'-')
    
    # fig2 = matplotlib.pyplot.figure()
    ax3 = fig1.add_subplot(313)
    ax3.set_title("MACD")
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
        
    fig2 = matplotlib.pyplot.figure(figsize=(15,10))
    ax21 = fig2.add_subplot(311)
    ax21.set_title("ADX")
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax21.plot(Dates[(len(Dates)-1-len(pDI)):(len(Dates)-1)],pDI,'-')
        ax21.plot(Dates[(len(Dates)-1-len(mDI)):(len(Dates)-1)],mDI,'-')
        ax21.plot(Dates[(len(Dates)-1-len(ADX)):(len(Dates)-1)],ADX,'-')
        ax21.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax21.plot(x_axis[(len(x_axis)-1-len(pDI)):(len(x_axis)-1)],pDI,'-')
        ax21.plot(x_axis[(len(x_axis)-1-len(mDI)):(len(x_axis)-1)],mDI,'-')
        ax21.plot(x_axis[(len(x_axis)-1-len(ADX)):(len(x_axis)-1)],ADX,'-')
        # ax21.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    ax22 = fig2.add_subplot(312)
    ax22.set_title("KD")
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax22.plot(Dates[(len(Dates)-1-len(K)):(len(Dates)-1)],K,'-')
        ax22.plot(Dates[(len(Dates)-1-len(D)):(len(Dates)-1)],D,'-')
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax22.plot(x_axis[(len(x_axis)-1-len(K)):(len(x_axis)-1)],K,'-')
        ax22.plot(x_axis[(len(x_axis)-1-len(D)):(len(x_axis)-1)],D,'-')
    ax23 = fig2.add_subplot(313)
    ax23.set_title("CCO")
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax23.plot(Dates[(len(Dates)-1-len(CCO)):(len(Dates)-1)],CCO,'-')
        ax23.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax23.plot(x_axis[(len(x_axis)-1-len(CCO)):(len(x_axis)-1)],CCO,'-')
        
    fig3 = matplotlib.pyplot.figure(figsize=(15,10))
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
        # x_axis[(len(x_axis)-1-len(K)):(len(x_axis)-1)]
        ax32.plot(x_axis[(len(x_axis)-1-len(Closes_rate)):(len(x_axis)-1)],Closes_rate,'C0-',label='Close')
        ax32.plot(x_axis[(len(x_axis)-1-len(Balance_rate)):(len(x_axis)-1)],Balance_rate,'C1-',label='Balance')

    ax32.legend()
    print('Close change:' + str(Closes_rate[len(Closes_rate)-1]))
    print('Balance change:' + str(Balance_rate[len(Balance_rate)-1]))
        
    # matplotlib.pyplot.plot_date(Dates,Closes)

