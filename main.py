# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import invest as inv
import plotter

## Inputs
Market = "TW" # TW or US
Code = "0050"
Tick = "d" # [5m 10m 30m d w m]
Length = -1
# Inv_setting
rsi_weight = 0
macd_weight = 1
adx_weight = 1
buy_gauge = 0.9
sell_gauge = -0.9
inv_rate = 40 / 100

Inv_set = [rsi_weight,macd_weight,adx_weight,buy_gauge,sell_gauge,inv_rate]

# ---
date_price = scr.price_scraper(Market, Code, Tick, Length)
Closes = date_price[1]

analysis = ana.analysis(date_price)

Inv_result = inv.invest(Closes, analysis,Inv_set)

plotter.plotter(Tick,date_price,analysis,Inv_result)

