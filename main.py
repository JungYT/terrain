from terrain import Terrain
import plotly.graph_objects as go
import numpy as np

terrain = Terrain()
interpolation_name = "kangwon-yangyang"
dem_called = terrain.get_terrain(interpolation_name)

xlim = 1000 
ylim = 1000 
dx = 1
dy = 1
x = np.arange(-xlim, xlim, dx)
y = np.arange(-ylim, ylim, dy)
z = dem_called(x, y)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.show()

