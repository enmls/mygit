# _*_ encode:utf-8_*_
#2021/11/12
import os
from collections.abc import Iterable
import re
import requests
from lxml import etree
import itertools

class wMsj():
    def __init__(self):
        self.herders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
        self.url = "https://www.biquge7.com/book/764/"
        self.url2 = "https://www.biquge7.com"
    def urllist(self):
        url_list = []
        url_list2 = []
        html = requests.get(self.url,self.herders).text
        html1 = etree.HTML(html, etree.HTMLParser(encoding='utf8'))
        result = html1.xpath('/html/body/div[5]/dl/*/a/@href')
        result2 = html1.xpath('/html/body/div[5]/dl/span/dd[*]/a/@href')
        for i in result:
            if i=="javascript:dd_show()":
                for j in result2:
                    url_list2.append(self.url2 + j)
            url_list.append(self.url2+i)
        url_list.insert(10,url_list2)
        url_list.remove('https://www.biquge7.comjavascript:dd_show()')
        return url_list

    def flatten(self,input_list):
        '''嵌套列表平铺'''
        output_list = []
        while True:
            if input_list == []:
                break
            for index, i in enumerate(input_list):
                if type(i) == list:
                    input_list = i + input_list[index + 1:]
                    break
                else:
                    output_list.append(i)
                    input_list.pop(index)
                    break
        return output_list


def read(num):
    if num > 2021:
        print("没有这一章!!")
    elif num <= 2021:
        data1 = requests.get(data[num - 1], wm.herders).text

        data2 = etree.HTML(data1, etree.HTMLParser(encoding='utf8'))

        r = data2.xpath('//*[@id="chaptercontent"]/text()')

        for n in r:
            print(n)

wm = wMsj()
data = wm.flatten(wm.urllist())

if __name__ == '__main__':
    while True:
        a = int(input("请输入章数:"))
        if a<=2021:
            m = read(a)
            print(f"{m}\n当前完美世界第{a}章!\t输入8888退出!")
        elif a==8888:
            break


