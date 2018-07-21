
__author__ = 'zy'
__date__ = '2018/4/24 20:21'

import jieba
from wordcloud import WordCloud
from scipy.misc import imread
import matplotlib.pyplot as plt

text = open("F:\英雄时刻\啦啦\大数据课程论文.txt",'r+').read()
cut_text = "".join(jieba.cut(text),)
colour = imread("F:\英雄时刻\啦啦\\timg.jpg")
cloud = WordCloud(
    font_path = "HYQiHei-25J.ttf",
    background_colour = "white",
    #mask = color_mask,
    max_word = 50,
    max_font_size = 30
)
word_cloud = cloud.generate(cut_text)
word_cloud.to_file("wordcloud.jpg")

plt.imshow(word_cloud)
plt.axis('off')
plt.show()
