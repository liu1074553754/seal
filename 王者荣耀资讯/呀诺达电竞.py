# coding=gbk
'''
��ȡѽŵ����������ҫÿ����ѯ
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def yanuoda():
    response = requests.get('http://yonodo.com/').content.decode('utf-8')
    #����xpath/html/body/div[3]/div[2]/ul/li[1]
    lists = etree.HTML(response).xpath('/html/body/main/div/div/main/section/section/div[2]/div')
    for li in lists:
        #��������
        try:
            ctime = li.xpath('div[2]/p[2]/span/text()')[0].split('-')[-1]
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
        title = li.xpath('div[2]/h4/a/text()')[0].strip()
        print(title)
        url = 'http://yonodo.com' + li.xpath('div[2]/h4/a/@href')[0]
        source = requests.get(url).content.decode('utf-8')
        # print(source)
        try:
            sult = etree.HTML(source).xpath('/html/body/main/div[2]/div/main/section/section[2]')[0]
        except:
            continue
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\������ҫ��Ѷ\%s" % str(local_day)):
            os.mkdir(r"D:\������ҫ��Ѷ\%s" % str(local_day))
        # with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'w',encoding='utf-8') as f:
        #     f.write(div_str)
        # # print(div_str.decode('utf-8'))
        title,text = Clear_code(div_str,title)
        with open(r"D:\������ҫ��Ѷ\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------ѽŵ��-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    yanuoda()