# -*- coding: utf-8 -*-

def invest(Closes,analysis,Inv_set):
    # Change = analysis[0]
    RSI = analysis[1]
    # DIF = analysis[2]
    # MACD = analysis[3]
    HIS = analysis[4]
    pDI = analysis[5]
    mDI = analysis[6]
    ADX = analysis[7]
    MA5 = analysis[8]
    MA10= analysis[9]
    MA20= analysis[10]
    K = analysis[11]
    D = analysis[12]
    
    #weight
    rsi_wt = Inv_set[0]
    macd_wt = Inv_set[1]
    adx_wt = Inv_set[2]
    ma5_wt = Inv_set[3]
    ma10_wt = Inv_set[4]
    ma20_wt = Inv_set[5]
    KD_wt = Inv_set[6]
    buy_gauge = Inv_set[7]
    sell_gauge = Inv_set[8]
    
    inv_rate = Inv_set[9]
    
    ini_balance = 100000
    
    # length of indicators
    ana_child_len = []
    for i in [1,4,7,10,11]:
        ana_child_len.append(len(analysis[i]))
    
    Cash = [ini_balance] * min(ana_child_len)
    Inved_amount = [0] * len(Cash)
    Inved_value = [0] * len(Cash)
    Balance = [ini_balance] * len(Cash)
    
    for i in range(1,len(Cash)):
        ## RSI (14)
        rsi_i = i + (len(RSI) - len(Cash))
        
        # 衰減 rsigd
        # if i == 1:
            # rsigd_1 = 0
        #　超売
        if RSI[rsi_i]<25:
            rsigd = 1
        # 弱
        elif RSI[rsi_i]>25 and RSI[rsi_i]<45:
            rsigd = -1
        # 中性
        elif RSI[rsi_i]>45 and RSI[rsi_i]<55:
            rsigd = 0
        # 弱
        elif RSI[rsi_i]>55 and RSI[rsi_i]<75:
            rsigd = 1
        # 超買
        elif RSI[rsi_i]>75:
            rsigd = -1
        # 衰減 rsigd
        # else:
            # rsigd = rsigd_1
        # rsigd_1 = rsigd * 0.8
        
        ## MACD (9,12,26)
        # Cls_i = i + (len(Closes) - len(Cash))
        macd_i = i + (len(HIS) - len(Cash))
        
        # 強
        if HIS[macd_i]>0:
            macdgd = 1
        elif HIS[macd_i]==0:
            macdgd = 0
        elif HIS[macd_i]<0:
            macdgd = -1
            
        ## ADX
        adx_i = i + (len(ADX) - len(Cash))
        
        # 強
        if ADX[adx_i]>=ADX[adx_i-1] :
            # 強
            if pDI[adx_i]>mDI[adx_i]:
                adxgd = 1
            # 弱
            elif pDI[adx_i]<=mDI[adx_i]:
                adxgd = -1
        # 中
        elif ADX[adx_i]<ADX[adx_i-1]:
            adxgd = 0
        
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
            
        kd_i = i + (len(K) - len(Cash))
        if K[kd_i] >= 80:
            kdgd = -.5
        elif K[kd_i] <= 20:
            kdgd = .5
        elif K[kd_i]>20 and K[kd_i]<80:
            if K[kd_i] >= D[kd_i]:
                if K[kd_i-1] >= D[kd_i-1]:
                    kdgd = .5 # 強
                else:
                    kdgd = 1 # 黃金交叉
            else:
                if K[kd_i-1] >= D[kd_i-1]:
                    kdgd = -1 # 死亡交叉
                else:
                    kdgd = -.5 # 弱
            
        
        # investor
        Cls_i = i + (len(Closes) - len(Cash))
        gd = rsigd*rsi_wt + macdgd*macd_wt + adxgd*adx_wt + \
            ma5gd*ma5_wt + ma10gd*ma10_wt + ma20gd*ma20_wt + \
            kdgd*KD_wt
        
        if gd > buy_gauge:
            buyamout = Cash[i-1] * inv_rate
            Cash[i] = Cash[i-1] - buyamout
            Inved_amount[i] = Inved_amount[i-1] + buyamout/Closes[Cls_i]
        elif gd < sell_gauge:
            sellaoumt = Inved_amount[i-1] * inv_rate
            Cash[i] = Cash[i-1] + sellaoumt*Closes[Cls_i]
            Inved_amount[i] = Inved_amount[i-1] - sellaoumt
        else:
            Cash[i] = Cash[i-1]
            Inved_amount[i] = Inved_amount[i-1]
            
        Inved_value[i] = Inved_amount[i] * Closes[Cls_i]
        Balance[i] = Cash[i] + Inved_value[i]
            
    return Balance, Cash, Inved_value