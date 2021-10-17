# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import paramfit as parfit
import plotter

## Inputs
Market = "TW" # TW or US
Code = "2330"
Tick = "5m" # [5m 10m 30m d w m]
Length = -1 # -1: full length
# Inv_setting
# 權重 & 衰減係數
rsi_weight = 3
macd_weight = 0
adx_weight = 0
ma5_wt = 1
ma10_wt = 1
ma20_wt = 1
KD_wt = 0
KD_dp = 0.8
CCO_wt = 0

buy_gauge = 50  # /100
sell_gauge = -50
inv_rate = 40 / 100

Inv_set = [[rsi_weight ,macd_weight, adx_weight, ma5_wt, ma10_wt,\
           ma20_wt, KD_wt, CCO_wt, buy_gauge, sell_gauge,\
            inv_rate],\
           [0,0,0,0,0,\
            0,KD_dp,0,0,0,\
            0]]
           

# ---
date_price = scr.price_scraper(Market, Code, Tick, Length)

analysis = ana.analysis(date_price)

# Inv_result = inv.invest(date_price, analysis,Inv_set)

fitresult = parfit.param_fit(date_price, analysis,Inv_set)

Fit_param = fitresult[0]
Balance_rate_try = fitresult[1]
Inv_result = fitresult[2]
print(Fit_param)
print(Balance_rate_try)

plotter.plotter(Tick,date_price,analysis,Inv_result)

