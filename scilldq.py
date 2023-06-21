import requests
from lxml import etree
import time
import re
from bs4 import BeautifulSoup
import pandas as pd

user=[]###用户名
recommend=[]###推荐
time=[]###评论时间
useful=[]###赞
comment=[]###评论正文
localurl=[]###用户详细页url
times=[]###评论具体时刻


print('创建ok0')

for i in range(25):###只会给用户看25页数据，然后网页的变化规律是每一页*20
    res=requests.get('https://movie.douban.com/subject/26266893/comments?start='+str(i*20)+'&limit=20&sort=new_score&status=P',
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
                        'Cookie': 'll="118254"; bid=BvDr7uyGn-4; __yadk_uid=gYFXCc7ucehhvmGLQKHpIknsWRiH7xMF; _vwo_uuid_v2=D5E998567A352A9612E58410B302E45B8|eadcb78c72256a151409bb364c3195c8; _ga=GA1.2.266715852.1685707008; _pk_id.100001.4cf6=ace4e6d679aafb10.1685707008.; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1685887712%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.266715852.1685707008.1685866572.1685887712.3; __utmc=30149280; __utmz=30149280.1685887712.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.235119827.1685707008.1685866572.1685887712.3; __utmb=223695111.0.10.1685887712; __utmc=223695111; __utmz=223695111.1685887712.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.1.10.1685887712; __gads=ID=eef85baaa3c0299d-22710f8021e1004d:T=1685707266:RT=1685887726:S=ALNI_MasZ373LJe4uQqDUuQFsaIOYd9rZg; __gpi=UID=00000c0ea76bccea:T=1685707266:RT=1685887726:S=ALNI_MZJxNJBLlAxHf0UcfBDBCNPYywxmA'})
    ht=etree.HTML(res.text)###xpath解析
    htt=BeautifulSoup(res.text,'lxml')###BeautifulSoup解析
    user=user+ht.xpath('//*[@id="comments"]/div/div/h3/span[2]/a/text()')
    recommend=recommend+ht.xpath('//*[@id="comments"]/div/div/h3/span[2]/span[2]/@title')
    time=time+[j.text for j in htt.find_all(name='span',class_='comment-time')]
    times=times+[t['title'] for t in htt.find_all(name='span',class_='comment-time')]
    useful=useful+ht.xpath('//*[@id="comments"]/div/div[2]/h3/span[1]/span/text()')
    comment=comment+ht.xpath('//*[@id="comments"]/div/div[2]/p/span/text()')
    localurl=localurl+ht.xpath('//*[@id="comments"]/div/div/h3/span[2]/a/@href')


print('爬取表面数据ok1.1')


local=[]###用户地址
addtime=[]###用户注册时间
n = 0
for m in localurl:
        ress=requests.get(m,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
                        'Cookie': 'll="118254"; bid=BvDr7uyGn-4; __yadk_uid=gYFXCc7ucehhvmGLQKHpIknsWRiH7xMF; _vwo_uuid_v2=D5E998567A352A9612E58410B302E45B8|eadcb78c72256a151409bb364c3195c8; _ga=GA1.2.266715852.1685707008; _pk_id.100001.4cf6=ace4e6d679aafb10.1685707008.; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1685887712%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.266715852.1685707008.1685866572.1685887712.3; __utmc=30149280; __utmz=30149280.1685887712.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.235119827.1685707008.1685866572.1685887712.3; __utmb=223695111.0.10.1685887712; __utmc=223695111; __utmz=223695111.1685887712.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.1.10.1685887712; __gads=ID=eef85baaa3c0299d-22710f8021e1004d:T=1685707266:RT=1685887726:S=ALNI_MasZ373LJe4uQqDUuQFsaIOYd9rZg; __gpi=UID=00000c0ea76bccea:T=1685707266:RT=1685887726:S=ALNI_MZJxNJBLlAxHf0UcfBDBCNPYywxmA'})
        httt=etree.HTML(ress.text)
        local=local+httt.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/a/text()')
        addtime=addtime+httt.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/div/text()[2]')
        print('pq2.1.0',n+2)
        n = n+1

print('爬取用户地址和注册时间ok2.1')


time=[re.sub('\n|\s+','',z) for z in time]###对评论时间进行清洗
# 将 time 转换为字符串，然后传递给 pd.to_datetime() 函数
'''
date = pd.to_datetime(str(time), format='%Y-%m-%d% H:%M:%S').date().strftime('%Y-%m-%d')

date = pd.to_datetime(time, format='%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
'''
da={'用户':user,'评分':recommend,'日期':time,'赞':useful,'评论':comment}
data=pd.DataFrame(da)
data['评分'] = data['评分'].astype(str)
data.loc[data['评分'].str.contains(' '), '评分'] = '无'###对评分进行设定
data['分数']=0

print('清洗数据ok2.2')


def score_to_rating(score):
    if score == '力荐':
        return 5
    elif score == '推荐':
        return 4
    elif score == '还行':
        return 3
    elif score == '较差':
        return 2
    elif score == '很差':
        return 1
    else:
        return 0

data['分数'] = data['评分'].apply(score_to_rating)
data.to_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\表面数据.xlsx')

