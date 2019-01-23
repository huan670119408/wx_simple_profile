from pyecharts import Geo


class CityGeo(object):

    def __init__(self, friends):
        beijing_city = [
            "东城", "西城", "朝阳", "丰台", "石景山", "海淀", "顺义", "通州", "大兴", "房山", "门头沟", "昌平", "平谷", "密云", "怀柔", "延庆"]
        shanghai_city = [
            "宝山", "长宁", "崇明", "奉贤", "虹口", "黄浦", "嘉定", "金山", "静安", "卢湾", "闵行", "浦东新区", "普陀", "青浦", "松江", "徐汇", "杨浦",
            "闸北"]
        tianjin_city = [
            "宝坻", "北辰", "滨海新区", "东丽", "和平", "河北", "河东", "河西", "红桥", "蓟县", "津南", "静海", "南开", "宁河", "武清", "西青"]
        chongqing_city = [
            "巴南", "北碚", "璧山", "长寿", "城口", "大渡口", "大足", "垫江", "丰都", "奉节", "涪陵", "合川", "江北", "江津", "九龙坡", "开县", "梁平",
            "两江新区",
            "南岸", "南川", "彭水",
            "綦江", "黔江", "荣昌", "沙坪坝", "石柱", "双桥", "铜梁", "潼南", "万盛", "万州", "巫山", "巫溪", "武隆", "秀山", "永川", "酉阳", "渝北", "渝中",
            "云阳", "忠县"]
        city_dict = {}
        for friend in friends:
            city = friend["City"]
            if len(city) != 0:
                if city in beijing_city:
                    city = "北京"
                elif city in shanghai_city:
                    city = "上海"
                elif city in tianjin_city:
                    city = "天津"
                elif city in chongqing_city:
                    city = "重庆"
                if city in city_dict.keys():
                    value = city_dict[city]
                    value += 1
                    city_dict[city] = value
                else:
                    city_dict[city] = 1
        self.data = []
        self.geo = Geo(
            friends[0]["NickName"] + "的微信好友全国分布",
            "",
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59",
        )

        for key, value in city_dict.items():
            coordinate = self.geo.get_coordinate(key)
            if coordinate is None:
                print(key + "不在中国区...")
                continue
            self.data.append((key, value))
        attr, value = self.geo.cast(self.data)
        self.geo.add(
            "",
            attr,
            value,
            visual_range=[0, 30],
            visual_text_color="#fff",
            symbol_size=15,
            is_visualmap=True,
        )

    def render(self):
        print(self.data)
        image_path = "images/cityGeo.png"
        self.geo.render(path=image_path)
        return image_path
