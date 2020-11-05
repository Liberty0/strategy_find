# strategy_find
technical analysis and evaluate strategy with historical prices

## Index grading

### MA
弱轉強 / 強轉弱  
MA - 昨MA > / < 0  
昨MA - 前MA < / > 0

強/弱  
MA - 昨MA > / < 0  
昨MA - 前MA >= / <= 0

中  
MA - 昨MA = 0
  
### RSI (14)
超買:
RSI值>75
代表市場快速上漲，要評估是否趨勢可能反轉向下、賣出訊號。

---
強:
55<RSI<75

中性:
45<RSI<55

弱:
25<RSI<45

---

超賣:
RSI值<25
代表市場快速下跌，要評估是否趨勢可能反轉向上，買進訊號。

鈍化： 連續 >75 或 <25 超過7天，表上漲/下跌趨勢強烈，反轉為買進/賣出訊號

RSI下跌背離(Bearish RSI Divergence)：股價創新高，但同期RSI指數向下走 (意味著上漲力道較之前減弱)，認為未來會往下，通常只在空頭市場回檔時有效。

RSI上漲背離(Bullish RSI Divergence)：股價創新低，但同期RSI指數向上走 (意味著下跌力道較之前減弱)，認為未來會往上，通常只在多頭市場回檔時有效。

### MACD (9,12,26)
黃金/死亡交叉: 柱狀圖正負翻轉，由負向正翻轉為買進訊號，反之為賣出

背離：
背離通常是因為股價在短期內快速上漲或是下跌，讓指標來不及反應價格的趨勢。
如果股價創新低，但快線卻上升，稱為「多頭背離」，一般認為是買進訊號。
如果股價創新高，但快線卻下降，稱為「空頭背離」，一般認為是賣出訊號。

強/中/弱:
OSC(柱狀圖,oscillator) (>/=/<) 0

### ADX DMI (14,14)
ADX 表趨勢強弱，上升突破25時：
+DI > -DI： 上升趨勢成形，買進訊號
-DI < +DI： 下降趨勢成形，賣出訊號

### KD (9)

超買: K > 80
超賣: K < 20
強: 20<K<80 & K>D & 昨K>昨D
弱: 20<K<80 & K<D & 昨K<昨D
黃金交叉: 20<K<80 & K>D & 昨K<昨D
死亡交叉: 20<K<80 & K<D & 昨K>昨D

**inv 與 inv3 中判讀不同**
inv: 超買賣 -+.5 | 金死叉 +-1衰減
inv3:超買賣 -+.5 | 金死叉 +-1 | 強弱 +-.5


## Reference
https://rich01.com/rsi-index-review/    
https://rich01.com/what-is-macd-indicator/