'''
for i in range(len(data['评分'])):###划分依据为网站给出
    if data['评分'][i]=='力荐':
        data['分数'][i]=50
    if data['评分'][i]=='推荐':
        data['分数'][i]=40
    if data['评分'][i]=='还行':
        data['分数'][i]=30
    if data['评分'][i]=='较差':
        data['分数'][i]=20
    if data['评分'][i]=='很差':
        data['分数'][i]=10
    if data['评分'][i]=='无':
        data['分数'][i]=0
data.to_excel('C:\\Users\\dell\\Desktop\\表面数据.xlsx')
'''
print('评分划定ok3')


local1=[re.sub('[A-Z]','国外',m) for m in local]###对用户地址进行清洗
for k in range(len(local1)):
        if local1[k]=='中国香港':
            local1[k]='香港'
for k in range(len(local1)):
        if local1[k]=='中国台湾':
            local1[k]='台湾'
for k in range(len(local1)):
        if local1[k]=='中国澳门':
            local1[k]='澳门'
da1={'地址':local1}
dat=pd.DataFrame(da1)
dat['地址'] = dat['地址'].astype(str)
dat['地址'][dat['地址'].str.contains('国外')] = '国外'
for s in range(len(dat['地址'])):
    if len(dat['地址'][s])>2:
        dat['地址'][s]=dat['地址'][s][0:2]
for k in range(len(dat['地址'])):
        if dat['地址'][k]=='讷河':
            dat['地址'][k]='黑龙江'
dat.to_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\地区数据.xlsx')

print('地区处理ok4')

att={'时刻':times}
datt=pd.DataFrame(att)
datt.to_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\时刻数据.xlsx')
addtimes=[re.sub('\n','无',g) for g in addtime]###对注册时间进行清洗
addtimes=[re.sub('加入','',g) for g in addtimes]
ad={'注册时间':addtimes}
datad=pd.DataFrame(ad)
datad.drop(index=list(datad['注册时间'][datad['注册时间']=='无'].index),inplace=True)
datad.to_excel('C:\\Users\\86132\\Desktop\\pythonProject1\\注册时间数据.xlsx')

print('时间处理ok5')

'''
import matplotlib.pyplot as plt
date=data['日期'].value_counts()###统计频次
date=date.sort_index()
plt.rcParams['font.sans-serif']=['SimHei']###显示中文
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(10,8))
plt.plot(range(len(date)), date,marker='o',c='#00DB00')
plt.xticks(range(len(date)), date.index, rotation=45)
plt.grid()
plt.title('短评数量随日期的变化情况')
plt.xlabel("日期")
plt.ylabel('短评数量')
plt.savefig('C:\\Users\\86132\\Desktop\\pythonProject1\\短评量随时间变化图.jpg')
'''

'''
time = [re.sub('\n|\s+|(\d{4}-\d{2}-\d{2})\s*(\d{2}:\d{2}:\d{2})', r'\1 ', z) for z in time]
print(time)
date=data['日期'].value_counts()###统计频次
date=date.sort_index()
plt.rcParams['font.sans-serif']=['SimHei']###显示中文
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(10,8))
plt.plot(range(len(data)), time,marker='o',c='#00DB00')
plt.xticks(range(len(date)), date.index, rotation=45)
plt.grid()
plt.title('短评数量随日期的变化情况')
plt.xlabel("日期")
plt.ylabel('短评数量')
plt.savefig('C:\\Users\\86132\\Desktop\\pythonProject1\\\短评量随时间变化图1.jpg')
'''

import matplotlib.pyplot as plt
# 将日期数据转换为天精度
data['日期'] = pd.to_datetime(data['日期'], format='%Y-%m-%d%H:%M:%S').dt.date.astype(str)
# 创建新的数据框用于统计评论分数出现次数
tmp=pd.DataFrame(0,index=data['日期'].drop_duplicates().sort_values(),
                columns=data['分数'].drop_duplicates().sort_values())

# 统计每个分数段出现次数
for i,j in zip(data['日期'],data['分数']):
    tmp.loc[i,j] += 1

n,m = tmp.shape
plt.title('评分随时间变化', fontsize=16)
plt.figure(figsize=(10,5))
plt.rcParams['font.sans-serif']=['SimHei']###显示中文
plt.rcParams['axes.unicode_minus'] = False
for i in range(m):
    plt.plot(range(n),(-1 if i<3 else 1)*tmp.iloc[:, i],)
    plt.fill_between(range(n), (-1 if i<3 else 1)*tmp.iloc[:, i], alpha=0.8) ###循环画图
plt.grid()
plt.legend()
plt.xlabel('日期')
plt.ylabel('评论数量')
plt.xticks(range(n), tmp.index,rotation=45)
plt.savefig('C:\\Users\\86132\\Desktop\\pythonProject1\\评分随时间变化.jpg')


print('时间变化图ok6')

'''
if __name__ == '__scilldq__':
    # 定义表面数据文件路径
    data_file = '表面数据.xlsx'

    # 调用函数，获取评分随时间变化的数据
    time_score_data = analyze_scores_by_time(data_file)

    # 直接打印结果数据
    print(time_score_data)
    plt.show()
'''