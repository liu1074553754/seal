from 多玩电竞 import duowandianjing
from 德玛西亚 import demaxiya,demaxiya_index
from 特玩网 import tewanwang
from 多玩游戏网 import duowanyouxi
from 叶子猪 import yezizhu
from threading import Thread
if __name__ == '__main__':
    '''
    德玛西亚视频可以获取，，，接口为szg_........开头
    叶子猪网站可以获取云顶之弈资讯：http://lol.yzz.cn/
    '''
    thread_01 = Thread(target=duowanyouxi)
    thread_02 = Thread(target=duowandianjing)
    thread_03 = Thread(target=demaxiya)
    thread_04 = Thread(target=tewanwang)
    thread_05 = Thread(target=yezizhu)
    thread_06 = Thread(target=demaxiya_index)

    # demaxiya()
    # tewanwang()
    thread_01.start()
    thread_02.start()
    thread_03.start()
    thread_04.start()
    thread_05.start()
    thread_06.start()