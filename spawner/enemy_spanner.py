import pygame
from obstacle.base_obstacle import BaseObstacle

class EnemyBaseSpanner(BaseObstacle):

    def __init__(self, x, y, hp, width, height, obj, image_path=None, color=(100, 100, 100), lv=1, spawn_interval=2000):
        super().__init__(x, y, hp, width, height, image_path, color, lv)
        self.obj = obj #敵のオブジェクトを格納
        self.type = "enemy_spawner"  # スポナーのタイプを設定
        self.passage_type = "enemy"  # 敵が通行可能な障害物
        self.spawned_enemies = []  # スポーンした敵キャラクターのリスト
        self.spawn_interval = spawn_interval  # ミリ秒単位でスポーン間隔
        self.last_spawn_time = pygame.time.get_ticks()  # 最後にスポーンした時刻

    def spawn_enemy(self):
        """指定された敵クラスのインスタンスをスポーンします。"""
        if not self.obj:
            raise ValueError("敵のオブジェクトが指定されていません。")
        enemy = self.obj()
        self.spawned_enemies.append(enemy)
        return enemy

    def update(self):
        """一定時間ごとに敵をスポーンする"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.spawn_interval:
            self.spawn_enemy()
            self.last_spawn_time = current_time

    def enemy_count(self):
        """スポーンした敵の数を返します。"""
        return len(self.spawned_enemies)
    def get_enemy_class(Self):
        """"それぞれの敵に対しての、敵クラスを返す"""
        return None  # ここではNoneを返すが、実際のゲームでは適切な敵クラスを返すように実装する必要があります。