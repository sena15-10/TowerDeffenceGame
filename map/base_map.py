import pygame
#マップクラスの基底クラス
"""
BaseMapクラスは、2Dゲームのマップを表現するための基底クラスです。
1. マップの幅と高さを指定して初期化します。
2. マップ上のオブジェクトを管理するためのメソッドを
3.マップの大きさは各マップによって異なります。
"""

class BaseMap:
    Z_ORDER = 0  # 描画順序の基底値
    def __init__(self, width, height, screen_width, screen_height, tile_size=64,map_tiles=None):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.objects = []  # マップ上のオブジェクトを格納するリスト
        self.image = self._create_background_surface()
        self.rect = self.image.get_rect()
        self.camera = pygame.Rect(0, 0, screen_width, screen_height)
        self.map_tiles = map_tiles  if map_tiles is not None else []
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
        """マップとマップ上のオブジェクトをカメラ視点で描画します。"""
        # 背景を描画
        screen.blit(self.image, (0, 0), self.camera)
        # オブジェクトを描画
        for obj in self.objects:
            # オブジェクトがカメラに写っているか判定
            if self.camera.colliderect(obj.rect):
                # カメラからの相対位置を渡してオブジェクトを描画
                obj.draw(screen, self.camera)
    def make_map(self, map_tiles):
        """マップのタイルを設定します。"""
        pass #ここで対応する画像を読み込み、タイルを設定する処理を実装します。
        # タイルを描画する処理を追加
    def defalute_map(self):
        return []