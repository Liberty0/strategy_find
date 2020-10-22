# -*- coding: utf-8 -*-

def price_scraper(Market='TW',Code='2330',Tick='5m'):
    
    import requests 
    from bs4 import BeautifulSoup
    from datetime import  datetime
    # import matplotlib
    import locale
    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
    
    # scrap data
    if Market == "US":
        URL = 'https://finance.yahoo.com/quote/GOOG/history?p='+Code
    elif Market == "TW":
        URL = 'https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd='+ Tick +'&mkt=10&sym='+ Code +'&v=1'
    else:
        print('Invalid "Market"')
        return -1
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')  
    
    Dates = []
    Closes = []
    High =[]
    Low =[]
    
    # retrive date & prices data
    Dates_span = soup.findAll(class_="Py(10px) Ta(start) Pend(10px)")
    Nums_td = soup.findAll(class_="Py(10px) Pstart(10px)")
    
    if Market == "US":
        # parse date string
        for i in range(0,len(Dates_span)):
            Dates.append(datetime.strptime(Dates_span[i].get_text(),"%b %d, %Y"))
            #print(Dates_span[i].get_text())
        
        # Dates = matplotlib.dates.date2num(Dates_str)
        # attract close prices
        for i in range(0, len(Nums_td)):
            if (i % 6)==3:
                # transfer string to num
                Closes.append(locale.atof(Nums_td[i].get_text()))
            elif (i%6)==1:
                High.append(locale.atof(Nums_td[i].get_text()))
            elif (i%6) ==2:
                Low.append(locale.atof(Nums_td[i].get_text()))
                
    elif Market == "TW":
        fulltext = soup.get_text() # datetime, open, high, low, close, variation
        sectionsplit = fulltext.split('[')
        timesplit = sectionsplit[1].split("{")
        for i in range(0,len(timesplit)):
            itemsplit = timesplit[i].split(':')
            for j in range(0, len(itemsplit)):
                valuesplit = itemsplit[j].split(',')
                if j == 1:
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
        # print result
    
    return Dates, Closes, High, Low

if __name__ == "__main__":
    
    Market = "TW"
    Code = "2330"
    result = price_scraper(Market,Code)
    
    print("length of dates:" + str(len(result[0])))
    print("length of close prices:" + str(len(result[1])))
    
    Dates = result[0]
    Closes = result[1]
    
    import matplotlib
    fig, ax = matplotlib.pyplot.subplots()
    
    # ax = matplotlib.pyplot.plot(Dates,Closes)
    if Market == "US":
        ax.plot(Dates,Closes)
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Market == "TW":
        ax.plot(Closes)
        # ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    
    