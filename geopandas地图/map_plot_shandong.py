import os
import geopandas as gpd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
os.chdir(os.path.split(os.path.realpath(__file__))[0])
print('copyright by Zhaosheng Zhang (misaraty@163.com)\n' + 'last update: 2024-08-17\n')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

gdf = gpd.read_file('370000_full.json')
fig, ax = plt.subplots()
gdf.plot(ax=ax, cmap='summer')

for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['name']):
    ax.annotate(label, xy=(x, y), xytext=(1.5, 1.5), textcoords="offset points", fontsize=6)
    ax.scatter(x, y, s=2, color='tab:orange')

ax.set_axis_off()
plt.savefig('map_shandong.jpg', dpi=1200, bbox_inches='tight')
plt.show()
plt.close()

