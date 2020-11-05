# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import invest3 as inv
import plotter

## Inputs
Market = "TW" # TW or US
Code = "2330"
Tick = "30m" # [5m 10m 30m d w m]
Length = -1 # -1: full length
# Inv_setting
rsi_weight = 1
macd_weight = 1
adx_weight = 1
ma5_wt = 1
ma10_wt = 1
ma20_wt = 1
KD_wt = 1

buy_gauge = 1.9
sell_gauge = -1.9
inv_rate = 40 / 100

Inv_set = [rsi_weight ,macd_weight, adx_weight, ma5_wt, ma10_wt,\
           ma20_wt, KD_wt, buy_gauge, sell_gauge, inv_rate]

# ---
date_price = scr.price_scraper(Market, Code, Tick, Length)
Closes = date_price[1]

analysis = ana.analysis(date_price)

Inv_result = inv.invest(Closes, analysis,Inv_set)

plotter.plotter(Tick,date_price,analysis,Inv_result)

