import itchat
import my_word_cloud
import sex_percent_pie
import jieba
import pyecharts_word_cloud
import city_geo

def main():
    itchat.auto_login(hotReload=True)
    itchat.send('天下之至柔，驰骋天下之至坚', 'filehelper')
    friends = itchat.get_friends(update=True)
    # 昵称词云
    signature_list = []
    nick_name_list = []
    for i in friends[1:]:
        signature_list.append(i["Signature"])
        nick_name_list.append(i["NickName"])
    nick_name_space_split = " ".join(nick_name_list)
    nick_name_cloud = my_word_cloud.MyWordCloud(nick_name_space_split, mask_image="images/car.jpeg")
    nick_name_path = nick_name_cloud.save_file("nick_name.png")
    print(nick_name_path)
    itchat.send_image(nick_name_path, "filehelper")
    # 签名词云
    signature_text = "".join(signature_list)
    signature_word_jieba = jieba.cut(signature_text, cut_all=True)
    signature_word_space_split = " ".join(signature_word_jieba)
    signature_cloud = my_word_cloud.MyWordCloud(signature_word_space_split, mask_image="images/car.jpeg")
    signature_path = signature_cloud.save_file("signature.png")
    print(signature_path)
    itchat.send_image(signature_path, "filehelper")
    # 性别比例饼状图
    pie = sex_percent_pie.SexPercentPie(friends, theme="vintage")
    pie_image_path = pie.render()
    itchat.send_image(pie_image_path, "filehelper")
    # pyEcharts昵称词云
    word_cloud = pyecharts_word_cloud.PyechatesWordCloud(nick_name_list, width=2000, height=1000,
                                                                   name="pyechartsWordCloud", shape="circle",
                                                                   word_size_range=[10, 20], theme="vintage", word_gap=5)
    pyecharts_path = word_cloud.render()
    itchat.send_image(pyecharts_path, "filehelper")
    # 微信好友分布
    geo = city_geo.CityGeo(friends)
    geo_path = geo.render()
    itchat.send_image(geo_path, "filehelper")

if __name__ == '__main__':
    main()