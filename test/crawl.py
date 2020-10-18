import  requests
import csv
import time
import lxml
from bs4 import BeautifulSoup

'''
# 页面演示代码
wget https://labfile.oss.aliyuncs.com/courses/599/index.html
# 抓取的房源信息
wget https://labfile.oss.aliyuncs.com/courses/599/rent.csv
# 爬虫代码
wget https://labfile.oss.aliyuncs.com/courses/599/crawl.py

'''


url='https://bj.58.com/pinpaigongyu/pn/%7Bpage%7D/?minprice=2000_4000'
page=0
csv_file=open('rent.csv',"w",encoding='utf-8')
csv_writer=csv.writer(csv_file,delimiter=(','))

while True:
    page +=1
    print('fetch:', url.format(page=page))
    time.sleep(1)
    reponse=requests.get(url.format(page=page))
    reponse.encoding='utf-8'
    html=BeautifulSoup(reponse.text,features='lxml')
    print('html', html)
    # house_list=html.find_all("li",{"class":"house"})
    house_list = html.select(".list > li")
    # print('house_list',house_list)
    if not house_list:
        break
    # print('2')
    for house in house_list:
        house_title=house.select("h2")[0].string
        house_url=house.select("a")[0]["herf"]
        house_info_list=house_title.split()
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location=house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money=house.select(".mopney")[0].select("b")[0].string

csv_writer.writerow([house_title,house_location,house_money,house_url])
csv_file.close()









