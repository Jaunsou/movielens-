import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts.charts import Bar,Grid,Line,Pie
import pyecharts.options as opts
from pyecharts.globals import ThemeType
pd.set_option('display.max_columns', None)   #显示完整的列
movies = pd.read_csv('movies.dat',delimiter='::',
                     engine='python',header=None,names = ['Movie ID','Movie Title','Genre'],
                     encoding = 'utf-8')
movies.head()
users = pd.read_csv('users.dat', delimiter='::',
                    engine='python', header=None, names = ['User ID', 'Twitter ID'],
                    encoding='utf-8')
users.head()
ratings = pd.read_csv('ratings.dat', delimiter='::',
                      engine='python', header=None, names=['User ID', 'Movie ID', 'Rating', 'Rating Timestamp'],
                      encoding='utf-8')
ratings.head()
'''
movies.info()
users.info()
ratings.info()
'''
##print(ratings.describe())
plt.figure(figsize=[10,8])
plt.subplot(221)
plt.hist(x = ratings['Rating'], color = ['orange'])
plt.subplot(222)
plt.boxplot(x = ratings['Rating'], showmeans = True, meanline = True)
plt.grid()
plt.show()
movies[movies['Genre'].isnull()].head()
movies['Genre'].value_counts()
movies['Genre'].isnull().sum() / len(movies['Genre']) # 打印下空值比例
movies['Genre'].fillna('others',inplace=True)
genres = movies['Genre'].str.split('|').to_numpy()
from collections import defaultdict
counter = defaultdict(int)
for genre in genres:
    for e in genre:
        counter[e] += 1
#print(counter)
counter_sorted = sorted(counter.items(),key=lambda x: x[1])
#print(counter_sorted)
top10 = counter_sorted[-10:]
x = [ x for x,y in top10]
y = [ y for x,y in top10]
bar = (
    Bar(init_opts= opts.InitOpts(height='1200px'))
    .add_xaxis(x)
    .add_yaxis('电影种类名',y,category_gap='50%')
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title="电影种类及影片数"),
                     toolbox_opts=opts.ToolboxOpts())
    )
grid = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(bar, grid_opts=opts.GridOpts(pos_left="30%"))
       )
grid.render('chart1.html')

c = (
    Pie().add("", [list(z) for z in top10],radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
)
print(c.render('chart2.html'))


