import requests
from lxml import etree
#获取原创首页视频
response = requests.get("http://www.lolshipin.com/lanmu/qingtong/list-2.html").content.decode('gbk')
# print(response)
#匹配视频url
urls = etree.HTML(response).xpath('/html//div[4]/div[1]/a/@href')
# print(url)
for url in urls:
    #请求视频url
    video_url = 'http://www.lolshipin.com' + url
    source = requests.get(video_url).content.decode('gbk')
    #/html/body/div[3]/div[1]/div[2]/h1
    title = etree.HTML(source).xpath('/html/body/div[3]/div[1]/div[2]/h1/text()')
    print(title)
    #http://42.81.115.51/om.tc.qq.com/AX5YaByPM0rjvK5xHAYI61i1WpAC8sJmQZD314llN-BA/uwMROfz2r57BIaQXGdGnC2deB3dUr_IkisDvBob9yrMGODlR/szg_24762272_50001_0c6991d1604a48dcadca351f5c2f799a.f622.mp4?sdtfrom=v1000&type=mp4&vkey=EB5A74F6516E474526D040579537277744E0ED5879D756AE628EA0A7C31DB5418A248B4FD0F64ED144C5680CA57ACE9CA514EBF1FA069954D24C4010960422F9BD205EC6303444A5E5FFC35A95C44F26E32B0ACDFCCEED9924047CF50492630C017E1E8FE18BBB1523BC30C887892E04DC9578C08C0DD99A261BDFF90069C73B525EA7A7B5A55190&level=0&platform=70202&br=105&fmt=hd&sp=0&guid=E8169787ECD1ED9E117DEB2A3C2602343EBC21D8