import pygame
from obstacle.base_obstacle import BaseObstacle

class EnemyBaseSpanner(BaseObstacle):

    def __init__(self, x, y, hp, width, height, image_path=None, color=(100, 100, 100), lv=1):
        super().__init__(x, y, hp, width, height, image_path, color, lv)
        self.type = "enemy_spawner"  # スポナーのタイプを設定
        self.spawned_enemies = []  # スポーンした敵キャラクターのリスト

    def spawn_enemy(self,player):
        """指定された敵クラスのインスタンスをスポーンします。"""
        enemy = get_enemy_class(player)
        self.spawned_enemies.append(enemy)
        return enemy
    def enemy_count(self):
        """スポーンした敵の数を返します。"""
        return len(self.spawned_enemies)
    def get_enemy_class(Self):
        """"それぞれの敵に対しての、敵クラスを返す"""
        return None  # ここではNoneを返すが、実際のゲームでは適切な敵クラスを返すように実装する必要があります。