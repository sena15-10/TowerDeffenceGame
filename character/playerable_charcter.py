#キャラクターの入力管理を行うクラス
import pygame
import pygame

class PlayerableCharacter:
    def __init__(self, player):
        self.player = player  # プレイヤーオブジェクト格納
        self.attack_pressed = False  # 攻撃ボタンの状態管理
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # 移動入力
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        
        # WASDキーでも移動可能
        if not (dx or dy):
            dx = keys[pygame.K_d] - keys[pygame.K_a]
            dy = keys[pygame.K_s] - keys[pygame.K_w]
        
        self.player.set_direction(dx, dy)
        
        # 攻撃入力（スペースキーまたはエンターキー）
        attack_key = keys[pygame.K_SPACE] or keys[pygame.K_RETURN]
        
        # 攻撃ボタンが押された瞬間のみ攻撃を実行（連続攻撃を防ぐ）
        if attack_key and not self.attack_pressed:
            # 攻撃処理は外部で実装される
            pass
        
        self.attack_pressed = attack_key
    
    def is_attack_pressed(self):
        """攻撃ボタンが押されているかを返す"""
        return self.attack_pressed