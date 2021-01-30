# -*- coding: utf-8 -*-

def price_scraper(Market='TW',Code='2330',Tick='d',Length=-1):
    
    import requests 
    from bs4 import BeautifulSoup
    from datetime import  datetime
    import re
    # import matplotlib
    import locale
    locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
    
    # scrap data
    if Market == "US":
        # https://query1.finance.yahoo.com/v8/finance/chart/GOOG?symbol=GOOG&period1=1529852400&period2=1604156132&interval=1d&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=a8owf8rmWfk&corsDomain=finance.yahoo.com
        URL = 'https://query1.finance.yahoo.com/v8/finance/chart/'+ Code + '?period1=1529852400&period2=1604156132&interval=1d&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=a8owf8rmWfk&corsDomain=finance.yahoo.com'
    elif Market == "TW":
        # https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=5m&mkt=10&sym=2330&v=1
        URL = 'https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd='+ Tick +'&mkt=10&sym='+ Code +'&v=1'
    else:
        print('Invalid "Market"')
        return -1
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    print('data loading')
    page = requests.get(URL, headers=headers)
    print('data load')
    soup = BeautifulSoup(page.content, 'html.parser')  
    
    Dates = []
    Closes = []
    High =[]
    Low =[]
    Volume = []
    
    
    if Market == "US":
        # retrive date & prices data
        Dates_span = soup.findAll(class_="timestamp")
        Nums_td = soup.findAll(class_="close")
        
        print(Dates_span)
        return -1

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
            elif (i%6) ==4: # didn't confirm
                Volume.append(locale.atof(Nums_td[i].get_text()))
                
    elif Market == "TW":

        fulltext = soup.get_text() # datetime, open, high, low, close, variation
        sectionsplit = fulltext.split('[')
        timesplit = re.split('{|},{|}',sectionsplit[1])
        print('data splited')
        # timesplit = sectionsplit[1].split("{")
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
                elif j == 6:
                    Volume.append(locale.atof(valuesplit[0]))
    
    if not Length == -1:
        Length = min(Length,len(Dates))
        Dates = Dates[(len(Dates)-Length):len(Dates)]
        Closes = Closes[(len(Closes)-Length):len(Closes)]
        
    return Dates, Closes, High, Low, Volume

if __name__ == "__main__":
    
    Market = "TW"
    Code = "2330"
    Tick = 'd'
    Length = -1
    result = price_scraper(Market,Code,Tick,Length)
    
    print("length of dates:" + str(len(result[0])))
    print("length of close prices:" + str(len(result[1])))
    
    Dates = result[0]
    Closes = result[1]
    print(Dates)
    
    import matplotlib
    fig, ax = matplotlib.pyplot.subplots()
    
    # ax = matplotlib.pyplot.plot(Dates,Closes)
    if Market == "US":
        ax.plot(Dates,Closes)
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Market == "TW":
        ax.plot(Closes)
        # ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    
    