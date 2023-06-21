import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# 加载数据
time_data = pd.read_excel('时刻数据.xlsx')
times = list(time_data['时刻'])

data = pd.read_excel('表面数据.xlsx')

# 修改日期格式
date = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d') for t in times]
data['日期'] = date
data['编号'] = range(1, len(data) + 1)

# 统计短评数量并可视化 统计每个日期上的短评数量，并按日期排序
date_counts = data['日期'].value_counts()
date_counts = date_counts.sort_index()
# 使用matplotlib库绘制出日期与对应的短评数量关系图
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(10,8)) # 创建了一个尺寸为10x8英寸（单位可以是像素）的画布对象fig
plt.plot(range(len(date_counts)), date_counts, marker='o',c='#00DB00') # X坐标轴的取值范围，(0,7)，即从 0 到 6 的整数序列 date_counts Y 表示某段时间内各日期出现次数的统计结果
plt.xticks(range(len(date_counts)), date_counts.index, rotation=45) # 设置坐标轴刻度标签参数 xtick 的位置，xtick 标签的文本内容 即 date_counts 中日期的名称
plt.grid() # 添加网格线
plt.title('短评数量随日期的变化情况')
plt.xlabel("日期")
plt.ylabel('短评数量')
plt.savefig('短评量随时间变化图（每天）.jpg')
