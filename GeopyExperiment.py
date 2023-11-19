'''

This is the visualization map of Illinois for the analysis of poverty and gambling

Created:    Nov 2023, J. Dost

'''

# Imports
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Creating towns
towns = {"Chicago": (41.8781, -87.6298),
         "Rockford": (42.2711, -89.0937),
         "Champaign": (40.1164, -88.2434),
         "Peoria": (40.6936, -89.5890),
         "Springfield": (39.7817, -89.6501),
         "Bloomington": (40.4842, -88.9937),
         "Carbondale": (37.7273, -89.2168)
         }

# Making data frame for towns
towns_data = {"Town": list(towns.keys()), "Coordinates": [Point(coords[1], coords[0]) for coords in towns.values()]}
towns_gdf = gpd.GeoDataFrame(towns_data, geometry='Coordinates')

# Load the uploaded shapefile for Illinois
shapefile_path = '/mnt/data/IL_BNDY_State.zip'
illinois_map = gpd.read_file(shapefile_path)

# Ploting Illinois
fig, ax = plt.subplots(figsize=(10, 10))
illinois_map.plot(ax=ax, color='lightblue', edgecolor='black')

# Ploting towns
towns_gdf.plot(ax=ax, marker='o', color='red', markersize=50)

# Adding labels to towns
for town, coords in towns.items():
    ax.text(coords[1], coords[0], town, fontsize=12, ha='right', va='center')

plt.title('Map of Illinois with Selected Towns')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()