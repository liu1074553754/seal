# coding=gbk
'''
获取人民健康网每日咨询
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def renminjiankangwang():
    response = requests.get('http://health.people.com.cn/GB/408572/index.html').content.decode('gbk')
    #盒子xpath
    lists = etree.HTML(response).xpath('/html/body/div/div[4]/div/div/div[1]/div[2]/ul//div')
    print(len(lists))
    for li in lists:
        #文章日期
        try:
            ctime = li.xpath('div/text()')[0].split('月')[-1].split('日')[0]
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
        url = 'http://health.people.com.cn' + li.xpath('a/@href')[0]
        source = requests.get(url).content.decode('gbk')
        # print(source)
        sult = etree.HTML(source).xpath('/html/body/div/div[4]/div/div/div[1]/div[2]/div[1]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\趣头条资讯\%s" % str(local_day)):
            os.mkdir(r"D:\趣头条资讯\%s" % str(local_day))

        title,text = Clear_code(div_str,title)
        with open(r"D:\趣头条资讯\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------人民健康网-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    renminjiankangwang()