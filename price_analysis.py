# -*- coding: utf-8 -*-


def analysis(Closes):
    Changes = []
    for i in range(0,len(Closes)-1):
        Changes.append(round(Closes[i]-Closes[i+1],2))
    # print("length of price changes:" + str(len(Changes)))
    
    ## RSI (14)
    Upsum = [0] * (len(Changes)-13)
    Downsum = [0] * len(Upsum)
    RSI = [0] * len(Upsum)
    for i in range(0,len(Changes)-13):
        ii = len(Changes)-13-i-1
        
        if i == 0:  # first value
            # print("first ii:" + str(ii))
            upsum = 0
            downsum = 0
            for j in range(0,13):
                if Changes[ii+j] > 0:
                    upsum = upsum + Changes[ii+j]
                else:
                    downsum = downsum - Changes[ii+j]
            Upsum[ii] = upsum
            Downsum[ii] = downsum
        elif ii > -1: # smooth RSI
            if Changes[ii] > 0:
                Upsum[ii] = (Changes[ii] + Upsum[ii+1] * 12)/13
                Downsum[ii] = Downsum[ii+1] * 12 / 13
            else:
                Upsum[ii] = Upsum[ii+1] * 12 / 13
                Downsum[ii] = (-Changes[ii] + Downsum[ii+1] * 12)/13
                    
        RSI[ii] = Upsum[ii] / (Upsum[ii] + Downsum[ii]) * 100
        
    ## MACD (9,12,26)
    MACD= [0] * (len(Closes)-26)
    
    for i in range(0,len(Closes)-26):
        ii = len(Closes)-26-i-2
        
        if i == 0:  # first EMA value
            EMAn_1 = sum(Closes[(ii+1):(ii+12)])/12
            EMAm_1 = sum(Closes[(ii+1):(ii+26)])/26
            
        EMAn = (EMAn_1 * (12-1) + Closes[ii] * 2) / (12+1)
        EMAm = (EMAm_1 * (26-1) + Closes[ii] * 2) / (26+1)

        DIF = EMAn - EMAm
        
        if i == 0:  # fist MACD value
            MACD_1 = DIF
        MACD[ii] = (MACD_1 * (9-1) + DIF * 2) / (9+1)
        
        # for next loop
        EMAn_1 = EMAn
        EMAm_1 = EMAm
        MACD_1 = MACD[ii]
    
    print(MACD)
    return Changes, RSI, MACD
# if __name__ == "__main__":
    