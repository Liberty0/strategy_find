# -*- coding: utf-8 -*-

def price_scraper(Market='TW',Code='2330',Tick='5m'):
    
    import requests 
    from bs4 import BeautifulSoup
    from datetime import  datetime
    import matplotlib
    import locale
    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
    
    # scrap data
    URL = 'https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd='+ Tick +'&mkt=10&sym='+ Code +'&v=1'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')  
    
    Dates_str = []
    Dates = []
    Closes = []
    High = []
    Low = []
    
    fulltext = soup.get_text() # datetime, open, high, low, close, variation
    sectionsplit = fulltext.split('[')
    timesplit = sectionsplit[1].split("{")
    for i in range(0,len(timesplit)):
        itemsplit = timesplit[i].split(':')
        for j in range(0, len(itemsplit)):
            valuesplit = itemsplit[j].split(',')
            if j == 1:
                Dates_str.append(valuesplit[0])
                if Tick=='d' or Tick=='w' or Tick=='m':
                    Dates.append(datetime.strptime(valuesplit[0],"%Y%m%d"))
                elif Tick=='5m' or Tick=='10m' or Tick=='30m':
                    Dates.append(datetime.strptime(valuesplit[0],"%Y%m%d%H%M"))
                
            elif j == 5:
                Closes.append(locale.atof(valuesplit[0]))
            elif j == 3:
                High.append(locale.atof(valuesplit[0]))
            elif j == 4:
                Low.append(locale.atof(valuesplit[0])) 
            # print(itemsplit[j].split(','))
    
    # print(Dates)
    
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(Dates,Closes)
    if Tick=='d' or Tick=='w' or Tick=='m':
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Tick=='5m' or Tick=='10m' or Tick=='30m':
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    
    fig2 = matplotlib.pyplot.figure()  
    ax2 = fig2.add_subplot()
    ax2.plot(Closes)
    
    # return Dates_str, Closes, High, Low

if __name__ == "__main__":
    result = price_scraper()
    
    # print("length of dates:" + str(len(result[0])))
    # print("length of close prices:" + str(len(result[1])))

