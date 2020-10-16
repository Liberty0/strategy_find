# -*- coding: utf-8 -*-

def analysis(Closes, High, Low):
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
    DIF= [0] * (len(Closes)-26)
    HIS= [0] * (len(Closes)-26)
    
    for i in range(0,len(Closes)-26):
        ii = len(Closes)-26-i-2
        
        if i == 0:  # first EMA value
            EMAn_1 = sum(Closes[(ii+1):(ii+12)])/12
            EMAm_1 = sum(Closes[(ii+1):(ii+26)])/26
            
        EMAn = (EMAn_1 * (12-1) + Closes[ii] * 2) / (12+1)
        EMAm = (EMAm_1 * (26-1) + Closes[ii] * 2) / (26+1)

        DIF[ii] = EMAn - EMAm
        
        if i == 0:  # fist MACD value
            MACD_1 = DIF[ii]
        MACD[ii] = (MACD_1 * (9-1) + DIF[ii] * 2) / (9+1)
        HIS[ii] = DIF[ii] - MACD[ii]
        
        # for next loop
        EMAn_1 = EMAn
        EMAm_1 = EMAm
        MACD_1 = MACD[ii]
    
    
    ## DMI (14,14)
    DX = [0] * (len(Closes)-14)
    ADX = [0] * (len(Closes)-14)
    pDI = [0] * (len(Closes)-14)
    mDI = [0] * (len(Closes)-14)
    pDM = [0] * (len(Closes)-14)
    mDM = [0] * (len(Closes)-14)
    pADM = [0] * (len(Closes)-14)
    mADM = [0] * (len(Closes)-14)
    TR = [0] * (len(Closes)-14)
    ATR = [0] * (len(Closes)-14)
        
    for i in range(0,len(Closes)-14):
        ii = len(Closes)-14-i-1
        
        pDM[ii] = High[ii] - High[ii+1]
        if pDM[ii] < 0:
            pDM[ii] = 0
        mDM[ii] = Low[ii+1] - Low[ii]
        if mDM[ii] < 0:
            mDM[ii] = 0
        
        if pDM[ii] > mDM[ii]:
            mDM[ii] = 0
        elif mDM[ii] > pDM[ii]:
            pDM[ii] = 0
        elif pDM[ii] == mDM[ii]:
            pDM[ii] = 0
            mDM[ii] = 0
        
        TR[ii] = max(High[ii]-Low[ii],
                     abs(High[ii]-Closes[ii+1]),
                     abs(Low[ii]-Closes[ii+1])
                     )
        
    # print(pDM)
    for i in range(0,len(Closes)-15):
        ii = len(Closes)-15-i-1
        
        if i == 0:
            
            pADM[ii] = pDM[ii]
            mADM[ii] = mDM[ii]
            ATR[ii] = TR[ii]
        else:
            pADM[ii] = pADM[ii+1] + (pDM[ii]-pADM[ii+1])/14
            mADM[ii] = mADM[ii+1] + (mDM[ii]-mADM[ii+1])/14
            ATR[ii] = ATR[ii+1] + (TR[ii]-ATR[ii+1])/14
            
        pDI[ii] = pADM[ii]/ATR[ii]*100
        mDI[ii] = mADM[ii]/ATR[ii]*100
        
        if (pDI[ii] + mDI[ii]) == 0:
            DX[ii] = 0
        else:
            DX[ii] = abs(pDI[ii]-mDI[ii])/(pDI[ii]+mDI[ii])*100
            
    for i in range(0,len(Closes)-16):
        ii = len(Closes)-16-i-1
        
        if i == 0:
            ADX[ii] = DX[ii]
        else:
            ADX[ii] = ADX[ii+1] + (DX[ii]-ADX[ii+1])/14
        
            
    return Changes, RSI, DIF, MACD, HIS, pDI, mDI, ADX
# if __name__ == "__main__":
    