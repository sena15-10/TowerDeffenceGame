#敵の基底クラスを作成
import pygame
from character.character import Character
from obstacle.base_obstacle import BaseObstacle
import random

class BaseEnemy(Character):
    Z_ORDER = 2  # 敵キャラクターのZ-indexを2に設定
    def __init__(self, name, health, attack_power, speed=1, player=None, image_path=None):
        super().__init__(name, health, attack_power, speed, image_path)
        self.is_aggressive = True
        self.targets = []
        self.target = None
        self.type = "enemy"
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 600)
        self.last_attack_time = 0
        self.attack_cooldown = 1000
        self.attack_range = 50

    def set_target(self, targets):
        """ターゲットを設定するメソッド"""
        if not isinstance(targets, list):
            targets = [targets]
        self.targets = targets
        self.find_closest_target()

    def find_closest_target(self):
        """最も近いターゲットを見つけるメソッド"""
        closest_target = None
        min_distance = float('inf')

        for target in self.targets:
            # 破壊済みのターゲットは無視
            if hasattr(target, 'destroyed') and target.destroyed:
                continue

            if hasattr(target, 'rect'):
                distance = pygame.math.Vector2(self.rect.center).distance_to(pygame.math.Vector2(target.rect.center))
                if distance < min_distance:
                    min_distance = distance
                    closest_target = target
        
        self.target = closest_target

    def update (self):
        """敵の状態を更新するメソッド"""
        # ターゲットがいない、または現在のターゲットが破壊された場合は、新しいターゲットを探す
        if self.target is None or (hasattr(self.target, 'destroyed') and self.target.destroyed):
            self.find_closest_target()

        if self.target:
            target_pos = pygame.Vector2(self.target.rect.center)
            current_pos = pygame.Vector2(self.rect.center)
            direction = target_pos - current_pos
            distance = direction.length()

            if distance <= self.attack_range:
                self.try_attack()
            else:
                if distance > 0:
                    direction = direction.normalize()
                    self.rect.x += direction.x * self.speed
                    self.rect.y += direction.y * self.speed

    def can_attack(self):
        """攻撃可能かどうかを確認するメソッド"""
        current_time = pygame.time.get_ticks()
        return current_time - self.last_attack_time >= self.attack_cooldown

    def try_attack(self):
        """攻撃を試行するメソッド"""
        if self.can_attack() and self.target:
            self.attack_target()
            self.last_attack_time = pygame.time.get_ticks()

    def attack_target(self):
        """ターゲットに攻撃を実行するメソッド"""
        if self.target:
            if isinstance(self.target, (Character, BaseObstacle)):
                self.target.take_damage(self.attack_power)
                target_name = getattr(self.target, 'name', self.target.__class__.__name__)
                print(f"{self.name}が{target_name}を攻撃！{self.attack_power}のダメージ！")
