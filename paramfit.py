def param_fit(Inv_set,Inv_result):
    Balance = Inv_result[0]
    Cash = Inv_result[1]
    Inved_value = Inv_result[2]
    
    Balance_rate = [0] * len(Balance)

    for i in range(0,len(Balance)):
        Balance_rate[i] = Balance[i] / Balance[0]