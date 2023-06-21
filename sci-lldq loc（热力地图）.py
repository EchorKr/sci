import matplotlib.pyplot as plt
import pandas as pd
from pyecharts.charts import Geo #导入画地图的库
import pyecharts.options as opts # 设定风格
from pyecharts.globals import ChartType #设定风格

# 使用pandas库将地区数据.xlsx中的地址信息读入到内存中
data=pd.read_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\地区数据0.xlsx') # 导入数据
da1=data['地址'][data['地址'][data['地址']!='国外'].index] # 筛选出国内数据
da1=da1.value_counts() # 统计个数
# 画图
(Geo()
  # 创建“地图”对象，在地图中添加中国地图，为每个区域设置样式
 .add_schema(maptype='china',itemstyle_opts=opts.ItemStyleOpts(color="#005757", border_color="#fff"))
  # 向地图添加数据，这里传递了序列名称、地区和数据值，选择的数据类型为热力图
 .add(series_name='',data_pair=[(i,j) for i,j in zip(da1.index,da1.values)],type_=ChartType.HEATMAP)
 .set_series_opts(label_opts=opts.LabelOpts(is_show=False)) # 隐藏热力图上的项目标签
 .set_global_opts(visualmap_opts=opts.VisualMapOpts()) # 设置全局显示选项（包括可视化映射选项）采用默认设置
).render("map.html")
