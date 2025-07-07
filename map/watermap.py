
from resouce.map_resouce import TILE_WATER

# 画面サイズ(800x600)とタイルサイズ(64x64)を考慮したマップサイズ
# 幅: 800 / 64 = 12.5 -> 13タイル
# 高さ: 600 / 64 = 9.375 -> 10タイル
MAP_WIDTH = 13
MAP_HEIGHT = 10

# 全てが水タイルで構成されたマップデータ
WATER_MAP_DATA = [[TILE_WATER for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
