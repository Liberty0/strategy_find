# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import invest as inv
import plotter

## Inputs
Market = "TW" # TW or US
Code = "0050"
Tick = "d" # [5m 10m 30m d w m]

date_price = scr.price_scraper(Market, Code, Tick)
Closes = date_price[1]
High = date_price[2]
Low = date_price[3]

analysis = ana.analysis(Closes, High, Low)
RSI = analysis[1]
# DIF = analysis[2]
# MACD = analysis[3]
# HIS = analysis[4]
# pDI = analysis[5]
# mDI = analysis[6]
# ADX = analysis[7]

Inv_result = inv.invest(Closes, RSI)

plotter.plotter(Tick,date_price,analysis,Inv_result)


