# coding=gbk
'''
��ȡҶ������վÿ����ѯ
'''
import requests
from lxml import etree
import time
import os
from clear_code import Clear_code
def yezizhu():
    response = requests.get('http://lol.yzz.cn/ydzy/').content.decode('gbk')
    #����xpath
    lists = etree.HTML(response).xpath('/html/body/div[2]/div[8]/div/div/dl/dd')
    print(len(lists))
    # lists += etree.HTML(response).xpath('/html/body/div[2]/div[3]/div/div[1]/div[2]/div[5]/div[2]/ul[1]/li')
    for li in lists:
        #��������
        try:
            ctime = li.xpath('span/text()')[0].split('-')[-1]
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
        url = li.xpath('a/@href')[0]
        source = requests.get(url).content.decode('gbk')
        # print(source)  
        sult = etree.HTML(source).xpath('/html/body/div[2]/div[3]/div[1]/div/div[3]/table/tbody/tr[1]/td')[0]
        div_str = etree.tostring(sult,encoding='utf-8').decode('utf-8')
        if not os.path.exists(r"D:\Ӣ������ͼƬ\%s" % str(local_day)):
            os.mkdir(r"D:\Ӣ������ͼƬ\%s" % str(local_day))
        # with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'w',encoding='utf-8') as f:
        #     f.write(div_str)
        # # print(div_str.decode('utf-8'))

        title,text = Clear_code(div_str,title)
        with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(str(local_day),title),'a',encoding='utf-8') as f:
            f.write('\n')
            f.write('------------------Ҷ����-----------------------')
            f.write('\n')
            f.write(url)
            f.write(text)
if __name__ == '__main__':
    yezizhu()