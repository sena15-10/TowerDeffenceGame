import pygame
import random
from enemy.slime.slime import Slime
from resource.resouce_maneger import ResouceManeger
from resource.enemy_resouce import ENEMY_IMAGES 
class SlimeSpawner:
    def __init__(self, x, y, spawn_interval, game_map, enemies_list, player):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.spawn_interval = spawn_interval  # ミリ秒単位
        self.last_spawn_time = pygame.time.get_ticks()
        self.game_map = game_map
        self.enemies_list = enemies_list
        self.image_path = ENEMY_IMAGES["redSlime"]
        self.player = player
        self.color = (0, 255, 0) # スポナーの色を緑に

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > self.spawn_interval:
            self.spawn_slime()
            self.last_spawn_time = current_time

    def spawn_slime(self):
        # スポナーの周囲にランダムな位置でスライムを生成
        spawn_x = self.x + random.randint(-30, 30)
        spawn_y = self.y + random.randint(-30, 30)
        print(self.image_path)
        new_slime = Slime("Slime", 50, 5, 2, self.image_path)
        new_slime.rect.topleft = (spawn_x, spawn_y)
        ResouceManeger().load_image(self.image_path)
        self.game_map.add_object(new_slime)
        self.enemies_list.append(new_slime)
        print(f"New slime spawned at ({spawn_x}, {spawn_y})")

    def draw(self, screen, camera):
        # カメラからの相対位置を計算して描画
        pygame.draw.rect(screen, self.color, (self.x - camera.left, self.y - camera.top, self.width, self.height))
