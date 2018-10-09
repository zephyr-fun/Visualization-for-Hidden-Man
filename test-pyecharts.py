# -*- coding: utf-8 -*-
from pyecharts import Geo
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
data = [
    (u"海门", 9), (u"鄂尔多斯", 12), (u"招远", 12), (u"舟山", 12), (u"齐齐哈尔", 14), (u"盐城", 15),
    (u"赤峰", 16), (u"青岛", 18), (u"乳山", 18), (u"金昌", 19), (u"泉州", 21), (u"莱西", 21),
    (u"日照", 21), (u"胶南", 22), (u"南通", 23), (u"拉萨", 24), (u"云浮", 24), (u"梅州", 25),
    (u"文登", 25), (u"上海", 25), (u"攀枝花", 25), (u"威海", 25), (u"承德", 25), (u"厦门", 26),
    (u"汕尾", 26), (u"潮州", 26), (u"丹东", 27), (u"太仓", 27), (u"曲靖", 27), (u"烟台", 28),
    (u"福州", 29), (u"瓦房店", 30), (u"即墨", 30), (u"抚顺", 31), (u"玉溪", 31), (u"张家口", 31),
    (u"阳泉", 31), (u"莱州", 32), (u"湖州", 32), (u"汕头", 32), (u"昆山", 33), (u"宁波", 33),
    (u"湛江", 33), (u"揭阳", 34), (u"荣成", 34), (u"连云港", 35), (u"葫芦岛", 35), (u"常熟", 36),
    (u"东莞", 36), (u"河源", 36), (u"淮安", 36), (u"泰州", 36), (u"南宁", 37), (u"营口", 37),
    (u"惠州", 37), (u"江阴", 37), (u"蓬莱", 37), (u"韶关", 38), (u"嘉峪关", 38), (u"广州", 38),
    (u"延安", 38), (u"太原", 39), (u"清远", 39), (u"中山", 39), (u"昆明", 39), (u"寿光", 40),
    (u"盘锦", 40), (u"长治", 41), (u"深圳", 41), (u"珠海", 42), (u"宿迁", 43), (u"咸阳", 43),
    (u"铜川", 44), (u"平度", 44), (u"佛山", 44), (u"海口", 44), (u"江门", 45), (u"章丘", 45),
    (u"肇庆", 46), (u"大连", 47), (u"临汾", 47), (u"吴江", 47), (u"石嘴山", 49), (u"沈阳", 50),
    (u"苏州", 50), (u"茂名", 50), (u"嘉兴", 51), (u"长春", 51), (u"胶州", 52), (u"银川", 52),
    (u"张家港", 52), (u"三门峡", 53), (u"锦州", 54), (u"南昌", 54), (u"柳州", 54), (u"三亚", 54),
    (u"自贡", 56), (u"吉林", 56), (u"阳江", 57), (u"泸州", 57), (u"西宁", 57), (u"宜宾", 58),
    (u"呼和浩特", 58), (u"成都", 58), (u"大同", 58), (u"镇江", 59), (u"桂林", 59), (u"张家界", 59),
    (u"宜兴", 59), (u"北海", 60), (u"西安", 61), (u"金坛", 62), (u"东营", 62), (u"牡丹江", 63),
    (u"遵义", 63), (u"绍兴", 63), (u"扬州", 64), (u"常州", 64), (u"潍坊", 65), (u"重庆", 66),
    (u"台州", 67), (u"南京", 67), (u"滨州", 70), (u"贵阳", 71), (u"无锡", 71), (u"本溪", 71),
    (u"克拉玛依", 72), (u"渭南", 72), (u"马鞍山", 72), (u"宝鸡", 72), (u"焦作", 75), (u"句容", 75),
    (u"北京", 79), (u"徐州", 79), (u"衡水", 80), (u"包头", 80), (u"绵阳", 80), (u"乌鲁木齐", 84),
    (u"枣庄", 84), (u"杭州", 84), (u"淄博", 85), (u"鞍山", 86), (u"溧阳", 86), (u"库尔勒", 86),
    (u"安阳", 90), (u"开封", 90), (u"济南", 92), (u"德阳", 93), (u"温州", 95), (u"九江", 96),
    (u"邯郸", 98), (u"临安", 99), (u"兰州", 99), (u"沧州", 100), (u"临沂", 103), (u"南充", 104),
    (u"天津", 105), (u"富阳", 106), (u"泰安", 112), (u"诸暨", 112), (u"郑州", 113), (u"哈尔滨", 114),
    (u"聊城", 116), (u"芜湖", 117), (u"唐山", 119), (u"平顶山", 119), (u"邢台", 119), (u"德州", 120),
    (u"济宁", 120), (u"荆州", 127), (u"宜昌", 130), (u"义乌", 132), (u"丽水", 133), (u"洛阳", 134),
    (u"秦皇岛", 136), (u"株洲", 143), (u"石家庄", 147), (u"莱芜", 148), (u"常德", 152), (u"保定", 153),
    (u"湘潭", 154), (u"金华", 157), (u"岳阳", 169), (u"长沙", 175), (u"衢州", 177), (u"廊坊", 193),
    (u"菏泽", 194), (u"合肥", 229), (u"武汉", 273), (u"大庆", 279)]
geo = Geo("全国主要城市空气质量", "Data - PM2.5 - by yz", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], maptype='china', visual_text_color="#fff",
        symbol_size=10, is_visualmap=True)
geo.show_config()
geo.render("全国主要城市空气质量.html")  # 生成html文件
data = [ ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15), ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21), ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25)]
attr, value = geo.cast(data)
geo1 = Geo("全国主要城市空气质量热力图", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
geo1.add("空气质量热力图", attr, value, visual_range=[0, 25], type='heatmap',visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo1.show_config()
geo1.render(path="04-04空气质量热力图.html")



