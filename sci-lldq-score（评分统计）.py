import pandas as pd
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opts

# 读取数据并进行处理
data = pd.read_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\表面数据.xlsx')
rating_count = data['分数'].value_counts()

# 绘制柱状图
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(list(map(str, rating_count.index.tolist()))) # x轴 将评分的索引值转换为字符串格式，并以列表的形式传递给柱状图
        .add_yaxis('', rating_count.values.tolist()) # y 轴 将评分对应的数量以列表的形式传递给柱状图 将系列名称设置为空字符串可以省略图例
        .set_global_opts( # 全局显示选项
            title_opts=opts.TitleOpts(title="评分统计"),
            toolbox_opts=opts.ToolboxOpts(), # 创建工具箱，包含各种常用功能
            yaxis_opts=opts.AxisOpts(name='数量'),
            xaxis_opts=opts.AxisOpts(name='评分'),
        )
)

# 保存图像
bar.render("ratings.html")


bar.render("ratings.html")
