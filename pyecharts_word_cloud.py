from pyecharts import WordCloud
import random


class PyechatesWordCloud(object):

    def __init__(self, word_list, width=1300, height=620, name="", shape="circle", word_gap=20,
                 word_size_range=[12, 60], theme="dark"):
        value_list = []
        for word in word_list:
            value_list.append(random.randint(10, 100))
        self.wordcloud = WordCloud(width, height)
        self.wordcloud.add(name, word_list, value_list, word_size_range)
        self.wordcloud.use_theme(theme)

    def render(self):
        image_path = "images/pyechartsWordCloud.png"
        self.wordcloud.render(path=image_path)
        return image_path
