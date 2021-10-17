import invest as inv

def param_fit(date_price, analysis,Inv_set):
    
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
    
    Inv_result = inv.invest(date_price, analysis,Inv_set)
    Balance = Inv_result[0]
    Balance_rate_ref = Balance[-1]/Balance[0]
    
    i = 0 # No. attempts
    Balance_rate_try = Balance_rate_ref-1
    while Balance_rate_try<Balance_rate_ref and i<50:
        Balance_rate_ref = Balance_rate_try # compare new try with current result
        rsi_wt += 1 # fitting attempt
        
        Inv_set[0][0] = rsi_wt
        
        Inv_result = inv.invest(date_price, analysis,Inv_set)
        Balance = Inv_result[0]
        Balance_rate_try = Balance[-1]/Balance[0]
        
        i += 1
    
    if i == 50:
        print('max attempts reached')
    else:
        print('fitting done')
        
    return Inv_set, Inv_result, Balance_rate_try
    # print(Inv_set)
    # print(Balance_rate_try)