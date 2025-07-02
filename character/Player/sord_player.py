from character.character import Character
from character.playerable_charcter import PlayerableCharacter
import pygame
from obstacle.barricade import Barricade

class SordPlayer(Character):
    def __init__(self, name, health, attack_power, speed=1, image_path=None):
        super().__init__(name, health, attack_power, speed, image_path)
        self.playerable_character =  PlayerableCharacter(self) # プレイヤー操作クラスのインスタンスを後で設定
        self.set_playerable_character(self.playerable_character)
        self.attack_range = 80 # 攻撃範囲
        self.barricade_cooldown = 5000 # 5秒
        self.last_barricade_time = -5000 # 最初から設置できるように

    def set_playerable_character(self, playerable_character):
        self.playerable_character = playerable_character

    def attack(self, enemies):
        """射程内の最も近い敵に攻撃する"""
        closest_enemy = None
        min_distance = float('inf')

        for enemy in enemies:
            if hasattr(enemy, 'rect'):
                distance = pygame.math.Vector2(self.rect.center).distance_to(pygame.math.Vector2(enemy.rect.center))
                if distance < min_distance and distance <= self.attack_range:
                    min_distance = distance
                    closest_enemy = enemy
        
        if closest_enemy:
            closest_enemy.take_damage(self.attack_power)
            target_name = getattr(closest_enemy, 'name', closest_enemy.__class__.__name__)
            print(f"{self.name}が{target_name}を攻撃！{self.attack_power}のダメージ！")

    def can_place_barricade(self):
        current_time = pygame.time.get_ticks()
        return current_time - self.last_barricade_time >= self.barricade_cooldown

    def place_barricade(self, game_map):
        if self.can_place_barricade():
            # プレイヤーの向きに応じてバリケードを設置
            if self.direction.length() > 0:
                # プレイヤーの前方に設置
                offset = self.direction * 60 # プレイヤーの60ピクセル前に設置
                barricade_x = self.rect.centerx + offset.x
                barricade_y = self.rect.centery + offset.y
            else:
                # プレイヤーが静止している場合は、すぐ右に設置
                barricade_x = self.rect.right + 20
                barricade_y = self.rect.centery

            new_barricade = Barricade(barricade_x, barricade_y, 100, 100, 50)
            game_map.add_object(new_barricade)
            self.last_barricade_time = pygame.time.get_ticks()
            print("Barricade placed!")
        else:
            print("Barricade on cooldown.")
        
