# coding=gbk
import os
import re
import requests
import html
import random
#���˱���
def Clear_code(codes,title):
    sult =  re.sub(r'<.*?>','',codes)
    # try:
    #     title = re.findall('<h1 class="fwr f30 arctitle">(.*?)</h1>')[0]
    # except:
    #     title = '%s'%str(random.randint(0,100000))
    #��������������
    return title,html.unescape(sult)

def save_image(codes,title,con):
    sults = re.findall(r'data-url="(.*?)"',codes)
    if not os.path.exists(r"D:\Ӣ������ͼƬ\%s" % title):
        os.mkdir(r"D:\Ӣ������ͼƬ\%s" % title)
    with open(r"D:\Ӣ������ͼƬ\%s\%s.txt"%(title,title),'w') as f:
        f.write(con)
    for i,sult in enumerate(sults):
        response = requests.get(sult).content
        with open(r"D:\Ӣ������ͼƬ\%s\%s.jpg"%(title,i),'wb') as f:
            f.write(response)
if __name__ == '__main__':
    strs = '''<p>
	�ƶ�֮����Ϊ���������ŵ�һ��ģʽ����9.18�汾Ҳ�����˺ܴ�ĸĶ������������Ű汾�ĸ��º���ҵ���⣬�ƶ�֮�ĵ��淨Ҳ���ֶ����ԡ������ڽ�Ϊ��Ҵ����ƶ�֮�����ý������4������������̵㣬����������ʹ�ò��Ϸ֡�</p>
<h3 class="h_tit2 h_tit">
	Լ�¶���ʦ��</h3>
<br />
<center>
	<img alt="�Ĵ��������C�����Ƽ� �ɶ��������ͻ��" class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915141949-50.jpg@q_80" /></center>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135226.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">�����</span></strong></p>
<p>
	���(2)����ȫ������������ʹ�������߼����˺���</p>
<p>
	�Լ�¶���(3)������Լ�¶��˿���ʹ������ǵĹ���ż������&ldquo;δ����&rdquo;������Լ�¶������������ӣ�&ldquo;δ����&rdquo;�ļ���Ҳ��������</p>
<p>
	���ʦ(3)��ʦ�ӹ����л�õķ���ֵ��������ˮƽ����������ʦ����ʹ��Ķ����÷���ǿ�ȣ����ŷ�ʦ���������ӣ���õķ���ǿ��Ҳ��������</p>
<p>
	���ʿ(2)��������ʿ����ʹ���Ǹ񵲼������ܵĹ����˺���������ʿ���������ӣ��񵲵��˺�Ҳ���������˺����⣺15/30/55 =&gt; 15/35/65��</p>
<p>
	���ħ(2)40%�̶�����ȼ��20�㷨��ֵ�����ظ�15/30/45�㷨��ֵ��</p>
<p>
	�����ʦ(3)�����㹻��Ļ���ʦ����ʹ�����ڱ���ʱ�������ֵ��</p>
<p>
	<strong><span style="color:#ff0000;">ǰ���ڹ���</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135227.png@q_80" /></center>
<p>
	ǰ�������õ���������3�������Ƭ�ɸ���ܳ�ɫ��������������������ȶ���ɷ������ȡ����������õ�Լ�¶����ͷ�ʦ����ݳ��ܺ�����õ���֤�������õ���C֮һ���ɶ������ݿ�ʼ����������</p>
<p>
	<strong><span style="color:#ff0000;">����װ��</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135227-50.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135228.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135228-50.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135229.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135231.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">����װ�����������������֤����װ����ӵ�У�ȷ���������ݵĺ����֮һ��ħ�ĳ��͡�</span></strong>��������õ�����֮צ�Ϳ�ͽ���ױ�֤����ʦ�ɶ���̹�ȸ���ħ���������ָ�������õ���C֮һ��ѻ��Ī�����ص���跶Χ���������˺��͸���׸��豣����</p>
<p>
	<strong><span style="color:#ff0000;">����վλ</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135232.png@q_80" /></center>
<p>
	��������ѡ���׼��վλ��ǰ�Ų���̹�Ⱥͳ��ܣ����úͲ��ȸ���һ���Ŀ��ƶ���Ů���κ����̹�ȼ汸���м䲼�ö�ħ��һ��������ɶ��������ǰ�Ÿ�����ƶ���ѻ����ĳ����������̹�ȿɹۣ��������һ���������֤���ŵ��ո���Ų������λ���������跶Χ�������ո��¶¶�ɸ���һ���ı����Ϳ��Ʊ�֤���ݵ�ս����</p>
<p>
	<strong><span style="color:#ff0000;">���ݵ���</span></strong></p>
<p>
	<strong><span style="color:#ff0000;">����������9.18�汾��S������֮һ��������Ͻ���������˺ܶ�����̹�ȺͿ���һһ�߱���</span></strong>ǰ���ڹ�������ȶ������ڼ����õ��ؼ���C�������Ƭ�����ݷ���ʱ����硣���Һ���װ��ƫ���˰汾���������������Բ�������ȱ���������ݴ���ͺܶ�ĺ����������������ѻ�Ƕ�ħ�ͻ���ʦ����Ҫ�߷ѿ�Ƭ��������C֮һ�����Ժ������Ӫ��֤�õ���ѻ��ͬʱ�õ��ؼ�װ����ȷ�����ݿ��Գ��Ͳ�������</p>
<p>
	<strong><span style="color:#000000;">�ɶ��������Ƴ�ǿ��������</span></strong></p>
<p style="text-align: center;">
	<span class="lazy-gif"><img alt="�Ĵ��������C�����Ƽ� " class="imagetype-gif scrollLoading" data-gifsrc="https://img.te5.com/uploads/allimg/190915/120-1Z915135526.gif" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135526.gif.jpg@q_80" /></span></p>
<h3 class="h_tit2 h_tit">
	��Ӱ����������</h3>
<br />
<center>
	<img alt="�Ĵ��������C�����Ƽ� �ɶ��������ͻ��" class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915141949.jpg@q_80" /></center>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135233-50.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">�����</span></strong></p>
<p>
	�����(4)��������������ʹ������һ�����ʻ�ù����ٶȼ�����Ч���������������������ӣ��������Ҳ��������</p>
<p>
	�����(2)�����㹻��İ�Ӱ��λ������ս����ʼʱ����һ��������ˣ��������ʼ����ֵ��</p>
<p>
	�����(2)����ȫ��������������ʹ�������Լ���Χ���ڵ��Ѿ��ڿ�ʼ��սʱ��û��ס�</p>
<p>
	���ʿ(2)��������ʿ����ʹ���Ǹ񵲼������ܵĹ����˺���������ʿ���������ӣ��񵲵��˺�Ҳ���������˺����⣺15/30/55 =&gt; 15/35/65��</p>
<p>
	�����(2)����������Ӣ�ۿ���ʹ���ǻ��һ������ѣ��Ŀ���Ч�������ż���Ӣ�����������ӣ��������Ҳ��������</p>
<p>
	���ħ(2)40%�̶�����ȼ��20�㷨��ֵ�����ظ�15/30/45�㷨��ֵ��</p>
<p>
	<strong><span style="color:#ff0000;">ǰ���ڹ���</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135234.png@q_80" /></center>
<p>
	ǰ����������ѡ������������������������̹�ȴ���3�Ź��忨Ƭǰ�ڵĹ��ȱ��ֿɹۡ����������õ������������Ȼ����СЧ������ǻ�����ϣ�����̹�Ⱥ�����汸���ݿ�ʼ����������</p>
<p>
	<strong><span style="color:#ff0000;">����װ��</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135234-50.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135235.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135236.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135236-50.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135237.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135237-50.png@q_80" /></center>
<p>
	������������ѡ�񺮱��ĺ���װ������װ���򵶸������ǵ��ӵĹ��ټӳ��������ǵ�������ྲ���չ�����ط���Ĭ��쫷�����������װ֮һ����������AOE����������������ѡ���ᱣ֤���ݶ�ħ�ĳ��ͣ�Ī�����ص���輼�ܵ�����Ч��������׸��������������ṩ������</p>
<p>
	<strong><span style="color:#ff0000;">����վλ</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135238.png@q_80" /></center>
<p>
	��������ͬ��ѡ���׼��վλ��ǰ�Ų�����Ů�����ñ�֤���ܵ�ͬʱ����һ���Ŀ��ƣ��м䲼�����λ��������ǧ��������������ɭ�ķ�Χ����������죬ֵ��һ���м䲼��ǧ��ɱ�֤ǧ�������󻯱�������ɭ������Ů��֤���ݳ��ܡ�����ͬ���������λ���������ݵ���C֮һ��ά³˹����һ����Poke���������������һ�����и���һ���ı����ͳ��ܡ�</p>
<p>
	<strong><span style="color:#ff0000;">���ݵ���</span></strong></p>
<p>
	<strong><span style="color:#ff0000;">�����������°汾ͬ��S�����ݣ��������ƴ������°汾���������������������㱣֤���ݺ��ڱ��֡�</span></strong>ͬ����Ȼ���ݴ����˶����ǽ���������ñ�֤�������Ͳ���̫�ܾ��ޡ�������������װ�����溮�������ô����װ�����ǰ汾������װ�������Ժ���ĺϳɲ�����װ���ǹؼ�֮һ����ξ������ݺ��ڵĸ߷���ѻ�ܹؼ�����������õ���ѻ��ô�������Ȼʧɫ�������ڹ���������ѡ����ѻ��֤���ݳ��͡�</p>
<p>
	<strong><span style="color:#000000;">���õĳ�ǿ���ƺ��������</span></strong></p>
<p style="text-align: center;">
	<span class="lazy-gif"><img alt="�Ĵ��������C�����Ƽ� " class="imagetype-gif scrollLoading" data-gifsrc="https://img.te5.com/uploads/allimg/190915/120-1Z915135529.gif" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135529.gif.jpg@q_80" /></span></p>
<h3 class="h_tit2 h_tit">
	ǹ��������</h3>
<br />
<center>
	<img alt="�Ĵ��������C�����Ƽ� �ɶ��������ͻ��" class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915141948.jpg@q_80" /></center>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135239-50.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">�����</span></strong></p>
<p>
	�����(1)��ս��ʼʱ��������˵���Χû������Ӣ�ۣ�������Ż��ܿ�ʼ��ս��</p>
<p>
	���ʿ(6)��������ʿӢ�ۿ���ʹ���ǵĹ�����һ�����ʽ��ж�ζ��⹥�������Ž�ʿӢ�����������ӣ��������Ҳ��������</p>
<p>
	�ǹ��(4)������ǹ�ֿ���ʹ���ǵĹ�����һ���������ж����Ŀ�꣬����ǹ�����������ӣ��������Ҳ��������</p>
<p>
	�����˹�Ƽ�(2)�ڱ���ս�������ʹ�з���2/ 4 ��װ��ʧЧ��</p>
<p>
	�����(1)�����ҽ�����һ������Ӣ�ۿ���ʹ���ù��������������в�ͬ����Ӣ�ۿ���ʹ��Щ����Ӣ�ۻ�ø���Ĺ�������</p>
<p>
	<strong><span style="color:#ff0000;">ǰ���ڹ���</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135240.png@q_80" /></center>
<p>
	ǰ������ѡ��ǹ���������ȣ�ǹ������źܳ�ɫ������ӳɴ���3�������Ƭ��֤�ȶ����������������õ������͹ؼ������֮һ���������ݿ�ʼ��������Ȼ�����ļӳ�Ч������ǿ�����Ǹ���Ľ�Ҽӳɱ�֤���ݺ����ȶ����͡�</p>
<p>
	<strong><span style="color:#ff0000;">����װ��</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135240-50.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135241.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135241-50.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135242.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135242-50.png@q_80" /></center>
<p>
	������������ѡ��������֮һʥǹ��װ�����ưܱ�֤������ɴ��6��ʿ����ѡ���򵶸��蹥�ٺ͵��ӹ��ٵ�Ч�����ྲ�ṩ�չ���Ĭ��Ч������һ���������������������ѡ�񴬳�װ����BUFF��֤�չ��߱�����Ч���������Ϊ��������ṩһ���ı�����֤���������</p>
<p>
	<strong><span style="color:#ff0000;">����վλ</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135243.png@q_80" /></center>
<p>
	��������ѡ���׼��վλ���ã�ǰ�Ų����� ���Ӱ ������3�ſ�Ƭ�ĳ����������ܿɹ����������ļ��ܸ񵲺���������Ļ��ܡ��м䲼�����λ���������ݵĹؼ������Ƭ�����AOE�������ǿ�����Ų����ո�ͷ�Χ�����Ƭ��Ůǹ����ܳ�ɫ�ķ�Χ���������˹���ո���ɶ�ƴ��</p>
<p>
	<strong><span style="color:#ff0000;">���ݵ���</span></strong></p>
<p>
	�������ݳ��ͺ���޽���Ȼ��A�����ݣ����ǳ��ͺ��ǿ�Ⱥͱ��ֲ���S�����ݡ�<strong><span style="color:#ff0000;">�������Ƴ��ͺ���ֺ��޽⣬��Ȼ��6��ʿ�Ĵ��������ưܺܺõĵ�������㣬���ݵĺ���װ����������Բ��󣬹���װѡ����ٱܿ��˰汾��������</span></strong>����ȱ����Ȼ�ưܺܺõĵ�������ϵ�ȱ�ݣ����ǳ��͵����ݺ�����Ҫ���Ÿ߷ѿ�Ƭ��Ůǹ�������������ݹؼ��ز����ٵĿ�Ƭ����ξ�����������δ���ι��ȽϷ��������Ժ���Ĵ��俨Ƭ��֤���Ȳ���̫��Ѫ���ǹؼ���</p>
<p>
	<strong><span style="color:#000000;">ǹ�ֽ�ʿ���䴬�����׵ķ�Χ���</span></strong></p>
<p style="text-align: center;">
	<span class="lazy-gif"><img alt="�Ĵ��������C�����Ƽ� " class="imagetype-gif scrollLoading" data-gifsrc="https://img.te5.com/uploads/allimg/190915/120-1Z915135531.gif" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135531.gif.jpg@q_80" /></span></p>
<h3 class="h_tit2 h_tit">
	Ԫ��Լ�¶���ʦ��</h3>
<br />
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135244.png@q_80" /></center>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135245.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">�����</span></strong></p>
<p>
	�Ԫ��ʹ(3)Ԫ��ʹ�ӹ����л�õķ���ֵ��������ˮƽ�������㹻���Ԫ��ʹ������ս��ʼʱ�ٻ���һ��Ԫ��Ϊ����ս��ħ�񻤼ף�20 =&gt; 40��</p>
<p>
	�Լ�¶���(3)������Լ�¶��˿���ʹ������ǵĹ���ż������&ldquo;δ����&rdquo;������Լ�¶������������ӣ�&ldquo;δ����&rdquo;�ļ���Ҳ��������</p>
<p>
	���ʦ(3)��ʦ�ӹ����л�õķ���ֵ��������ˮƽ����������ʦ����ʹ��Ķ����÷���ǿ�ȣ����ŷ�ʦ���������ӣ���õķ���ǿ��Ҳ��������</p>
<p>
	���ħ(2)40%�̶�����ȼ��20�㷨��ֵ�����ظ�15/30/45�㷨��ֵ��</p>
<p>
	���ʿ(2)��������ʿ����ʹ���Ǹ񵲼������ܵĹ����˺���������ʿ���������ӣ��񵲵��˺�Ҳ���������˺����⣺15/30/55 =&gt; 15/35/65��</p>
<p>
	�����(1)�����ҽ�����һ������Ӣ�ۿ���ʹ���ù��������������в�ͬ����Ӣ�ۿ���ʹ��Щ����Ӣ�ۻ�ø���Ĺ�������</p>
<p>
	<strong><span style="color:#ff0000;">ǰ���ڹ���</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135246.png@q_80" /></center>
<p>
	ǰ����������ѡ����������������ȣ���������°汾������һ���ܳ�ɫ�Ĺ�������źܳ�ɫ��̹�ȼӳɰ��������ȶ����ȡ����������õ����ݹؼ���Լ�¶����ͷ�ʦ����ݿ�ʼ����������ͳ��ܼ汸��</p>
<p>
	<strong><span style="color:#ff0000;">����װ��</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135246-50.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135247.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135247-50.png@q_80" /><img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135248.png@q_80" /></center>
<p>
	���ݵĹؼ����װ��ѡ��Ī�����ص���輼������Ч�����临��ױ�֤����������������<strong><span style="color:#ff0000;">��ѡ������������װ����������׶������ݹؼ��ıر�װ��</span></strong>��ͬ����������ѡ��</p>
<p>
	<strong><span style="color:#ff0000;">����վλ</span></strong></p>
<center>
	<img alt="�Ĵ��������C�����Ƽ� " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135248-50.png@q_80" /></center>
<p>
	��������ѡ���м䲼��վλ��ǰ�ŷ��ó��ܿ��Ƶ����úͲ��ȣ����俭�ϵķ�Χ��������˺����ˡ��м䲼�ÿ��ƴ�ʦ�����Ƽ���ѡ�ƿɸ�����ƻ��߻�����֤���ݵ���������Ų������λ�Ϳ���λ���ɶ���Ϊ����ʦ���οɸ�����Ʒ��ú��ű�֤��ȫ��ͬʱ��֤������������ζ�Ϊ���λ�����ո�ͷ�ΧAOE�˺���</p>
<p>
	<strong><span style="color:#ff0000;">���ݵ���</span></strong></p>
<p>
	<strong><span style="color:#ff0000;">�����������°汾������ý������ߴ����һ�����ݣ��������ݴ��������������������װ������Ҳʹ���������ݸ����˺ܶ��ӳ֣���֤���ݺ��ڵı��֡�</span></strong>��ζ������㱣֤װ��ѡ�񲻶࣬���ǽ������һ���ؼ�����ξ����������ݵĿɱ��Ժܴ�����ò����ؼ�װ���ɼ�ʱ�ĸ������ݵ���������ȱ����ǿ�Ұ�ĸĶ�ʹ��Լ�¶���������ڱ��������½�����ξ��Ƿ����Ϊ�߷ѿ�ƬͬʱҲ��Ԫ��ʹ�Ĺؼ���Ƭ�ر������Ժ������Ӫ�����İѿ�ÿ��ʱ�ڵĿ�Ƭ��װ���ǹؼ���</p>
<p>
	<strong><span style="color:#000000;">Ԫ��Լ�¶���ʦ���Ķ����C����ǿ��Χ�������</span></strong></p>
<p style="text-align: center;">
	<span class="lazy-gif"><img alt="�Ĵ��������C�����Ƽ� " class="imagetype-gif scrollLoading" data-gifsrc="https://img.te5.com/uploads/allimg/190915/120-1Z915135534.gif" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135534.gif.jpg@q_80" /></span></p>
<p>
	<span style="color:#0000ff;">�ܽ�</span></p>
<p>
	���ھ���Ϊ����Ƽ���4�����ý�����ķ�������C���ݣ����Կ����°汾���ڽ�����������𽥶����������𽥳�Ϊ��������ҿ��Զ����ϰ������Щ���ݵ�Ҫ�㣬����С���һ����λ������ߵ�С�����۽硣</p>

'''
    title = '�Ĵ��������C�����Ƽ� �ɶ��������ͻ��'
    title,con = Clear_code(strs,title)
    print(title,con)
    save_image(strs,title,con)