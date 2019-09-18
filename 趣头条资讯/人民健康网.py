# coding=gbk
'''
��ȡ���񽡿���ÿ����ѯ
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def renminjiankangwang():
    response = requests.get('http://health.people.com.cn/GB/408572/index.html').content.decode('gbk')
    #����xpath
    lists = etree.HTML(response).xpath('/html/body/div/div[4]/div/div/div[1]/div[2]/ul//div')
    print(len(lists))
    for li in lists:
        #��������
        try:
            ctime = li.xpath('div/text()')[0].split('��')[-1].split('��')[0]
        except:
            continue
        # print(ctime,type(ctime))
        #��ȡ��ǰ���ں�
        local_day = time.localtime(time.time()).tm_mday
        #�ж����������Ƿ���ڽ���
        # print(type(local_day))
        if int(ctime) != local_day:
            continue
        #��ȡ���±���
        title = li.xpath('a/text()')[0].strip()
        # print(title)
        url = 'http://health.people.com.cn' + li.xpath('a/@href')[0]
        source = requests.get(url).content.decode('gbk')
        # print(source)
        sult = etree.HTML(source).xpath('/html/body/div/div[4]/div/div/div[1]/div[2]/div[1]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\Ȥͷ����Ѷ\%s" % str(local_day)):
            os.mkdir(r"D:\Ȥͷ����Ѷ\%s" % str(local_day))

        title,text = Clear_code(div_str,title)
        with open(r"D:\Ȥͷ����Ѷ\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------���񽡿���-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    renminjiankangwang()