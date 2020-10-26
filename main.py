# -*- coding: utf-8 -*-

import price_scraper as scr
import price_analysis as ana
import invest as inv
import plotter

## Inputs
Market = "TW" # TW or US
Code = "0050"
Tick = "30m" # [5m 10m 30m d w m]

date_price = scr.price_scraper(Market, Code, Tick)
Closes = date_price[1]

analysis = ana.analysis(date_price)

Inv_result = inv.invest(Closes, analysis)

plotter.plotter(Tick,date_price,analysis,Inv_result)

