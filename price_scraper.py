# -*- coding: utf-8 -*-

def price_scraper(Market,Code):
    
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
        URL = 'https://tw.stock.yahoo.com/q/ts?s='+ Code +'&t=50'
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
        # retrive date & prices data
        Dates_span = soup.find("table",{"width":"100%"}).findAll("tr",{"bgcolor":"#ffffff"})
        for Data_line in Dates_span:
            Dates_ele = Data_line.findChildren("td")
            Dates.append(datetime.strptime(Dates_ele[0].get_text(),"%H:%M"))
            # print(datetime.strptime(Dates_ele[0].get_text(),"%H:%M"))
        
        # pull close prices
        Nums_td = soup.findAll("td",{"class":["high","low"]})
        for i in range(0, len(Nums_td)):
            if (i % 5) == 3:
                # transfer string to num
                Closes.append(locale.atof(Nums_td[i].get_text()))
            elif (i % 5) == 1:
                High.append(locale.atof(Nums_td[i].get_text()))
            elif (i % 5) == 2:
                Low.append(locale.atof(Nums_td[i].get_text()))

    # print result
    
    return Dates, Closes, High, Low

if __name__ == "__main__":
    
    Market = "US"
    Code = "GOOG"
    result = price_scraper(Market,Code)
    
    print("length of dates:" + str(len(result[0])))
    print("length of close prices:" + str(len(result[1])))
    
    Dates = result[0]
    Closes = result[1]
    
    import matplotlib
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(Dates,Closes)
    # ax = matplotlib.pyplot.plot(Dates,Closes)
    if Market == "US":
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %d"))
    elif Market == "TW":
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    
    