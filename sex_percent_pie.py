from pyecharts import Pie

class SexPercentPie(object):

    def __init__(self,friends,theme = "dark"):
        self.friends = friends
        self.pie = Pie("{}的微信好友性别占比".format(friends[0]["NickName"]))
        self.pie.use_theme(theme)
        self.attr = ["男性好友", "女性好友", "其他"]

    def render(self):
        male = female = other = 0
        for i in self.friends[1:]:
            sex = i['Sex']
            if sex == 1:
                male += 1
            elif sex == 2:
                female += 1
            else:
                other += 1
        v1 = [male, female, other]
        self.pie.add("", self.attr, v1, is_label_show=True)
        self.pie.show_config()
        total = len(self.friends[1:])
        male_friend_percent = float(male) / total * 100
        female_friend_percent = float(female) / total * 100
        other_friend_percent = float(other) / total * 100
        print("好友总数：{}".format(total))
        print("男性好友：{:.2f}，个数：{}".format(male_friend_percent, male))
        print("女性好友：{:.2f}，个数：{}".format(female_friend_percent, female))
        print("其他：{:.2f}，个数{}".format(other_friend_percent, other))
        image_path = "images/sexPercentPie.png"
        self.pie.render(path=image_path)
        return image_path
