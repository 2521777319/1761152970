import json
import requests
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
from fake_useragent import UserAgent

head = {'User-Agent': UserAgent().random}
url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
html = requests.get(url,headers = head,timeout = 2)
message = json.loads(html.text)
mes = json.loads(message['data'])
mes_dict = mes["dailyNewAddHistory"]
date=[]
country=[]
hubei=[]
nothubei=[]
n = 0
for d in mes_dict:
        date.append(d['date'])
        country.append(d['country'])
        hubei.append(d['hubei'])
        nothubei.append(d['notHubei'])
        n=n+1
        if n>40:
            break
x = date
y1 = country
y2 = hubei
y3 = nothubei
plt.figure(figsize=(20, 10))
plt.title("Chart of the number of newly confirmed cases per day in February 2020")
plt.xlabel('Date')
plt.ylabel('Number of newly confirmed cases')
plt.bar(x, y2, facecolor = 'pink',edgecolor='white',label='Hubei')
plt.bar(x, y3, facecolor = '#ff9999',edgecolor='white',label ='notHubei')
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.annotate(r"$add\ clinically\ diagnosed\ cases$",xy=('02.12',15153),xycoords='data',xytext=(+30,-100),
              textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
for x, y in zip(x, y1):
    plt.text(x, y+1, y, ha='left')
plt.legend()
plt.show()