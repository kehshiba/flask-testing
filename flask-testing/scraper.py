import re,requests
import csv
from bs4 import BeautifulSoup

def scr(link):
    rows=[]
    header={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link)
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(urls)):
            data= requests.get(urls[i],headers=header)
            soup = BeautifulSoup(data.text,'html.parser')
            html = BeautifulSoup(soup.text,'html.parser')
            body= BeautifulSoup(html.text,'html.parser')
            productname = soup.find('h1', {'id' : 'title'}).text
            productprice = soup.find('span',{'class':'a-price-whole'}).text
            productrating = soup.find('span',{'class':'a-size-medium a-color-base'}).text
            rows.append([productname.strip(),productprice.strip(),productrating.strip()])
        writer.writerow(['Name','Price','Rating'])
        writer.writerows(rows)      
    return rows