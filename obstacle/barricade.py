import pygame
from obstacle.base_obstacle import BaseObstacle
class Barricade(BaseObstacle):
    """
    バリケードクラス。
    プレイヤーや敵の移動を阻む障害物として機能します。
    """
    def __init__(self, x, y, hp, width, height, image_path=None, color=(100, 100, 100), lv=1):
        super().__init__(x, y, hp, width, height, image_path, color, lv)
        self.type = "barricade"  # バリケードのタイプを設定
    def update(self):
        """
        バリケードの状態を更新します。
        静的な障害物なので、通常は何もしません。
        """
        pass
    def draw(self, screen):
        super().draw(screen)  # バリケードを描画
