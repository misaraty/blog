import os
import geopandas as gpd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
os.chdir(os.path.split(os.path.realpath(__file__))[0])
print('copyright by Zhaosheng Zhang (misaraty@163.com)\n' + 'last update: 2024-08-17\n')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

data = gpd.read_file('100000_full.json').to_crs('EPSG:4326')
nine_dotted_line = data.iloc[-1]
data = data[:-1]

fig, ax = plt.subplots()
ax = data.plot(ax=ax, column='name', cmap='summer', legend=False)
ax = gpd.GeoSeries(nine_dotted_line.geometry).plot(ax=ax, edgecolor='tab:green')
ax.set_aspect('equal', adjustable='datalim')
provincial_capitals = gpd.GeoDataFrame({
    'city': ['北京', '郑州', '成都', '广州', '台北', '上海', '重庆', '天津', '哈尔滨',
             '长春', '沈阳', '呼和浩特', '石家庄', '乌鲁木齐', '兰州', '西宁', '西安',
             '银川', '郑州', '济南', '太原', '合肥', '武汉', '长沙', '南京', '成都',
             '贵阳', '昆明', '拉萨', '杭州', '南昌', '广州', '福州', '海口', '香港',
             '澳门', '南宁'],
    'geometry': gpd.points_from_xy(
        [116.4074, 113.6500, 104.0665, 113.2644, 121.5201, 121.4737, 106.5516, 117.2009, 126.6425,
         125.3235, 123.4291, 111.7511, 114.5149, 87.6177, 103.8343, 101.7782, 108.9402,
         106.2325, 113.6500, 117.0009, 112.5492, 117.2830, 114.3054, 112.9388, 118.7969, 104.0665,
         106.6333, 102.7103, 91.1322, 120.1551, 115.8587, 113.2644, 119.2965, 110.1999, 114.1734,
         113.5439, 108.3665]
        ,[39.9042, 34.7570, 30.5723, 23.1291, 25.0458, 31.2304, 29.5630, 39.0842, 45.8022,
         43.8171, 41.8057, 40.8415, 38.0458, 43.8256, 36.0611, 36.6209, 34.3416,
         38.4872, 34.7570, 36.6512, 37.8706, 31.8206, 30.5951, 28.2282, 32.0603, 30.5723,
         26.6477, 25.0438, 29.6442, 30.2741, 28.6757, 23.1291, 26.0753, 20.0174, 22.3964,
         22.1860, 22.8160]
    )
})
provincial_capitals.plot(ax=ax, marker='o', color='tab:orange', markersize=1)
for x, y, label in zip(provincial_capitals.geometry.x, provincial_capitals.geometry.y, provincial_capitals.city):
    ax.annotate(label, xy=(x, y), xytext=(1, 1), textcoords="offset points", fontsize=4)
ax.tick_params(axis='both', which='major', labelsize=6)
plt.savefig('map_china.jpg', dpi=1200, bbox_inches='tight')
plt.show()
plt.close()