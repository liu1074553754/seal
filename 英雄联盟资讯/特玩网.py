# coding=gbk
'''
��ȡ������վÿ����ѯ
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def tewanwang():
    response = requests.get('http://lol.te5.com/list/').content.decode('utf-8')
    #����xpath
    lists = etree.HTML(response).xpath('//*[@id="tagfc0be193fd7134d6e1cd67fc5241edad"]/a')
    for li in lists:
        #��������
        try:
            ctime = li.xpath('dl/dd/div[1]/span/text()')[0].split('-')[-1]
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
        title = li.xpath('dl/dd/div[1]/h2/text()')[0].strip()
        # print(title)
        url = li.xpath('@href')[0]
        source = requests.get(url).content.decode('utf-8')
        # print(source)
        sult = etree.HTML(source).xpath('//*[@id="text"]')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\Ӣ������ͼƬ\%s" % str(local_day)):
            os.mkdir(r"D:\Ӣ������ͼƬ\%s" % str(local_day))
        # with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'w',encoding='utf-8') as f:
        #     f.write(div_str)
        # # print(div_str.decode('utf-8'))
        title,text = Clear_code(div_str,title)
        with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------������-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    tewanwang()