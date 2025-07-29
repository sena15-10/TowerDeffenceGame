import pygame
import random
from obstacle.base_obstacle import BaseObstacle

class Character:
    def __init__(self, name,health,attack_power,speed=1,image_path=None):
        self.health = health
        self.attack_power = attack_power
        # speedをデフォルト1に
        self.speed = speed
        self.name = name
        self.type = "player" #基底クラスでプレイヤー側っていう風に設定 
        self.current_health = health
        self.lv = 1
        self.exp = 0
        self.exp_to_next_lv = 100
        self.critical_chance = 0.3  # クリティカルヒットの確率
        self.critical_multiplier = 2.0  # クリティカルヒットのダメージ倍率
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
        else:
            # テスト用の画像
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))  # 赤色の四角形
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.direction = pygame.Vector2(0, 0)
        self.playerable_character = None  # 後で設定される
        self.set_direction(0, 0)  # 初期方向を設定

    def set_direction(self, x, y):  
        #方向を設定
        self.direction = pygame.Vector2(x, y)
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()


    def update(self, enemies=None,game_map=None):
        """
        キャラクターの基本的な更新処理。
        サブクラス（PlayerやBaseEnemy）でオーバーライドされることを想定。
        """
        # 基本的な移動ロジックのみ残す
        if self.direction.length() > 0:
            self.rect.x += self.direction.x * self.speed
            self.rect.y += self.direction.y * self.speed
    
    def _check_collision(self, new_x, new_y, game_map):
        """新しい位置でオブジェクトとの衝突をチェックします。
        - 自分自身とは衝突しない
        - 同じタイプ(敵同士、味方同士)のキャラクターとは衝突しない
        - 通行が許可されている障害物(passage_type)とは衝突しない
        - 上記以外とは衝突する
        """
        # 新しい位置での仮想的なrectを作成
        test_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

        # マップ上の全オブジェクトをチェック
        for obj in game_map.objects:
            # 自分自身はチェック対象外
            if obj == self:
                continue

            # --- 通り抜けられる条件 ---
            # 1. 相手が同じタイプのキャラクター(敵同士、味方同士)の場合
            if isinstance(obj, Character) and obj.type == self.type:
                continue
            # 2. 相手が障害物で、通行が許可されている(passage_typeが一致する)場合
            if isinstance(obj, BaseObstacle) and hasattr(obj, 'passage_type') and obj.passage_type == self.type:
                continue

            # --- 衝突判定 ---
            # 上記の「通り抜け」条件に当てはまらないオブジェクトと衝突するかチェック
            if hasattr(obj, 'rect') and test_rect.colliderect(obj.rect):
                return True  # 衝突を検出

        return False  # 衝突なし

    def draw(self, surface, camera):
        # カメラからの相対位置を計算して描画
        surface.blit(self.image, self.rect.move(-camera.left, -camera.top))
    def is_alive(self):
        #キャラクターが生きているかどうかを確認
        return self.current_health > 0
    
    
    def take_damage(self, damage):
        self.current_health -= damage
        print(f"{self.name}は{damage}のダメージを受けた。残りの体力: {self.current_health}")
        if self.current_health < 0:
            self.current_health = 0
        return self.current_health
    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.health:
            self.current_health = self.health
        print(f"{self.name}は{amount}回復した。現在の体力: {self.current_health}")
        return self.current_health
    
    def attack(self,target):
        #エンターキーを押したときに攻撃
        pass
        
