import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'  # 设置使用的字体为黑体

# 读取表面数据和时刻数据表格
surface_data = pd.read_excel('表面数据.xlsx', index_col=0)
time_data = pd.read_excel('时刻数据.xlsx')

# 合并两个表格
data = pd.merge(surface_data.reset_index(), time_data.reset_index(), on='index', how='inner')

# 进行情感分析(英文情感分析，所以没有结果，后续对其进一步完善)
from textblob import TextBlob

def sentiment_score(comment):
    return TextBlob(comment).sentiment.polarity

data['情感得分'] = data['评论'].apply(sentiment_score)

# 对时间进行处理
data['日期'] = pd.to_datetime(data['日期'], format='%Y-%m-%d%H:%M:%S')
data['月份'] = data['日期'].dt.strftime('%Y-%m')

grouped_data = data.groupby('月份', as_index=False).agg({'评论': 'count', '情感得分': 'mean'})

# 可视化影评趋势
plt.plot('月份', '评论', data=grouped_data, label='评论数')
plt.plot('月份', '情感得分', data=grouped_data, label='情感得分')
plt.xticks(rotation=45)
plt.legend()

# 添加标签
plt.xlabel('时间(年-月)')
plt.ylabel('数量')
plt.title('影评趋势（每月）')
plt.show()

'''
from nltk.sentiment import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()

def sentiment_score(comment):
    return sentiment_analyzer.polarity_scores(comment)['compound']

data['情感得分'] = data['评论'].apply(sentiment_score)
'''