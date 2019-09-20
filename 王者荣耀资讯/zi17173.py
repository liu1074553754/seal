# coding=gbk
'''
获取17173游戏每日咨询
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def zi17173():
    response = requests.get('https://www.17173.com/').content.decode('utf-8')
    #盒子xpath//*[@id="forsetLink50"]/ul/li[1]@id="forsetLink40"
    # //*[@id="forsetLink53"]/div[2]/ul/li[9]//*[@id="global"]/ul/li[9]
    lists = etree.HTML(response).xpath('//*[contains(@id,forsetLink)]//li')
    print(len(lists))
    for li in lists:
        #文章日期
        try:
            ctime = li.xpath('div/span/text()')[0].split('[')[-1].split(']')[0]
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
        title = li.xpath('div/a/text()')[0].strip()
        # print(title)
        url = li.xpath('div/a/@href')[0]
        source = requests.get(url).content.decode('utf-8')
        # print(source)
        try:
            sult = etree.HTML(source).xpath('//*[@id="mod_article"]')[0]
        except:
            continue
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\王者荣耀资讯\%s" % str(local_day)):
            os.mkdir(r"D:\王者荣耀资讯\%s" % str(local_day))
        # with open(r"D:\英雄联盟图片\%s\%s.txt"%(str(local_day),title),'w',encoding='utf-8') as f:
        #     f.write(div_str)
        # # print(div_str.decode('utf-8'))
        title,text = Clear_code(div_str,title)
        try:
            with open(r"D:\王者荣耀资讯\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
                f.write('\n')
                f.write('------------------17173-----------------------')
                f.write('\n')
                f.write(url)
                f.write(text)
        except:
            continue
if __name__ == '__main__':
    zi17173()