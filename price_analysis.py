# -*- coding: utf-8 -*-

def analysis(date_price):
    # Dates = date_price[0]
    Closes = date_price[1]
    High = date_price[2]
    Low = date_price[3]
    
    Changes = []
    for i in range(0,len(Closes)-1):
        Changes.append(round(Closes[i+1]-Closes[i],2))
    # print("length of price changes:" + str(len(Changes)))
    
    ## RSI (14)
    
    # Close 0123456789
    # Chang 123456789
    # Upsum(3) 3456789  
    Upsum = [0] * (len(Changes)-13)
    Downsum = [0] * len(Upsum)
    RSI = [0] * len(Upsum)
    
    for i in range(0,len(Changes)-13):
        if i == 0:  # first value
            upsum = 0
            downsum = 0
            for j in range(0,13):
                if Changes[i+j] > 0:
                    upsum = upsum + Changes[i+j]
                else:
                    downsum = downsum - Changes[i+j]
            Upsum[i] = upsum / 14
            Downsum[i] = downsum / 14
        else:
            if Changes[i+13] > 0:
                Upsum[i] = (Changes[i+13] + Upsum[i-1] * 12)/13
                Downsum[i] = Downsum[i-1] * 12 / 13
            else:
                Upsum[i] = Upsum[i-1] * 12 / 13
                Downsum[i] = (-Changes[i+13] + Downsum[i-1] * 12)/13
        RSI[i] = Upsum[i] / (Upsum[i] + Downsum[i]) * 100
        
    ## MACD (9,12,26)
    # Close 0123456789
    # DIF(3) (2)3456789
    # MACD(3) (5)6789
    DIF= [0] * (len(Closes)-26)
    MACD= [0] * (len(Closes)-26-9)
    HIS= [0] * (len(Closes)-26-9)
    
    for i in range(0,len(Closes)-26):
        ii = i + 26
        
        if i == 0:  # first EMA value
            #[note] the range [0:3] actually call [0,1,2]
            EMAn_1 = sum(Closes[(ii-12):(ii)])/12
            EMAm_1 = sum(Closes[(ii-26):(ii)])/26
            
        EMAn = (EMAn_1 * (12-1) + Closes[ii] * 2) / (12+1)
        EMAm = (EMAm_1 * (26-1) + Closes[ii] * 2) / (26+1)

        DIF[i] = EMAn - EMAm
        
        # for next loop
        EMAn_1 = EMAn
        EMAm_1 = EMAm        
        
    for i in range(0,len(MACD)):
        ii = i + 9
        
        if i == 0:  # fist MACD value
            MACD_1 = sum(DIF[(ii-9):(ii)])/9
            
        MACD[i] = (MACD_1 * (9-1) + DIF[ii] * 2) / (9+1)
        HIS[i] = DIF[ii] - MACD[i]
        
        # for next loop
        MACD_1 = MACD[i]
        
    
    ## DMI (14,14)
    # Close 0123456789
    # DM 123456789
    # ADM(3) 3456789
    # ADX(3) (6)789
    pDM = []
    mDM = []
    TR = []
    # pDI = [0] * (len(Closes)-14-1)
    # mDI = [0] * (len(Closes)-14-1)
    ADX = [0] * (len(Closes)-28-1)
    
    for i in range(0,len(Closes)-1):
        ii = i + 1
        _pDM = max(High[ii]-High[ii-1],0)
        _mDM = max(Low[ii-1]-Low[ii],0)
        if _pDM > _mDM:
            _mDM = 0
        elif _pDM < _mDM:
            _pDM = 0
        else:
            _pDM = 0
            _mDM = 0
        pDM.append(_pDM)
        mDM.append(_mDM)
        TR.append(max(
            High[ii]-Low[ii],
            abs(High[ii]-Closes[ii-1]),
            abs(Low[ii]-Closes[ii-1])
            ))
        
    pADM = [0] * (len(pDM)-14+1)
    mADM = [0] * len(pADM)
    ATR = [0] * len(pADM)
    pDI = [0] * len(pADM)
    mDI = [0] * len(pADM)
    DX = [0] * len(pADM)

    for i in range(0, len(pDM)-14+1):
        ii = i + 13
        if i == 0:
            pADM[i] = sum(pDM[(ii-13):ii])/14
            mADM[i] = sum(mDM[(ii-13):ii])/14
            ATR[i] = sum(TR[(ii-13):ii])/14
        else:
            pADM[i] = pADM[i-1] + (pDM[ii]-pADM[i-1])/14
            mADM[i] = mADM[i-1] + (mDM[ii]-mADM[i-1])/14
            ATR[i] = ATR[i-1] + (TR[ii]-ATR[i-1])/14
        pDI[i] = pADM[i] / ATR[i]*100
        mDI[i] = mADM[i] / ATR[i]*100
        
        if (pDI+mDI)==0:
            DX[i] = 0
        else:
            DX[i] = abs(pDI[i]-mDI[i])/(pDI[i]+mDI[i])*100
            
    ADX = [0] * (len(DX)-14+1)
    
    for i in range(0, len(ADX)):
        ii = i + 13
        if i == 0:
            ADX[i] = sum(DX[(ii-13):ii])/14
        else:
            ADX[i] = ADX[i-1] + (DX[ii] - ADX[i-1])/14
            
    return Changes, RSI, DIF, MACD, HIS, pDI, mDI, ADX
# if __name__ == "__main__":
    