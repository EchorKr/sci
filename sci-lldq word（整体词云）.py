from tkinter import _flatten

import pandas as pd
import jieba # 导入jieba分词库
import pandas as pd

data=pd.read_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\表面数据.xlsx') # 导入数据
da=data['评论'] # 提出评论一列
dacut=da.apply(jieba.lcut) # 对每一项进行分词
with open('C:\\Users\\86132\\Desktop\\pythonProject1\\停词表.txt','r',encoding='utf8') as f:###读入停词表
    stw=f.read()
stw=['\n','',' ','。','》','《','！','，',':','：','吗','得','着','这','啦','是','他','她','它','所','就','也','都','还','便','被','真的','里','中','的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一',
        '一个', '上', '也', '很', '到', '你', '说', '要', '去', '会', '对', '我们',
        '自己', '没有', '看', '可', '这','但','让','就是','不是','大','吧','还是','多','最后','可以','能','电影']+stw.split() # 设定停词表
datacut=dacut.apply(lambda x:[i for i in x if i not in stw]) # 进行停词处理
datacut

print(datacut)

cutname=pd.Series(_flatten(list(datacut))) # 展平每一项停词后结果
number=cutname.value_counts() # 统计词频


import matplotlib.pyplot as plt # 画图的库
from wordcloud import WordCloud # 导入画词云的库
# 导入 ImageColorGenerator 类
from wordcloud import ImageColorGenerator

mask=plt.imread('C:\\Users\\86132\\Desktop\\pythonProject1\\底图2.jpeg') # 读入词云底图
wc=WordCloud(font_path='C:\\Users\\86132\\Desktop\\pythonProject1\\STXINGKA.TTF',mask=mask,background_color='white') # 设定词云的字体，底图，背景颜色
plt.figure(figsize=(10,10)) # 设定画布大小
plt.imshow(wc.fit_words(number)) # 画出词云
plt.axis('off') # 去掉坐标轴
plt.savefig('C:\\Users\\86132\\Desktop\\pythonProject1\\整体词云.jpg')

'''
from PIL import ImageColor

# 配置字体颜色
font_colors = [
    '#155fc0',   #赛博蓝
    '#00d17c',   #机器绿
    '#ff26a8',   #霓虹粉
    '#bfc0c0',   #钛金属色
    '#282828',   #磨砂黑
    '#db241b',   #恶魔红
    '#606060',   #阴影灰
    '#51138a'    #宇宙紫
]

def get_font_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return ImageColor.getrgb(font_colors[random_state.randint(0, 7)])

# 设定画布大小和底图
width, height = 10000, 10000
mask = plt.imread('C:\\Users\\86132\\Desktop\\pythonProject1\\底图2.jpeg')

# 将宽度和高度传递给 WordCloud 对象
wc = WordCloud(width=width, height=height, font_path='C:\\Users\\86132\\Desktop\\pythonProject1\\STXINGKA.TTF', mask=mask, background_color='white', min_font_size=10, color_func=get_font_color)

# 获取该底图的颜色信息，用于生成字体颜色
image_colors = ImageColorGenerator(mask)

# 绘制词云，并重新着色
plt.figure(figsize=(10,10))
plt.imshow(wc.fit_words(number).recolor(color_func=image_colors, random_state=7), interpolation="bilinear")
plt.axis('off')
plt.savefig('C:\\Users\\86132\\Desktop\\pythonProject1\\整体词云.jpg')



from PIL import Image

width, height = 1000, 1000
# 读取图片并生成词云
mask=plt.imread('C:\\Users\\86132\\Desktop\\pythonProject1\\底图2.jpeg')

wc = WordCloud(width=width, height=height, font_path='C:\\Users\\86132\\Desktop\\pythonProject1\\STXINGKA.TTF', mask=mask, background_color='white', min_font_size=10)

# 设定不同颜色
color_list = [(21, 101, 192), (0, 209, 124), (255, 38, 168), (191, 192, 192),(40, 40, 40),(219, 36, 27),(81, 19, 138)]

# 获取该底图的颜色信息，用于生成字体颜色
image_colors = ImageColorGenerator(mask)

# 绘制词云，并重新着色
plt.figure(figsize=(10,10))
plt.imshow(wc.fit_words(number).recolor(color_func=image_colors, random_state=6), interpolation="bilinear")
plt.axis('off')
plt.savefig('C:\\Users\\86132\\Desktop\\pythonProject1\\整体词云.jpg')
'''


