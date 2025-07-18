import pygame
import random
import math
from resource.map_resouce import TILE_DEFINITIONS
from resource.resouce_maneger import ResouceManeger
from obstacle.tree import Tree

#マップクラスの基底クラス
"""
BaseMapクラスは、2Dゲームのマップを表現するための基底クラスです。
1. マップの幅と高さを指定して初期化します。
2. マップ上のオブジェクトを管理するためのメソッドを
3.マップの大きさは各マップによって異なります。
"""

class BaseMap:
    Z_ORDER = -1  # 描画順序の基底値（最低レイヤー）
    def __init__(self, width, height, screen_width, screen_height, tile_size=64):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.resource_maneger = ResouceManeger() #マップの画像をシングルストンで管理する
        self.objects = []  # マップ上のオブジェクトを格納するリスト
        self.image = self._create_background_surface()
        self.rect = self.image.get_rect()
        self.camera = pygame.Rect(0, 0, screen_width, screen_height)
    def _create_background_surface(self):
        """タイルに基づいた背景サーフェスを生成します。"""
        background = pygame.Surface((self.width, self.height))
        # よりゲームらしい背景色に変更
        background.fill((40, 40, 40)) # 暗い灰色

        # 格子を描画してタイルを表現
        for x in range(0, self.width, self.tile_size):
            pygame.draw.line(background, (60, 60, 60), (x, 0), (x, self.height))
        for y in range(0, self.height, self.tile_size):
            pygame.draw.line(background, (60, 60, 60), (0, y), (self.width, y))
        return background

    def add_object(self, obj):
        """マップにオブジェクトを追加します。"""
        self.objects.append(obj)

    def remove_object(self, obj):
        """マップからオブジェクトを削除します。"""
        if obj in self.objects:
            self.objects.remove(obj)

    def update(self, target):
        """ターゲット（プレイヤー）に合わせてカメラを更新します。"""
        self.camera.center = target.rect.center
        # カメラがマップの範囲外に出ないようにする (clamp_ipで簡潔に)
        self.camera.clamp_ip(self.rect)

    def draw(self, screen):
        # 背景タイルを先に描画（最低レイヤー）
        self._draw_background_tiles(screen)
        
        # オブジェクトをZ_ORDERでソートして描画
        visible_objects = [obj for obj in self.objects if self.camera.colliderect(obj.rect)]
        visible_objects.sort(key=lambda obj: getattr(obj, 'Z_ORDER', 0))
        
        for obj in visible_objects:
            obj.draw(screen, self.camera)
    
    def _draw_background_tiles(self, screen):
        """背景タイルを効率的に描画します。"""
        map_data = self._create_default_map()
        
        # カメラの範囲内のタイルのみを計算
        start_x = max(0, self.camera.left // self.tile_size)
        end_x = min(len(map_data[0]), (self.camera.right + self.tile_size - 1) // self.tile_size)
        start_y = max(0, self.camera.top // self.tile_size)
        end_y = min(len(map_data), (self.camera.bottom + self.tile_size - 1) // self.tile_size)
        
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                if y < len(map_data) and x < len(map_data[y]):
                    tile = map_data[y][x]
                    tile_info = TILE_DEFINITIONS.get(tile, {})
                    image_id = tile_info.get('image')
                    if image_id:
                        try:
                            tile_image = self.resource_maneger.load_image(image_id)
                            tile_x = x * self.tile_size - self.camera.left
                            tile_y = y * self.tile_size - self.camera.top
                            screen.blit(tile_image, (tile_x, tile_y))
                        except Exception as e:
                            print(f"画像の読み込みに失敗しました: {image_id}")
                            raise e
    def _create_default_map(self):
        """マップのタイル配置を定義する2次元配列を生成します。"""
        tile_width = self.width // self.tile_size
        tile_height = self.height // self.tile_size
        # 例として、すべてのタイルをID 0 (例: 草地) で埋める
        return [[0 for _ in range(tile_width)] for _ in range(tile_height)]
    
   