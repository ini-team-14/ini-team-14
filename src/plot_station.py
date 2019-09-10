import csv
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

data_closet_at_road = '../data/closest_at_road.geojson'
data_roads_pads_network = '../data/roads_pads_network.geojson'

stat_dic = {}
with open('../data/20190829_stn_status.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        if row[6] == "Found":
            stat_dic[row[1]] = "Found"
        elif row[6] == "Not found":
            stat_dic[row[1]] = "Not found"
        else:
            stat_dic[row[1]] = "Neither"

#print(stat_dic)
plt.rcParams['figure.figsize'] = (15, 10)
df_stations = gpd.read_file(data_closet_at_road)
df_roads = gpd.read_file(data_roads_pads_network)

status = []

for index, row in df_stations.iterrows():
    stat_name = row['NAME']
    if stat_name in stat_dic:
        status.append(stat_dic[stat_name])
    else:
        status.append('Not sure')


df_stations['STATUS'] = status
df_stations_found = df_stations[(df_stations.STATUS == "Found")]
df_stations_not_found = df_stations[(df_stations.STATUS == "Not found")]
df_stations_neither = df_stations[(df_stations.STATUS == "Neither")]
df_stations_not_sure = df_stations[(df_stations.STATUS == "Not sure")]
#print(df_stations_found)
#print(df_stations_not_found)
#print(df_stations_neither)
#print(df_stations_not_sure)

fig, ax = plt.subplots()
ax.set_aspect('equal')
fig.suptitle('Stations Map');

df_roads.plot(ax=ax, color='black', edgecolor='black')
#df_stations.plot(ax=ax)
pl_found = df_stations_found.plot(ax=ax)
pl_not_found = df_stations_not_found.plot(ax=ax)
pl_neither = df_stations_neither.plot(ax=ax)
pl_not_sure = df_stations_not_sure.plot(ax=ax)

for index, row in df_stations_found.iterrows():
    pl_found.text(row['EASTING'] + 20, row['NORTHING'] + 20, row['NAME'])
for index, row in df_stations_not_found.iterrows():
    pl_not_found.text(row['EASTING'] + 20, row['NORTHING'] + 20, row['NAME'])
for index, row in df_stations_neither.iterrows():
    pl_neither.text(row['EASTING'] + 20, row['NORTHING'] + 20, row['NAME'])

plt.show()
