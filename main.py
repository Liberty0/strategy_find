# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import invest as inv
import inv_plot as invp
import paramfit as parfit
import plotter

## Inputs
Market = "TW" # TW or US
Code = "2330"
Tick = "30m" # [5m 10m 30m d w m]
Length = -1 # -1: full length
# Inv_setting
# 權重 & 衰減係數
rsi_weight = 3
rsi_dp = 0.8
macd_weight = 0
macd_dp = 0.8
adx_weight = 0
adx_dp = 0.8
ma5_wt = 1
ma10_wt = 1
ma20_wt = 1
KD_wt = 0
KD_dp = 0.8 # demping coeffecient 
CCO_wt = 0

buy_gauge = 50  # /100
sell_gauge = -50
inv_rate = 40 / 100

switch_fit = 0

Inv_set = [[rsi_weight ,macd_weight, adx_weight, ma5_wt, ma10_wt,\
           ma20_wt, KD_wt, CCO_wt, buy_gauge, sell_gauge,\
            inv_rate],\
           [rsi_dp,macd_dp,adx_dp,0,0,\
            0,KD_dp,0,0,0,\
            0]]
           
# ---
date_price = scr.price_scraper(Market, Code, Tick, Length)

analysis = ana.analysis(date_price)

if switch_fit == 1:
    fitresult = parfit.param_fit(date_price, analysis,Inv_set)
    Fit_param = fitresult[0]
    Inv_result = fitresult[1]
    Balance_rate = fitresult[2]
    plotter.plotter(Tick,date_price,analysis,Inv_result)
    print('Fitted Parameter:' + str(Fit_param[0]))
    # print('Close change:' + str(Balance_rate))
else:
    Inv_result = inv.invest(date_price, analysis,Inv_set)
    invp.invplot(Tick,date_price,Inv_result)


