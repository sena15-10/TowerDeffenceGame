from character.character import Character
from character.playerable_charcter import PlayerableCharacter
import pygame

class SordPlayer(Character):
    def __init__(self, name, health, attack_power, speed=1, image_path=None):
        super().__init__(name, health, attack_power, speed, image_path)
        self.playerable_character =  PlayerableCharacter(self) # プレイヤー操作クラスのインスタンスを後で設定
        self.set_playerable_character(self.playerable_character)
        self.attack_range = 80 # 攻撃範囲

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
        
