# -*- coding: utf-8 -*-

def price_scraper(Market='TW',Code='2330',Tick='d'):
    
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
    
    # findsoup = soup.findAll("ta")
    fulltext = soup.get_text()
    print(len(fulltext))
    # print(findsoup)
    # retrive date & prices data
    # Dates_span = soup.find("table",{"width":"100%"}).findAll("tr",{"bgcolor":"#ffffff"})
    # for Data_line in Dates_span:
    #     Dates_ele = Data_line.findChildren("td")
    #     Dates.append(datetime.strptime(Dates_ele[0].get_text(),"%H:%M"))
        # print(datetime.strptime(Dates_ele[0].get_text(),"%H:%M"))
    
    # pull close prices
    # Nums_td = soup.findAll("td",{"class":["high","low"]})
    # for i in range(0, len(Nums_td)):
    #     if (i % 5) == 3:
    #         # transfer string to num
    #         Closes.append(locale.atof(Nums_td[i].get_text()))
    #     elif (i % 5) == 1:
    #         High.append(locale.atof(Nums_td[i].get_text()))
    #     elif (i % 5) == 2:
    #         Low.append(locale.atof(Nums_td[i].get_text()))
            
    # fig, ax = matplotlib.pyplot.subplots()
    # ax.plot(Dates,Closes)
    # ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    
    # return Dates_str, Closes, High, Low

if __name__ == "__main__":
    result = price_scraper("TW","2330","d")
    
    # print("length of dates:" + str(len(result[0])))
    # print("length of close prices:" + str(len(result[1])))

