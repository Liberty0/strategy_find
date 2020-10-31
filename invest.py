# -*- coding: utf-8 -*-

def invest(Closes,analysis,Inv_set):
    # Change = analysis[0]
    RSI = analysis[1]
    # DIF = analysis[2]
    MACD = analysis[3]
    HIS = analysis[4]
    pDI = analysis[5]
    mDI = analysis[6]
    ADX = analysis[7]
    
    rsi_weight = Inv_set[0]
    macd_weight = Inv_set[1]
    adx_weight = Inv_set[2]
    buy_gauge = Inv_set[3]
    sell_gauge = Inv_set[4]
    
    inv_rate = Inv_set[5]
    
    ini_balance = 100000
    Cash = [ini_balance] * min(len(Closes),len(RSI),len(HIS),len(ADX))
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
        # rsigd_1 = rsigd * 0.8
        
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
        elif HIS[macd_i]>0 and HIS[macd_i-1]<0:
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
        
        # investor
        # Cls_i = i + (len(Closes) - len(Cash))
        gd = rsigd*rsi_weight + macdgd*macd_weight + adxgd*adx_weight
        
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