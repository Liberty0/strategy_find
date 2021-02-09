# -*- coding: utf-8 -*-

def invest(date_price,analysis,Inv_set):
    
    Closes = date_price[1]
    
    # Change = analysis[0]
    RSI = analysis[1]
    # DIF = analysis[2]
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

    #weight
    rsi_wt = Inv_set[0][0]
    macd_wt = Inv_set[0][1]
    adx_wt = Inv_set[0][2]
    ma5_wt = Inv_set[0][3]
    ma10_wt = Inv_set[0][4]
    ma20_wt = Inv_set[0][5]
    KD_wt = Inv_set[0][6]
    CCO_wt = Inv_set[0][7]
    buy_gauge = Inv_set[0][8]
    sell_gauge = Inv_set[0][9]
    
    inv_rate = Inv_set[0][10]
    
    ini_balance = 100000
    total_score = sum(Inv_set[0][0:6+1])
    buy_score = buy_gauge/100
    sell_score = sell_gauge/100
    
    # length of indicators
    # print(len(analysis))
    ana_child_len = []
    for i in range(0,len(analysis)):
        ana_child_len.append(len(analysis[i]))
    
    Cash = [ini_balance] * min(ana_child_len)
    Grades = []
    Inved_amount = [0] * len(Cash)
    Inved_value = [0] * len(Cash)
    Balance = [ini_balance] * len(Cash)
    
    for i in range(1,len(Cash)):
        ## RSI (14)
        rsi_i = i + (len(RSI) - len(Cash))
        
        if i == 1:
            rsigd_1 = 0
        #　買売超区間 (OverBuy OverSell zone)
        if RSI[rsi_i]<30:
            rsigd = 1
        elif RSI[rsi_i] > 70:
            rsigd = -1
        # 鈍化
        elif max(RSI[(rsi_i-7):rsi_i])<30:
            rsigd = -1
        elif min(RSI[(rsi_i-7):rsi_i])>70:
            rsigd = 1
        # 背離
        
        else:
            rsigd = rsigd_1
        rsigd_1 = rsigd * 0.8
        
        ## MACD (9,12,26)
        Cls_i = i + (len(Closes) - len(Cash))
        macd_i = i + (len(HIS) - len(Cash))
        
        if i == 1:
            macdgd_1 = 0
        # 背離
        if Closes[Cls_i]==max(Closes[0:(Cls_i+1)]) and MACD[macd_i]<MACD[macd_i]:
            macdgd = -2
        elif Closes[Cls_i]==min(Closes[0:(Cls_i+1)]) and MACD[macd_i]>MACD[macd_i]:
            macdgd = 2
        # 交差
        elif HIS[macd_i]>0 and HIS[macd_i-1]<0 and macdgd_1<1:
            macdgd = 1
        elif HIS[macd_i]<0 and HIS[macd_i-1]>0:
            macdgd = -1
        else:
            macdgd = macdgd_1 *0.8
        macdgd_1 = macdgd
        
        ## ADX
        adx_i = i + (len(ADX) - len(Cash))
        
        if i == 1:
            adxgd_1 = 0
        if ADX[adx_i]>25 and ADX[adx_i-1]<25:
            if (pDI[adx_i]-mDI[adx_i]) > 0:
                adxgd = 1
            elif (pDI[adx_i]-mDI[adx_i]) < 0:
                adxgd = -1
        else:
            adxgd = adxgd_1 * 0.8
        adxgd_1 = adxgd
        
        # MA
        ma5_i = i + (len(MA5) - len(Cash))
        ma10_i = i + (len(MA10) - len(Cash))
        ma20_i = i + (len(MA20) - len(Cash))
        
        # raise and turn up
        if MA5[ma5_i] > MA5[ma5_i-1]:
            ma5gd = 1
        # fall and turn down
        elif MA5[ma5_i] < MA5[ma5_i-1]:
            ma5gd = -1
        else:
            ma5gd = 0
        
                # raise and turn up
        if MA10[ma10_i] > MA10[ma10_i-1]:
            ma10gd = 1
        # fall and turn down
        elif MA10[ma10_i] < MA10[ma10_i-1]:
            ma10gd = -1
        else:
            ma10gd = 0
            
                # raise and turn up
        if MA20[ma20_i] > MA20[ma20_i-1]:
            ma20gd = 1
        # fall and turn down
        elif MA20[ma20_i] < MA20[ma20_i-1]:
            ma20gd = -1
        else:
            ma20gd = 0
            
        # KD
        kd_i = i + (len(K) - len(Cash))
        
        if i == 1:
            kdgd_1 = 0
            
        if K[kd_i] >= 80:
            kdgd = -.5 # 超買
        elif K[kd_i] <= 20:
            kdgd = .5 # 超賣
        elif K[kd_i]>20 and K[kd_i]<80:
            if K[kd_i] >= D[kd_i] and K[kd_i-1] <= D[kd_i-1]:
                kdgd = 1 # 黃金交叉
            elif K[kd_i] <= D[kd_i] and K[kd_i-1] >= D[kd_i-1]:
                kdgd = -1 # 死亡交叉
            else:
                kdgd = kdgd_1 * .8 # 訊號衰減
        kdgd_1 = kdgd
                
        # CCO
        CCO_i = i + (len(CCO) - len(Cash))
        
        if i == 1:
            CCOgd_1=0
        ## 評分法待定
        CCOgd = 0
        
        
        ## investor
        # Cls_i = i + (len(Closes) - len(Cash))
        gd = (rsigd*rsi_wt + macdgd*macd_wt + adxgd*adx_wt + \
            ma5gd*ma5_wt + ma10gd*ma10_wt + ma20gd*ma20_wt + \
            kdgd*KD_wt + CCOgd*CCO_wt)\
            /total_score
        
        if gd > buy_score:
            buyamout = Cash[i-1] * inv_rate
            Cash[i] = Cash[i-1] - buyamout
            Inved_amount[i] = Inved_amount[i-1] + buyamout/Closes[Cls_i]
        elif gd < sell_score:
            sellaoumt = Inved_amount[i-1] * inv_rate
            Cash[i] = Cash[i-1] + sellaoumt*Closes[Cls_i]
            Inved_amount[i] = Inved_amount[i-1] - sellaoumt
        else:
            Cash[i] = Cash[i-1]
            Inved_amount[i] = Inved_amount[i-1]
            
        Inved_value[i] = Inved_amount[i] * Closes[Cls_i]
        Balance[i] = Cash[i] + Inved_value[i]
        Grades.append([gd,rsigd,macdgd,adxgd,ma5gd,ma10gd,ma20gd,kdgd,CCOgd])
    # print(len(Grades))
            
    return Balance, Cash, Inved_value, Grades