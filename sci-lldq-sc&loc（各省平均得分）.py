import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie

# 读取数据
data = pd.read_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\表面数据.xlsx')
region_data = pd.read_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\地区数据0.xlsx')

# 按照地址（省份）进行分组统计评分的平均值
rating_mean_by_region = data.groupby(region_data['地址'])['分数'].mean().reset_index()

# 绘制柱状图，展示不同省份评分的平均值
bar_chart = (# 函数创建一个柱状图对象
    Bar()
    .add_xaxis(rating_mean_by_region['地址'].tolist()) # 横轴 传递给柱状图对象，这里传递的是电影评论存在的省份
    .add_yaxis('平均评分', rating_mean_by_region['分数'].tolist()) # 纵轴 传递的不同省份电影评分的平均值；同时 '平均评分' 参数为数据序列指定了一个名称
    .set_global_opts( # 方法设置柱状图的全局选项，包括标题、横轴标签和纵轴标签等
        title_opts=opts.TitleOpts(title="各省份电影平均得分"),
        xaxis_opts=opts.AxisOpts(name='省份'),
        yaxis_opts=opts.AxisOpts(name='平均得分')
    )
)
bar_chart.render("sc-loc1.html")

'''
# 使用饼图展示电影评论数量最多的前几个省份
top_regions = rating_mean_by_region.sort_values(by='分数', ascending=False).head(5)['地址'].tolist()
region_counts = region_data['地址'].value_counts()
region_pie_data = [(region, count) for region, count in region_counts.items() if region in top_regions]
region_pie = (
    Pie()
    .add("", data_pair=region_pie_data)
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="电影评论数量最多的5个省份占比"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
)
region_pie.render("sc-loc2.html")
'''