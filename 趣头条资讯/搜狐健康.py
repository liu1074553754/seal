#coding=utf-8
import re

import requests
from lxml import etree
import time
import os
from clear_code import Clear_code

def souhujiankang():
    response = requests.get('https://health.sohu.com/?spm=smpc.ch24-smkx.top-subnav.1.1568778576614WkAuH1k').content.decode('utf-8')
    #盒子xpath
    lists = etree.HTML(response).xpath('//*[@id="main-container"]//a')
    print(len(lists))
    for li in lists:
        # 获取文章标题
        try:
            title = re.sub(r'[|?]','',li.xpath('text()')[0].strip())
        except:
            continue
        # print(title)
        url = 'http:' + li.xpath('@href')[0]
        try:
            source = requests.get(url).content.decode('utf-8')
        except:
            continue
        # print(source)

        #文章日期
        try:
            ctime = etree.HTML(source).xpath('//*[@id="news-time"]/text()')[0].split('-')[-1].split(' ')[0]

        except:
            continue
        # print(ctime,type(ctime))
        #获取当前日期号
        local_day = time.localtime(time.time()).tm_mday
        #判断文章日期是否等于今天
        # print(type(local_day))
        if int(ctime) != local_day:
            continue

        # print(source)
        sult = etree.HTML(source).xpath('//*[@id="mp-editor"]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\趣头条资讯\%s" % str(local_day)):
            os.mkdir(r"D:\趣头条资讯\%s" % str(local_day))

        title,text = Clear_code(div_str,title)
        with open(r"D:\趣头条资讯\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------搜狐健康---------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    souhujiankang()