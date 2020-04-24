import numpy as np
from scipy.interpolate import interp2d
from pathlib import Path

class Terrain:
    def __init__(self):
        self.map = []
        self.map_x = []
        self.map_y = []
        self.map_z = []
        
    def load_data(self, area_list):
        # load data
        for name in area_list:
            path = Path(f"./dem/{name}.txt")
            if not path.exists():
                print(f"load_data error! {name}.txt file does not exist")
            with path.open() as data:
                map_temp = [[float(i) for i in line.split()]
                            for line in data.readlines()]
            self.map = self.map + map_temp

    def data_arange(self):
        # combine data
        self.map = sorted(self.map, key=lambda fmap: fmap[1])
        self.map_x = [i[0] for i in self.map]
        self.map_y = [i[1] for i in self.map]
        self.map_z = [i[2] for i in self.map]

    def center(self):
        # make (0,0) as center of the map
        self.center_x = (max(self.map_x) + min(self.map_x)) / 2
        self.center_y = (max(self.map_y) + min(self.map_y)) / 2
        self.map_x = list(np.array(self.map_x) - self.center_x)
        self.map_y = list(np.array(self.map_y) - self.center_y)

    def make_terrain(self, area_list, name):
        # make interpolate function
        self.load_data(area_list)
        self.data_arange()
        self.center()

        save_dir = Path("./interpolation")
        if not save_dir.exists():
            save_dir.mkdir()

        save_name = name
#        if name:
#            save_name = name 
#        else:
#            save_name = '+'.join(area_list)
        path = Path(f"./interpolation/{save_name}")

        terrain = interp2d(self.map_x, self.map_y, self.map_z) 
        np.save(path, np.array(terrain))
        return terrain
            
    def call_terrain(self, name):
        np_load_old = np.load
        np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
#        if not area_list and name:
#            call_name = name
#        elif area_list and not name:
#            call_name= '+'.join(area_list)
#        elif not all((area_list, name)):
#            print("Error: <area_list> or <name> have to be set.")
#        else:
#            call_name = name
        call_name = name
        path = Path(f"./interpolation/{call_name}.npy")
        terrain_temp = np.load(path)
        np.load = np_load_old
        terrain = terrain_temp.item()

        return terrain
            

