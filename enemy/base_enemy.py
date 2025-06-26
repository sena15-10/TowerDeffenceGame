#敵の基底クラスを作成
import pygame 
from character.character import Character
import random
class BaseEnemy(Character):
    def __init__(self, name, health, attack_power, speed=1, player=None, image_path=None):  
        super().__init__(name, health, attack_power, speed, image_path)
        self.is_aggressive = True  # 敵が攻撃的かどうかのフラグ
        self.target = None  # プレイヤーなどのターゲットを設定するための変数
        self.charcter = player # プレイヤーキャラクターかほかキャラクターかのフラグのための変数
        self.type = "enemy"
        self.rect = self.image.get_rect()  # 画像の矩形を取得
        self.rect.x = random.randint(0, 800)  # 画面の幅に合わせてランダムな位置を設定
        self.rect.y = random.randint(0, 600)  # 画面の
        self.last_attack_time = 0  # 最後の攻撃時間
        self.attack_cooldown = 1000  # 攻撃クールダウン（ミリ秒）
        self.attack_range = 60  # 攻撃射程
    def set_target(self, target):
        """ターゲットを設定するメソッド"""
        if not isinstance(target, Character):
            raise ValueError("ターゲットはCharacterのインスタンスでなければなりません。")
        self.target = target
    def update (self):
        """敵の状態を更新するメソッド"""
        if self.target:
            # プレイヤーの方向を計算
            target_pos = pygame.Vector2(self.target.rect.center)
            current_pos = pygame.Vector2(self.rect.center)
            direction = target_pos - current_pos
            distance = direction.length()
            
            # 攻撃範囲内かチェック
            if distance <= self.attack_range:
                self.try_attack()
            else:
                # 方向を正規化して移動
                if distance > 0:
                    direction = direction.normalize()
                    self.rect.x += direction.x * self.speed
                    self.rect.y += direction.y * self.speed   
    def target_get_distance(self,target):
        """ターゲットの距離が近いかどうかを確認するメソッド""" 
        if self.target:
            distance = self.rect.center.distance_to(self.target.rect.center)
            return distance
        return None
    
    def can_attack(self):
        """攻撃可能かどうかを確認するメソッド"""
        current_time = pygame.time.get_ticks()
        return current_time - self.last_attack_time >= self.attack_cooldown
    
    def try_attack(self):
        """攻撃を試行するメソッド"""
        if self.can_attack() and self.target and self.check_collision():
            self.attack_target()
            self.last_attack_time = pygame.time.get_ticks()
    
    def check_collision(self):
        """プレイヤーとの衝突をチェックするメソッド"""
        if self.target:
            return self.rect.colliderect(self.target.rect)
        return False
    
    def attack_target(self):
        """ターゲットに攻撃を実行するメソッド"""
        if self.target:
            self.target.take_damage(self.attack_power)
            print(f"{self.name}が{self.target.name}を攻撃！{self.attack_power}のダメージ！")