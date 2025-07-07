#マップのリソースすべてを管理するクラス
#マップサイズは基本的に64x64のタイルを使用
#タイルの画像はimg/mapフォルダに保存されている

# タイルIDをキーとし、プロパティを値とする辞書
# "image": 画像ファイルへのパス (プロジェクトルートのimg/からの相対パス)
# "walkable": キャラクターが通行可能かどうか
#[0,0,0,0]とかの形式でタイルを定義するのではなく、辞書で定義することで
# タイルのプロパティを柔軟に管理できるようにする
TILE_DEFINITIONS = {
    0: {"name": "grass", "image": "map/grass.png", "walkable": True},
    1: {"name": "water", "image": "map/maptile_mizu.png", "walkable": True},
    2: {"name": "water_lily", "image": "map/maptile_mizu_hasu_02.png", "walkable": True},
    # 必要に応じて他のタイル（道、森、壁など）を追加
    3: {"name": "dirt", "image": "map/dirt.png", "walkable": True},
}