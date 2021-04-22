# import jieba
import jieba.analyse
from os import path
import wordcloud
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

filename = "maogai.txt"

###当前文件路径
d = path.dirname(__file__)

with open(filename, encoding="utf-8") as f:
    text = f.read()


# 取top50词频，textrank是一种NLP算法，具体参阅官方文档
# https://amueller.github.io/word_cloud/index.html
# jieba分词非常的慢
text = jieba.analyse.textrank(text, topK=50, withWeight=True)

result = {}

for list in text:
    result[list[0]] = list[1]

image = Image.open('./img/heart.png')
graph = np.array(image)
wordc = WordCloud(font_path='./font/SimHei.ttf',  mask=graph, background_color='black', max_words=50, width=1920, height=1080)
# generate word cloud
wordc.generate_from_frequencies(result)
image_color = ImageColorGenerator(graph)

# store to file
wordc.to_file(path.join(d, "./img/result.jpg"))

# show
plt.imshow(wordc)
plt.imshow(wordc.recolor(color_func=image_color))
plt.axis("off")



