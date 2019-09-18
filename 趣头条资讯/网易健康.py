# coding=gbk
'''
获取网易健康每日咨询
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def wangyijiankang():
    response = requests.get('https://jiankang.163.com/').content.decode('gbk')
    #盒子xpath
    lists = etree.HTML(response).xpath('//*[@id="jiankangindex_wrap"]/div[6]/div[1]/div[1]/ul/li')
    print(len(lists))
    for li in lists:
        local_day = time.localtime(time.time()).tm_mday
        #获取文章标题
        title = li.xpath('h3/a/text()')[0].strip()
        # print(title)
        url = li.xpath('h3/a/@href')[0]
        source = requests.get(url).content.decode('gbk')
        # print(source)
        sult = etree.HTML(source).xpath('//*[@id="endText"]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\趣头条资讯\%s" % str(local_day)):
            os.mkdir(r"D:\趣头条资讯\%s" % str(local_day))

        title,text = Clear_code(div_str,title)
        with open(r"D:\趣头条资讯\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------网易健康网-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    wangyijiankang()