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
    ADX = [0] * (len(Closes)-1)
    pDI = [0] * (len(Closes)-1)
    mDI = [0] * (len(Closes)-1)
        
    # print(pDM)
    for i in range(0,len(Closes)-2):
        ii = len(Closes)-2-i-1
        
        pDM = High[ii] - High[ii+1]
        mDM = Low[ii+1] - Low[ii]
        
        
        if i == 0:
            pDM_1 = max(High[ii+1] - High[ii+2],0)
            mDM_1 = max(Low[ii+2] - Low[ii+1],0)
            if pDM_1 > mDM_1:
                mDM_1 = 0
            elif pDM_1 < mDM_1:
                pDM_1 = 0
            else:
                pDM_1 = 0
                mDM_1 = 0
            TR_1 = max(High[ii+1]-Low[ii+1],
                 abs(High[ii+1]-Closes[ii+2]),
                 abs(Low[ii+1]-Closes[ii+2])
                 )            
            pADM_1 = pDM_1
            mADM_1 = mDM_1
            ATR_1 = TR_1
            
        pDM = max(High[ii] - High[ii+1],0)
        mDM = max(Low[ii+1] - Low[ii],0)
        if pDM > mDM:
            mDM = 0
        elif pDM < mDM:
            pDM = 0
        else:
            pDM = 0
            mDM = 0
        TR = max(High[ii]-Low[ii],
             abs(High[ii]-Closes[ii+1]),
             abs(Low[ii]-Closes[ii+1])
             )
        pADM = pADM_1 + (pDM - pADM_1)/14
        mADM = mADM_1 + (mDM - mADM_1)/14
        ATR = ATR_1 + (TR - ATR_1)/14
        pDI[ii] = pADM / ATR*100
        mDI[ii] = mADM / ATR*100
        if (pDI[ii]+mDI[ii]) == 0:
            DX = 0
        else:
            DX = abs(pDI[ii]-mDI[ii])/(pDI[ii]+mDI[ii])*100
            
        if i == 0:
            ADX[ii] = DX
        else:
            ADX[ii] = ADX[ii+1] + (DX - ADX[ii+1])/14
        
        pADM_1 = pADM
        mADM_1 = mADM
        ATR_1 = ATR
                   
    print(ADX)
        
            
    return Changes, RSI, DIF, MACD, HIS, pDI, mDI, ADX
# if __name__ == "__main__":
    