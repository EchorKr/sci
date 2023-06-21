import matplotlib.pyplot as plt
import pandas as pd

# 读取地区数据.xlsx文件中的地址信息
data = pd.read_excel('地区数据0.xlsx')

# 筛选出国内数据
da1 = data['地址'][data['地址'][data['地址']!='国外'].index]

# 将省、市、自治区等各级行政区划级别提取为第一列
da2 = da1.apply(lambda x: x.split()[0])

# 统计每个省份的电影评论数量并排序
province_counts = da2.value_counts().sort_values(ascending=False)

# 设定需要展示的省份数量
n = 5

# 提取前 n 个电影评论数量最多的省份和占比
top_provinces = province_counts[:n] # 指定了需要展示的电影评论最多的前 n 个省份，并将它们存储在 top_provinces 变量中。
proportion = top_provinces / province_counts.sum() # 代码计算了每个省份的电影评论数量在总体评论数量中的占比，并将它们保存在 proportion 变量中

# 绘制饼图
plt.rcParams['font.sans-serif']=['SimHei']###显示中文
plt.rcParams['axes.unicode_minus'] = False
labels = top_provinces.index.tolist()
sizes = proportion.tolist() # 将电影评论最多的前几个省份的名称和占比转换为列表类型，并传递给 plt.pie() 函数以绘制对应的饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%') # 指定了显示饼图中每个部分占比的格式，即保留小数点后一位，同时添加百分号
plt.title(f'Top {n} 评论省份')
plt.axis('equal')
plt.savefig('C:\\Users\\86132\\Desktop\\pythonProject1\\Top5 评论省份.jpg')
plt.show()
