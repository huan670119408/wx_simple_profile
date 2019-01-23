import itchat
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import os
import numpy as np

from pyecharts import Pie
import city_geo

# itchat.login()
itchat.auto_login(hotReload=True)
# itchat.send('天下之至柔，驰骋天下之至坚', 'filehelper')
friends = itchat.get_friends(update=True)

signature_list = []
nick_name_list = []
for i in friends[0:]:
    signature_list.append(i["Signature"])
    nick_name_list.append(i["NickName"])
    sex = i['Sex']
    # print(i)

geo = city_geo.CityGeo(friends)
geo_path = geo.render()
itchat.send_image(geo_path, "filehelper")
