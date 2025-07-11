import pygame
from obstacle.base_obstacle import BaseObstacle
class Castle(BaseObstacle):
    #城、味方が守るべき場所
    def __init__(self, x, y, hp, width, height, image_path=None, color=(100, 100, 100), lv=1):
        super().__init__(x, y, hp, width, height, image_path, color, lv)
        self.type = "castle"  # 城のタイプを設定
        self.repiar_money = 300
        self.color = (200, 200, 200)  # 城の色を設定
    def heal(self, amount):
        if self.is_destroyed:
            return
        self.hp = min(self.hp + amount, self.max_hp)
        print(f"{self.type}は{amount}回復した。現在の体力: {self.hp}")

        
