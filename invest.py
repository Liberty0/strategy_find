# -*- coding: utf-8 -*-

def invest(Closes,RSI):
    
    inv_gauge = 0
    inv_rate = 25 / 100
    
    ini_balance = 100000
    Cash = [ini_balance] * min(len(Closes),len(RSI))
    Inved_amount = [0] * len(Cash)
    Inved_value = [0] * len(Cash)
    Balance = [ini_balance] * len(Cash)
    
    for i in range(1,len(Cash)):
        rsi_i = i + (len(RSI) - len(Cash))
        if RSI[rsi_i] < 40:
            rsigd = 1
        elif RSI[rsi_i] > 80:
            rsigd = -1
        else:
            rsigd = 0
        
        Cls_i = i + (len(Closes) - len(Cash))
        gd = rsigd
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