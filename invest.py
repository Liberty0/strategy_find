# -*- coding: utf-8 -*-

def invest(Closes,analysis):
    # Change = analysis[0]
    RSI = analysis[1]
    # DIF = analysis[2]
    # MACD = analysis[3]
    HIS = analysis[4]
    pDI = analysis[5]
    mDI = analysis[6]
    ADX = analysis[7]
    
    rsi_weight = 5
    macd_weight = 3
    adx_weight = 3
    inv_gauge = 1.5
    inv_rate = 25 / 100
    
    ini_balance = 100000
    Cash = [ini_balance] * min(len(Closes),len(RSI),len(HIS),len(ADX))
    Inved_amount = [0] * len(Cash)
    Inved_value = [0] * len(Cash)
    Balance = [ini_balance] * len(Cash)
    
    for i in range(1,len(Cash)):
        # RSI
        rsi_i = i + (len(RSI) - len(Cash))
        
        if i == 1:
            rsigd_1 = 0
        if RSI[rsi_i] < 40:
            rsigd = 1
        elif RSI[rsi_i] > 80:
            rsigd = -1
        else:
            rsigd = rsigd_1
        rsigd_1 = rsigd * 0.8
        
        # MACD
        macd_i = i + (len(HIS) - len(Cash))
        
        if i == 1:
            macdgd_1 = 0
        if (HIS[macd_i]>0) and (HIS[macd_i-1]<0):
            macdgd = 1
        elif (HIS[macd_i]<0) and (HIS[macd_i-1]>0):
            macdgd = -1
        else:
            macdgd = macdgd_1 *0.8
        macdgd_1 = macdgd
        
        # ADX
        adx_i = i + (len(ADX) - len(Cash))
        
        if i == 1:
            adxgd_1 = 0
        if ADX[adx_i]>25:
            if (pDI[adx_i]-mDI[adx_i]) > 0:
                adxgd = 1
            elif (pDI[adx_i]-mDI[adx_i]) < 0:
                adxgd = -1
        else:
            adxgd = adxgd_1 * 0.8
        adxgd_1 = adxgd
        
        # investor
        Cls_i = i + (len(Closes) - len(Cash))
        gd = rsigd*rsi_weight + macdgd*macd_weight + adxgd*adx_weight
        
        if gd > inv_gauge:
            buyamout = Cash[i-1] * inv_rate
            Cash[i] = Cash[i-1] - buyamout
            Inved_amount[i] = Inved_amount[i-1] + buyamout/Closes[Cls_i]
        elif gd < inv_gauge:
            sellaoumt = Inved_amount[i-1] * inv_rate
            Cash[i] = Cash[i-1] + sellaoumt*Closes[Cls_i]
            Inved_amount[i] = Inved_amount[i-1] - sellaoumt
        else:
            Cash[i] = Cash[i-1]
            Inved_amount[i] = Inved_amount[i-1]
            
        Inved_value[i] = Inved_amount[i] * Closes[Cls_i]
        Balance[i] = Cash[i] + Inved_value[i]
            
    return Balance, Cash, Inved_value