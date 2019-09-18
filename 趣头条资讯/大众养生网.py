# coding=gbk
'''
获取大众养生网每日咨询
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def dazhongyangsheng():
    headers = {

'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'Hm_lvt_d9c9cb2018bcee922c7c679094304232=1568776465; SERVERID=762bb535d9cfe50a47c6e015c6811a13|1568783108|1568776464; Hm_lpvt_d9c9cb2018bcee922c7c679094304232=1568783811',

'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    response = requests.get('https://www.cndzys.com/',headers=headers).content.decode('utf-8')
    #盒子xpath
    lists = etree.HTML(response).xpath('//*[@id="artlist_more"]/li')
    for li in lists:
        #文章日期//*[@id="artlist_more"]/li[1]
        try:
            ctime = int(li.xpath('div/span/time/text()')[0].split('-')[-1].split(' ')[0])
        except:
            continue
        # print(ctime,type(ctime))
        #获取当前日期号
        local_day = time.localtime(time.time()).tm_mday
        #判断文章日期是否等于今天
        # print(type(local_day))
        # if ctime != local_day:
        #     continue
        #获取文章标题
        title = li.xpath('div/h4/a/text()')[0].strip()
        # print(title)
        url = 'https://www.cndzys.com' + li.xpath('a/@href')[0]
        source = requests.get(url).content.decode('utf-8')
        # print(source)
        try:
            sult = etree.HTML(source).xpath('//div[@class="con_left"]')[0]
        except:
            continue
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\趣头条资讯\%s" % str(local_day)):
            os.mkdir(r"D:\趣头条资讯\%s" % str(local_day))

        title,text = Clear_code(div_str,title)
        with open(r"D:\趣头条资讯\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------大众养生网-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    dazhongyangsheng()