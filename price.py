import grequests
import gevent
from gevent import monkey as curious_george
curious_george.patch_all(thread=False, select=False)
import requests
from flask import Flask, render_template, request
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import asyncio
import time

class PriceData(object):
    def __init__(self, page_num, Item):
        self.num_page = page_num
        self.content = []
        self.item = Item

    #定義協程(coroutine)
    async def main(self):
        links = list()
        for page in range(1, self.page_num):
            links.append("https://www.findprice.com.tw/g/{}/?i={}".format(self.item, str(page)))

        async with ClientSession() as session:
            tasks = [asyncio.create_task(self.fetch(link, session)) for link in links]  # 建立任務清單
            await asyncio.gather(*tasks)  # 打包任務清單及執行

    #定義協程(coroutine)
    async def fetch(self, link, session):
        async with session.get(link) as response:  #非同步發送請求
            html_body = await response.text()

            soup = BeautifulSoup(html_body, "html.parser")  # 解析HTML原始碼

            products = soup.find_all("a", class_="ga")
            prices = soup.find_all("span", class_="rec-price-20")
            print(1111111)
            for product, price in zip(products, prices):
                print(product.getText(), price.getText())
                self.content.append([product.getText(), price.getText()])

    def work(self):
        loop = asyncio.get_event_loop()  #建立事件迴圈(Event Loop)
        loop.run_until_complete(self.main())  #執行協程(coroutine)
        for p, pc in self.content[:10]:
            print(p, pc)
        return self.content
#print(response.text)

def getItemPrice(pages, itemName):
    links = list()  # 請求網址清單(1-pages頁的網址)
    content = []
    for page in range(1, pages):
        links.append("https://www.findprice.com.tw/g/{}/?i={}".format(itemName, str(page)))

    reqs = (grequests.get(link) for link in links)  # 建立請求集合
    response = grequests.imap(reqs, grequests.Pool(2))  # 發送請求

    for r in response:
       soup = BeautifulSoup(r.content, "html.parser")  # 解析HTML原始碼

       products = soup.find_all("a", {"class": "ga"} )
       prices = soup.find_all("span", {"class": "rec-price-20"})

       for product, price in zip(products, prices):
             #print(product.getText(), price.getText())
             content.append([product.getText(), price.getText()])
    return content


def getPrice(itemName=''):
    print(11111)
    #item = PriceData(20, itemName)
    #items = item.work()
    #print(items, 11111)
    return '<h1>11111</h1>'
    #return render_template("price.html", itemList = items)

def test(itemName):
   items = getItemPrice(5, itemName)
   #print(items)
   return render_template("price.html", itemList = items)
