import matplotlib
import numpy as np

def invplot(Tick,date_price,Inv_result):
    Dates = date_price[0]
    Closes = date_price[1]
    
    Balance = Inv_result[0]
    Cash = Inv_result[1]
    Inved_value = Inv_result[2]
    Grades = Inv_result[3]
    
    Gd = []
    rsiGd = []
    macdGd = []
    adxGd = []
    ma5Gd = []
    ma10Gd = []
    ma20Gd = []
    for i in range(len(Grades)):
        # Grades.append([[gd,rsigd,macdgd,adxgd,ma5gd,ma10gd,ma20gd,kdgd,CCOgd]])
        Gd.append(Grades[i][0])
        rsiGd.append(Grades[i][1])
        macdGd.append(Grades[i][2])
        adxGd.append(Grades[i][3])
        ma5Gd.append(Grades[i][4])
        ma10Gd.append(Grades[i][5])
        ma20Gd.append(Grades[i][6])
    # print(rsiGd)
        
    x_axis = np.linspace(0,len(Closes),len(Closes)+1)
    # Costomized x-axis label
    Cost_axis = [0] * len(Dates)
    if Tick=='5m' or Tick=='10m':
        for ii in range(len(Dates)):
            if Dates[ii].hour == 9 and Dates[ii].minute == 0:
                Cost_axis[ii] = Dates[ii].strftime('%d.%H')
            elif Dates[ii].minute == 0:
                Cost_axis[ii] = Dates[ii].strftime('%H')
            else:
                Cost_axis[ii] = ''
    elif Tick=='30m':
        for ii in range(len(Dates)):
            if Dates[ii].hour == 9 and Dates[ii].minute == 0:
                Cost_axis[ii] = Dates[ii].strftime('%d')
            else:
                Cost_axis[ii] = ''
    
    fig3 = matplotlib.pyplot.figure(figsize=(15,10))
    ax31 = fig3.add_subplot(311)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax31.plot(Dates[(len(Dates)-1-len(Inved_value)):(len(Dates)-1)],Inved_value,'-')
        ax31.plot(Dates[(len(Dates)-1-len(Cash)):(len(Dates)-1)],Cash,'-')
        ax31.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Balance,'-')
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax31.plot(x_axis[(len(x_axis)-1-len(Inved_value)):(len(x_axis)-1)],Inved_value)
        ax31.plot(x_axis[(len(x_axis)-1-len(Cash)):(len(x_axis)-1)],Cash)
        ax31.plot(x_axis[(len(x_axis)-1-len(Balance)):(len(x_axis)-1)],Balance)
        # ax31.plot(Inved_value,'-')
        # ax31.plot(Cash,'-')
        # ax31.plot(Balance,'-')
        ax31.xaxis.set_ticks(np.arange(len(Dates)+1))
        ax31.set_xticklabels(Cost_axis)
        
    ax32 = fig3.add_subplot(312)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax32.plot(Dates[(len(Dates)-1-len(rsiGd)):(len(Dates)-1)],rsiGd,'-')
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        # x_axis[(len(x_axis)-1-len(K)):(len(x_axis)-1)]
        ax32.plot(x_axis[(len(x_axis)-1-len(Gd)):(len(x_axis)-1)],Gd,label='Tot')
        ax32.plot(x_axis[(len(x_axis)-1-len(rsiGd)):(len(x_axis)-1)],rsiGd,label='RSI')
        ax32.plot(x_axis[(len(x_axis)-1-len(macdGd)):(len(x_axis)-1)],macdGd,label='MACD')
        ax32.plot(x_axis[(len(x_axis)-1-len(adxGd)):(len(x_axis)-1)],adxGd,label='ADX')
        ax32.plot(x_axis[(len(x_axis)-1-len(ma5Gd)):(len(x_axis)-1)],ma5Gd,label='MA5')
        ax32.plot(x_axis[(len(x_axis)-1-len(ma10Gd)):(len(x_axis)-1)],ma10Gd,label='MA10')
        ax32.plot(x_axis[(len(x_axis)-1-len(ma20Gd)):(len(x_axis)-1)],ma20Gd,label='MA20')
        ax32.xaxis.set_ticks(np.arange(len(Dates)+1))
        ax32.set_xticklabels(Cost_axis)
    ax32.legend()
        
    Closes_rate = [0] * len(Closes)
    Balance_rate = [0] * len(Balance)
    for i in range(0, len(Closes)):
        Closes_rate[i] = Closes[i] / Closes[len(Closes)-1-len(Balance)]
    for i in range(0,len(Balance)):
        Balance_rate[i] = Balance[i] / Balance[0]
    ax33 = fig3.add_subplot(313)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax33.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Closes_rate[(len(Dates)-1-len(Balance)):(len(Dates)-1)],'C0-',label='Close')
        ax33.plot(Dates[(len(Dates)-1-len(Balance)):(len(Dates)-1)],Balance_rate,'C1-',label='Balance')
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        # x_axis[(len(x_axis)-1-len(K)):(len(x_axis)-1)]
        ax33.plot(x_axis[(len(x_axis)-1-len(Closes_rate)):(len(x_axis)-1)],Closes_rate,'C0-',label='Close')
        ax33.plot(x_axis[(len(x_axis)-1-len(Balance_rate)):(len(x_axis)-1)],Balance_rate,'C1-',label='Balance')
        ax33.xaxis.set_ticks(np.arange(0,len(Dates)+1,1.0))
        ax33.set_xticklabels(Cost_axis)
    ax33.legend()
    
    print('Close change: ' + str(Closes_rate[len(Closes_rate)-1]))
    print('Balance change: ' + str(Balance_rate[len(Balance_rate)-1]))
    print('Current grade: ' + str(Gd[-1:]))