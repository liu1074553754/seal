# coding=gbk
'''
��ȡ���׽���ÿ����ѯ
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def wangyijiankang():
    response = requests.get('https://jiankang.163.com/').content.decode('gbk')
    #����xpath
    lists = etree.HTML(response).xpath('//*[@id="jiankangindex_wrap"]/div[6]/div[1]/div[1]/ul/li')
    print(len(lists))
    for li in lists:
        local_day = time.localtime(time.time()).tm_mday
        #��ȡ���±���
        title = li.xpath('h3/a/text()')[0].strip()
        # print(title)
        url = li.xpath('h3/a/@href')[0]
        source = requests.get(url).content.decode('gbk')
        # print(source)
        sult = etree.HTML(source).xpath('//*[@id="endText"]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\Ȥͷ����Ѷ\%s" % str(local_day)):
            os.mkdir(r"D:\Ȥͷ����Ѷ\%s" % str(local_day))

        title,text = Clear_code(div_str,title)
        with open(r"D:\Ȥͷ����Ѷ\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------���׽�����-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    wangyijiankang()