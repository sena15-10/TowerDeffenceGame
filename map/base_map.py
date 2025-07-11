import pygame
from resource.map_resouce import TILE_DEFINITIONS
from resource.resouce_maneger import ResouceManeger

#マップクラスの基底クラス
"""
BaseMapクラスは、2Dゲームのマップを表現するための基底クラスです。
1. マップの幅と高さを指定して初期化します。
2. マップ上のオブジェクトを管理するためのメソッドを
3.マップの大きさは各マップによって異なります。
"""

class BaseMap:
    Z_ORDER = 0  # 描画順序の基底値
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
        # オブジェクトを描画
        for obj in self.objects:
            # オブジェクトがカメラに写っているか判定
            print(obj.__class__.__name__) #どのオブジェクトが描画されるかどうかをデバック
            if self.camera.colliderect(obj.rect):
                # カメラからの相対位置を渡してオブジェクトを描画
                obj.draw(screen, self.camera)
        for y,row in enumerate(self._create_default_map()):
            for x,tile in enumerate(row):
                tile_info = TILE_DEFINITIONS.get(tile, {})
                image_id = tile_info.get('image')
                if image_id:
                    try:
                        tile_image = self.resource_maneger.load_image(image_id)
                        tile_x = x * self.tile_size - self.camera.left
                        tile_y = y * self.tile_size - self.camera.top
                        #カメラ内のみ表示する。
                        if (tile_x > -self.tile_size and tile_x < self.camera.width and
                        tile_y > -self.tile_size and tile_y < self.camera.height):
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