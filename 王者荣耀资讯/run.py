from 呀诺达电竞 import yanuoda
from zi52pk import zi52pk
from zi17173 import zi17173
from 牛游戏网 import niuyouxi
from threading import Thread
if __name__ == '__main__':
    '''
    德玛西亚视频可以获取，，，接口为szg_........开头
    叶子猪网站可以获取云顶之弈资讯：http://lol.yzz.cn/
    '''
    thread_01 = Thread(target=yanuoda)
    thread_02 = Thread(target=zi17173)
    thread_03 = Thread(target=zi52pk)
    thread_04 = Thread(target=niuyouxi)


    # demaxiya()
    # tewanwang()
    thread_01.start()
    thread_02.start()
    thread_03.start()
    thread_04.start()
