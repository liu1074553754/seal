# coding=gbk
'''
��ȡ����������վÿ����ѯ
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def demaxiya():
    response = requests.get('https://www.demaxiya.com/news/').content.decode('utf-8')
    lists = etree.HTML(response).xpath('/html/body/div[3]/div[2]/ul/li')
    for li in lists:
        #��������
        try:
            ctime = li.xpath('div/span/time/text()')[0].split('-')[-1]
        except:
            continue
        # print(ctime,type(ctime))
        #��ȡ��ǰ���ں�
        local_day = time.localtime(time.time()).tm_mday
        #�ж����������Ƿ���ڽ���
        # print(type(local_day))
        if int(ctime) != local_day:
            continue
        title = li.xpath('div/a/@title')
        # print(title)
        url = li.xpath('div/a/@href')[0]
        source = requests.get(url).content.decode('utf-8')
        # print(source)
        sult = etree.HTML(source).xpath('/html/body/div[3]/div[2]/div[2]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\Ӣ������ͼƬ\%s" % str(local_day)):
            os.mkdir(r"D:\Ӣ������ͼƬ\%s" % str(local_day))
        # with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'w',encoding='utf-8') as f:
        #     f.write(div_str)
        # # print(div_str.decode('utf-8'))
        title,text = Clear_code(div_str,title)
        with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------��������-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)

def demaxiya_index():
    response = requests.get('https://www.demaxiya.com/').content.decode('utf-8')
    lists = etree.HTML(response).xpath('/html/body/div[9]/div[2]/div[1]/dl')
    print(len(lists))
    for li in lists:
        #��������
        try:
            ctime = li.xpath('dd/p/text()')[0].split('-')[-1]
        except:
            continue
        # print(ctime,type(ctime))
        #��ȡ��ǰ���ں�
        local_day = time.localtime(time.time()).tm_mday
        #�ж����������Ƿ���ڽ���
        # print(type(local_day))
        if int(ctime) != local_day:
            continue
        title = li.xpath('dd/a/text()')[0]
        # print(title)
        url = li.xpath('dd/a/@href')[0]
        source = requests.get(url).content.decode('utf-8')
        # print(source)
        sult = etree.HTML(source).xpath('/html/body/div[3]/div[2]/div[2]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\Ӣ������ͼƬ\%s" % str(local_day)):
            os.mkdir(r"D:\Ӣ������ͼƬ\%s" % str(local_day))
        # with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'w',encoding='utf-8') as f:
        #     f.write(div_str)
        # # print(div_str.decode('utf-8'))
        title,text = Clear_code(div_str,title)
        with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------��������-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)

if __name__ == '__main__':
    demaxiya_index()