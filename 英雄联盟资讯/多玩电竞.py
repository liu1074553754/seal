# coding=gbk
'''
��ȡ����羺��վÿ����ѯ
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def duowandianjing():
    response = requests.get('http://news.duowan.com/').content.decode('utf-8')
    #����xpath
    lists = etree.HTML(response).xpath('/html/body/div[2]/div[1]/div[4]/div[1]/ul[1]/li')
    print(len(lists))
    for li in lists:
        #��������
        try:
            ctime = li.xpath('div/div/div[1]/span[3]/text()')[0].split('-')[-1]
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
        title = li.xpath('div/a/h4/text()')[0].strip()
        # print(title)
        url = li.xpath('div/a/@href')[0]
        source = requests.get(url).content.decode('utf-8')
        # print(source)
        sult = etree.HTML(source).xpath('/html/body/div[2]/div/div[3]/div[1]/div[2]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\Ӣ������ͼƬ\%s" % str(local_day)):
            os.mkdir(r"D:\Ӣ������ͼƬ\%s" % str(local_day))
        # with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'w',encoding='utf-8') as f:
        #     f.write(div_str)
        # # print(div_str.decode('utf-8'))

        title,text = Clear_code(div_str,title)
        with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------����羺-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    duowandianjing()