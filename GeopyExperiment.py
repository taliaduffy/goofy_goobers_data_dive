'''

This is the visualization map of Illinois for the analysis of poverty and gambling

Created:    Nov 2023, J. Dost

'''

# Imports
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Creating towns (top 10 most populous, without Naperville & Cicero) + (top 5 most impoverished, with exceptions)
towns = {# Top 10 populous
         "Chicago": (41.8781, -87.6298),
         "Aurora": (41.7606, -88.3201),
         "Joliet": (41.5206, -88.1506),
         "Rockford": (42.2711, -89.0937),
         "Springfield": (39.7817, -89.6501),
         "Elgin": (42.0396, -88.3217),
         "Peoria": (40.6936, -89.5890),
         "Champaign": (40.1164, -88.2434),
         "Waukegan": (42.3608, -87.8341),
         "Bloomington": (40.4842, -88.9937),
         # Top 5 impoverished
         "Carbondale": (37.7273, -89.2168),
         "East St. Louis": (38.6164, -90.1598),
         "Harvey": (41.6076, -87.6519),
         "Macomb": (40.4592, -90.6718),
         "Danville": (40.1245, -87.6300),
         }

# Making data frame for towns
towns_data = {"Town": list(towns.keys()), "Coordinates": [Point(coords[1], coords[0]) for coords in towns.values()]}
towns_gdf = gpd.GeoDataFrame(towns_data, geometry='Coordinates')

# Load the uploaded shapefile for Illinois
shapefile_path = 'IL_BNDY_State_Ln.shp'
illinois_map = gpd.read_file(shapefile_path)

# Ploting Illinois
fig, ax = plt.subplots(figsize=(10, 10))
illinois_map.plot(ax=ax, color='lightblue', edgecolor='black')

# Ploting towns
towns_gdf.plot(ax=ax, marker='o', color='red', markersize=15)

# Adding labels to towns
for town, coords in towns.items():
    ax.text(coords[1], coords[0], town, fontsize=8, ha='right', va='center')

plt.title('Illinois Poverty/Gambling Comparison')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(False)
plt.show()