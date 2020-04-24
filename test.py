from terrain import Terrain

terrain = Terrain()
area_list = ["test_data", "test_data2"]
interpolation_name = "test"
dem_saved = terrain.interp_terrain(area_list, interpolation_name)
dem_called = terrain.get_terrain(interpolation_name)

