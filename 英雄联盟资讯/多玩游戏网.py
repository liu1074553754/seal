# coding=gbk
'''
获取多玩游戏网站每日咨询
'''
import re

import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def duowanyouxi():
    response = requests.get('http://lol.duowan.com/').content.decode('utf-8')
    #盒子xpath
    lists = etree.HTML(response).xpath('//*[@id="ZQ"]/div[3]/div[11]/div[2]/div/div[2]/div/ul/li')
    lists += etree.HTML(response).xpath('//*[@id="weekly3"]/div[2]/div/ul/li')
    for li in lists:
        #文章日期
        try:
            ctime = li.xpath('span/text()')[0].split('-')[-1]
        except:
            continue
        # print(ctime,type(ctime))
        #获取当前日期号
        local_day = time.localtime(time.time()).tm_mday
        #判断文章日期是否等于今天
        # print(type(local_day))
        if int(ctime) != local_day:
            continue
        #获取文章标题
        title = li.xpath('a/text()')[0].strip()
        # print(title)
        #如果url保存，则多玩电竞py会抓取
        url = li.xpath('a/@href')[0]
        url = 'http://lol.duowan.com' + url
        try:
            source = requests.get(url).content.decode('utf-8')
        except :
            continue
        # print(source)
        sult = etree.HTML(source).xpath('//*[@id="text"]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\英雄联盟图片\%s" % str(local_day)):
            os.mkdir(r"D:\英雄联盟图片\%s" % str(local_day))
        # with open(r"D:\英雄联盟图片\%s\%s.txt"%(str(local_day),title),'w',encoding='utf-8') as f:
        #     f.write(div_str)
        # # print(div_str.decode('utf-8'))

        title,text = Clear_code(div_str,title)
        with open(r"D:\英雄联盟图片\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------多玩游戏-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    duowanyouxi()