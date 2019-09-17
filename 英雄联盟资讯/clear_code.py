# coding=gbk
import os
import re
import requests
import html
import random
#过滤编码
def Clear_code(codes,title):
    sult =  re.sub(r'<.*?>','',codes)
    # try:
    #     title = re.findall('<h1 class="fwr f30 arctitle">(.*?)</h1>')[0]
    # except:
    #     title = '%s'%str(random.randint(0,100000))
    #返回文章与内容
    return title,html.unescape(sult)

def save_image(codes,title,con):
    sults = re.findall(r'data-url="(.*?)"',codes)
    if not os.path.exists(r"D:\英雄联盟图片\%s" % title):
        os.mkdir(r"D:\英雄联盟图片\%s" % title)
    with open(r"D:\英雄联盟图片\%s\%s.txt"%(title,title),'w') as f:
        f.write(con)
    for i,sult in enumerate(sults):
        response = requests.get(sult).content
        with open(r"D:\英雄联盟图片\%s\%s.jpg"%(title,i),'wb') as f:
            f.write(response)
if __name__ == '__main__':
    strs = '''<p>
	云顶之弈作为联盟最热门的一个模式，在9.18版本也给予了很大的改动及调整，随着版本的更新和玩家的理解，云顶之弈的玩法也出现多样性。而本期将为大家带来云顶之弈妙用金铲铲的4大非主流阵容盘点，帮助大家灵活使用并上分。</p>
<h3 class="h_tit2 h_tit">
	约德尔法师龙</h3>
<br />
<center>
	<img alt="四大非主流主C阵容推荐 纳尔猪妹异军突起" class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915141949-50.jpg@q_80" /></center>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135226.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">核心羁绊</span></strong></p>
<p>
	羁绊：龙(2)部署全部两条龙可以使他们免疫技能伤害。</p>
<p>
	羁绊：约德尔人(3)部署多个约德尔人可以使针对他们的攻击偶尔出现&ldquo;未命中&rdquo;，随着约德尔人数量的增加，&ldquo;未命中&rdquo;的几率也会提升。</p>
<p>
	羁绊：法师(3)法师从攻击中获得的法力值高于正常水平。部署多个法师可以使你的队伍获得法术强度，随着法师数量的增加，获得的法术强度也会提升。</p>
<p>
	羁绊：骑士(2)部署多个骑士可以使他们格挡即将遭受的攻击伤害，随着骑士数量的增加，格挡的伤害也会提升。伤害减免：15/30/55 =&gt; 15/35/65。</p>
<p>
	羁绊：恶魔(2)40%固定几率燃烧20点法力值，并回复15/30/45点法力值。</p>
<p>
	羁绊：换形师(3)部署足够多的换形师可以使他们在变形时获得生命值。</p>
<p>
	<strong><span style="color:#ff0000;">前中期过度</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135227.png@q_80" /></center>
<p>
	前期我们拿到抢手羁绊配合3张输出卡片可给予很出色的输出能力，帮助我们稳定完成发育过度。中期我们拿到约德尔人羁绊和法师羁绊阵容承受和输出得到保证，并且拿到主C之一的纳尔，阵容开始初步发力。</p>
<p>
	<strong><span style="color:#ff0000;">核心装备</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135227-50.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135228.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135228-50.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135229.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135231.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">核心装备优先抢到金铲铲保证暗裔装备的拥有，确保我们阵容的核心羁绊之一恶魔羁绊的成型。</span></strong>其次我们拿到巨龙之爪和狂徒铠甲保证换形师纳尔的坦度给予魔抗和生命恢复。最后拿到主C之一乌鸦的莫雷洛秘典给予范围技能灼烧伤害和复活甲给予保护。</p>
<p>
	<strong><span style="color:#ff0000;">阵容站位</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135232.png@q_80" /></center>
<p>
	这里我们选择标准的站位，前排布置坦度和承受，猪妹和波比给予一定的控制而龙女换形后输出坦度兼备。中间布置恶魔和一个输出，纳尔可以配合前排给予控制而乌鸦给予的持续输出并且坦度可观，狐狸给予一定的输出保证后排的收割。后排布置输出位，龙王给予范围输出完成收割，而露露可给予一定的保护和控制保证阵容的战力。</p>
<p>
	<strong><span style="color:#ff0000;">阵容点评</span></strong></p>
<p>
	<strong><span style="color:#ff0000;">这套阵容是9.18版本的S级阵容之一，整体配合金铲铲成型了很多羁绊，输出坦度和控制一一具备。</span></strong>前中期过度相对稳定，中期即可拿到关键主C和输出卡片，阵容发力时间较早。并且核心装备偏离了版本的主流，想多局限性不大。阵容缺点则是阵容搭配和很多的核心输出，尤其是乌鸦是恶魔羁绊和换形师羁绊的主要高费卡片，还是主C之一。所以合理的运营保证拿到乌鸦的同时拿到关键装备，确保阵容可以成型并发力。</p>
<p>
	<strong><span style="color:#000000;">纳尔如来神掌超强控制能力</span></strong></p>
<p style="text-align: center;">
	<span class="lazy-gif"><img alt="四大非主流主C阵容推荐 " class="imagetype-gif scrollLoading" data-gifsrc="https://img.te5.com/uploads/allimg/190915/120-1Z915135526.gif" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135526.gif.jpg@q_80" /></span></p>
<h3 class="h_tit2 h_tit">
	暗影护卫游侠流</h3>
<br />
<center>
	<img alt="四大非主流主C阵容推荐 纳尔猪妹异军突起" class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915141949.jpg@q_80" /></center>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135233-50.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">核心羁绊</span></strong></p>
<p>
	羁绊：游侠(4)部署多个游侠可以使他们有一定几率获得攻击速度激增的效果，随着游侠数量的增加，这个几率也会提升。</p>
<p>
	羁绊：暗裔(2)部署足够多的暗影单位可以在战斗开始时诅咒一个随机敌人，降低其初始生命值。</p>
<p>
	羁绊：护卫(2)部署全部两个护卫可以使其自身以及周围相邻的友军在开始作战时获得护甲。</p>
<p>
	羁绊：骑士(2)部署多个骑士可以使他们格挡即将遭受的攻击伤害，随着骑士数量的增加，格挡的伤害也会提升。伤害减免：15/30/55 =&gt; 15/35/65。</p>
<p>
	羁绊：极地(2)部署多个极地英雄可以使他们获得一定几率眩晕目标的效果，随着极地英雄数量的增加，这个几率也会提升。</p>
<p>
	羁绊：恶魔(2)40%固定几率燃烧20点法力值，并回复15/30/45点法力值。</p>
<p>
	<strong><span style="color:#ff0000;">前中期过度</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135234.png@q_80" /></center>
<p>
	前期我们优先选择贵族羁绊帮助发育，贵族羁绊给予的坦度搭配3张贵族卡片前期的过度表现可观。中期我们拿到多种阵容羁绊，虽然都是小效果的羁绊但是互相配合，控制坦度和输出兼备阵容开始初步发力。</p>
<p>
	<strong><span style="color:#ff0000;">核心装备</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135234-50.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135235.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135236.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135236-50.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135237.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135237-50.png@q_80" /></center>
<p>
	这里我们优先选择寒冰的核心装备攻速装，羊刀给予我们叠加的攻速加成提升我们的输出，肃静可普攻给予地方沉默，飓风金铲铲的特殊装之一，给予我们AOE输出能力。随后我们选择暗裔保证阵容恶魔羁绊的成型，莫雷洛秘典给予技能的灼烧效果，复活甲给予二次输出能力提供保护。</p>
<p>
	<strong><span style="color:#ff0000;">阵容站位</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135238.png@q_80" /></center>
<p>
	这里我们同样选择标准的站位，前排布置日女和猪妹保证承受的同时给予一定的控制，中间布置输出位，寒冰和千珏给予输出搭配潘森的范围输出表现优异，值得一提中间布置千珏可保证千珏大招最大化保护，潘森搭配日女保证阵容承受。后排同样布置输出位，寒冰阵容的主C之一，维鲁斯给予一定的Poke输出能力，最后搭配一个铁男给予一定的保护和承受。</p>
<p>
	<strong><span style="color:#ff0000;">阵容点评</span></strong></p>
<p>
	<strong><span style="color:#ff0000;">这套阵容在新版本同属S级阵容，阵容优势搭配了新版本热门输出羁绊游侠，多个输出点保证阵容后期表现。</span></strong>同样虽然阵容搭配了多个羁绊但是金铲铲的妙用保证阵容羁绊成型不会太受局限。阵容劣势则是装备方面寒冰和猪妹搭配的装备都是版本的主流装备，所以合理的合成并运用装备是关键之一，其次就是阵容后期的高费乌鸦很关键，如果不能拿到乌鸦那么暗裔就黯然失色，所以在共享尽量优先选择乌鸦保证阵容成型。</p>
<p>
	<strong><span style="color:#000000;">猪妹的超强控制和输出能力</span></strong></p>
<p style="text-align: center;">
	<span class="lazy-gif"><img alt="四大非主流主C阵容推荐 " class="imagetype-gif scrollLoading" data-gifsrc="https://img.te5.com/uploads/allimg/190915/120-1Z915135529.gif" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135529.gif.jpg@q_80" /></span></p>
<h3 class="h_tit2 h_tit">
	枪剑浪人流</h3>
<br />
<center>
	<img alt="四大非主流主C阵容推荐 纳尔猪妹异军突起" class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915141948.jpg@q_80" /></center>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135239-50.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">核心羁绊</span></strong></p>
<p>
	羁绊：浪人(1)作战开始时，如果浪人的周围没有其他英雄，他会带着护盾开始作战。</p>
<p>
	羁绊：剑士(6)部署多个剑士英雄可以使他们的攻击有一定几率进行多次额外攻击，随着剑士英雄数量的增加，这个几率也会提升。</p>
<p>
	羁绊：枪手(4)部署多个枪手可以使他们的攻击有一定几率命中额外的目标，随着枪手数量的增加，这个几率也会提升。</p>
<p>
	羁绊：海克斯科技(2)在本次战斗中随机使敌方的2/ 4 件装备失效。</p>
<p>
	羁绊：忍者(1)部署且仅部署一个忍者英雄可以使其获得攻击力。部署所有不同忍者英雄可以使这些忍者英雄获得更多的攻击力。</p>
<p>
	<strong><span style="color:#ff0000;">前中期过度</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135240.png@q_80" /></center>
<p>
	前期我们选择枪手羁绊帮助过度，枪手羁绊有着很出色的输出加成搭配3张输出卡片保证稳定发育。中期我们拿到海盗羁绊和关键的输出之一船长，阵容开始发力。虽然海盗羁绊的加成效果并不强劲但是给予的金币加成保证阵容后期稳定成型。</p>
<p>
	<strong><span style="color:#ff0000;">核心装备</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135240-50.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135241.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135241-50.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135242.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135242-50.png@q_80" /></center>
<p>
	这里我们优先选择核心输出之一圣枪的装备，破败保证我们完成大羁绊6剑士羁绊，其次选择羊刀给予攻速和叠加攻速的效果，肃静提供普攻沉默的效果给予一定的限制能力。随后我们选择船长装备红BUFF保证普攻具备灼烧效果，复活甲为我们输出提供一定的保护保证持续输出。</p>
<p>
	<strong><span style="color:#ff0000;">阵容站位</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135243.png@q_80" /></center>
<p>
	阵容依旧选择标准的站位布置，前排布置慎 青钢影 亚索，3张卡片的承受能力都很可观尤其是慎的技能格挡和亚索给予的护盾。中间布置输出位，都是阵容的关键输出卡片单体和AOE输出都很强，后排布置收割和范围输出卡片，女枪给予很出色的范围输出搭配金克斯的收割完成对拼。</p>
<p>
	<strong><span style="color:#ff0000;">阵容点评</span></strong></p>
<p>
	这套阵容成型后很无解虽然是A级阵容，但是成型后的强度和表现不输S级阵容。<strong><span style="color:#ff0000;">阵容优势成型后表现很无解，虽然有6剑士的大羁绊但是配合破败很好的抵消了这点，阵容的核心装备方面局限性不大，攻速装选择较少避开了版本的主流。</span></strong>阵容缺点虽然破败很好的抵消了羁绊上的缺陷，但是成型的阵容后期需要两张高费卡片，女枪和亚索都是阵容关键羁绊必不可少的卡片，其次就是阵容中期未成形过度较乏力，所以合理的搭配卡片保证过度不掉太多血量是关键。</p>
<p>
	<strong><span style="color:#000000;">枪手剑士搭配船长不俗的范围输出</span></strong></p>
<p style="text-align: center;">
	<span class="lazy-gif"><img alt="四大非主流主C阵容推荐 " class="imagetype-gif scrollLoading" data-gifsrc="https://img.te5.com/uploads/allimg/190915/120-1Z915135531.gif" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135531.gif.jpg@q_80" /></span></p>
<h3 class="h_tit2 h_tit">
	元素约德尔法师流</h3>
<br />
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135244.png@q_80" /></center>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135245.png@q_80" /></center>
<p>
	<strong><span style="color:#ff0000;">核心羁绊</span></strong></p>
<p>
	羁绊：元素使(3)元素使从攻击中获得的法力值高于正常水平。部署足够多的元素使会在作战开始时召唤出一个元素为你作战。魔像护甲：20 =&gt; 40。</p>
<p>
	羁绊：约德尔人(3)部署多个约德尔人可以使针对他们的攻击偶尔出现&ldquo;未命中&rdquo;，随着约德尔人数量的增加，&ldquo;未命中&rdquo;的几率也会提升。</p>
<p>
	羁绊：法师(3)法师从攻击中获得的法力值高于正常水平。部署多个法师可以使你的队伍获得法术强度，随着法师数量的增加，获得的法术强度也会提升。</p>
<p>
	羁绊：恶魔(2)40%固定几率燃烧20点法力值，并回复15/30/45点法力值。</p>
<p>
	羁绊：骑士(2)部署多个骑士可以使他们格挡即将遭受的攻击伤害，随着骑士数量的增加，格挡的伤害也会提升。伤害减免：15/30/55 =&gt; 15/35/65。</p>
<p>
	羁绊：忍者(1)部署且仅部署一个忍者英雄可以使其获得攻击力。部署所有不同忍者英雄可以使这些忍者英雄获得更多的攻击力。</p>
<p>
	<strong><span style="color:#ff0000;">前中期过度</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135246.png@q_80" /></center>
<p>
	前期我们优先选择贵族羁绊帮助发育过度，贵族羁绊在新版本依旧是一个很出色的过度羁绊，有着很出色的坦度加成帮助我们稳定过度。中期我们拿到阵容关键的约德尔人羁绊和法师羁绊阵容开始发力，输出和承受兼备。</p>
<p>
	<strong><span style="color:#ff0000;">核心装备</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135246-50.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135247.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135247-50.png@q_80" /><img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135248.png@q_80" /></center>
<p>
	阵容的关键输出装备选择莫雷洛秘典给予技能灼烧效果搭配复活甲保证持续输出能力，随后<strong><span style="color:#ff0000;">可选择金铲铲的特殊装备暗裔和悠米都是阵容关键羁绊的必备装备</span></strong>，同样可以优先选择。</p>
<p>
	<strong><span style="color:#ff0000;">阵容站位</span></strong></p>
<center>
	<img alt="四大非主流主C阵容推荐 " class="scrollLoading" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135248-50.png@q_80" /></center>
<p>
	这里我们选择中间布置站位，前排放置承受控制的猪妹和波比，搭配凯南的范围输出优先伤害敌人。中间布置卡牌大师，卡牌技能选牌可给予控制或者回蓝保证阵容的输出。后排布置输出位和控制位，纳尔作为换形师换形可给予控制放置后排保证安全的同时保证进场，最后依次都为输出位给予收割和范围AOE伤害。</p>
<p>
	<strong><span style="color:#ff0000;">阵容点评</span></strong></p>
<p>
	<strong><span style="color:#ff0000;">这套阵容是新版本灵活运用金铲铲最具代表的一个阵容，成型阵容搭配了两个金铲铲的特殊装备，这也使得这套阵容附带了很多羁绊加持，保证阵容后期的表现。</span></strong>其次多个输出点保证装备选择不多，但是金铲铲是一个关键。其次就是这套阵容的可变性很大，如果拿不到关键装备可及时的更换阵容的走向。阵容缺点就是狂野羁绊的改动使得约德尔人羁绊在中期表现有所下降，其次就是凤凰作为高费卡片同时也是元素使羁绊的关键卡片必备，所以合理的运营并灵活的把控每个时期的卡片和装备是关键。</p>
<p>
	<strong><span style="color:#000000;">元素约德尔法师流的多点主C及超强范围输出能力</span></strong></p>
<p style="text-align: center;">
	<span class="lazy-gif"><img alt="四大非主流主C阵容推荐 " class="imagetype-gif scrollLoading" data-gifsrc="https://img.te5.com/uploads/allimg/190915/120-1Z915135534.gif" src="http://js.18183.com/public/img/pixel.gif" data-url="https://img.te5.com/uploads/allimg/190915/120-1Z915135534.gif.jpg@q_80" /></span></p>
<p>
	<span style="color:#0000ff;">总结</span></p>
<p>
	本期就是为大家推荐的4大妙用金铲铲的非主流主C阵容，可以看出新版本对于金铲铲的利用逐渐多样，并且逐渐成为主流。大家可以多加练习掌握这些阵容的要点，带上小伙伴一起排位，让身边的小伙伴大开眼界。</p>

'''
    title = '四大非主流主C阵容推荐 纳尔猪妹异军突起'
    title,con = Clear_code(strs,title)
    print(title,con)
    save_image(strs,title,con)