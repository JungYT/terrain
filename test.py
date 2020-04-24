from terrain import Terrain

terrain = Terrain()
#name_list = ["kangwon-yangyang"]
area_list = ["test_data", "test_data2"]
interpolation_name = "test"
dem_saved = terrain.make_terrain(area_list, interpolation_name)
dem_called = terrain.call_terrain(interpolation_name)

