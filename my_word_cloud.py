from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import PIL.Image as Image
import os
import numpy as np


class MyWordCloud(object):

    def __init__(self, word_str, background_color="white", max_words=5000, mask_image="images/car.jpeg",
                 max_font_size=100, min_font_size=10, random_state=42,
                 font_path="fonts/simhei.ttf"):
        self.word_str = word_str
        self.font_path = font_path
        self.image_path = os.path.dirname(__file__) + "/images"
        self.background_color = background_color
        self.max_words = max_words
        self.mask_image = mask_image
        self.max_font_size = max_font_size
        self.min_font_size = min_font_size
        self.random_state = random_state
        self.font_path = font_path

    def save_file(self, image_name):
        np_array = np.array(Image.open(self.mask_image))
        world_cloud = WordCloud(background_color=self.background_color, max_words=self.max_words, mask=np_array,
                                max_font_size=self.max_font_size, min_font_size=self.min_font_size,
                                random_state=self.random_state,
                                font_path=self.font_path).generate(self.word_str)
        image_colors = ImageColorGenerator(np_array)
        plt.imshow(world_cloud.recolor(color_func=image_colors))
        plt.imshow(world_cloud)
        plt.axis("off")
        world_cloud.to_file(os.path.join(self.image_path, image_name))
        return os.path.dirname(self.image_path) + "/images/" + image_name
