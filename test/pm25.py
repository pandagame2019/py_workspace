import requests
from bs4 import BeautifulSoup


url='http://www.pm25x.com/'
html=requests.get(url)
sp1=BeautifulSoup(html.text,'html.parser')
html.encoding='utf-8'
print(sp1)

strs = input('请输入你要查询的城市：')
city=sp1.find('a',{'title':f'{strs}PM2.5'})
citylink=city.get('href')
# print(citylink)


url2=url+citylink
html2=requests.get(url2)
# print(url2)
sp2=BeautifulSoup(html2.text,'html.parser')
# print(sp2)
data1=sp2.select('.aqivalue')
pm25=data1[0].text
print(f'{strs}此时的pm2.5：',pm25)


