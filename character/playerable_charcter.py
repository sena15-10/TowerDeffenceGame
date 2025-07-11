#キャラクターの入力管理を行うクラス
import pygame

class PlayerableCharacter:
    def __init__(self, player):
        self.player = player  # プレイヤーオブジェクト格納
        self.attack_pressed = False  # 攻撃ボタンの状態管理
        self.barricade_key_pressed_time = 0
        self.barricade_place_threshold = 1000 # 1秒長押しで設置
    
    def handle_input(self, enemies=None, game_map=None):
        keys = pygame.key.get_pressed()
        
        # 移動入力
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        print(game_map.__class__)
        # WASDキーでも移動可能
        if not (dx or dy):
            dx = keys[pygame.K_d] - keys[pygame.K_a]
            dy = keys[pygame.K_s] - keys[pygame.K_w]
        
        self.player.set_direction(dx, dy)
        
        # 攻撃入力（スペースキーまたはエンターキー）
        attack_key = keys[pygame.K_SPACE] or keys[pygame.K_RETURN]
        
        # 攻撃ボタンが押された瞬間のみ攻撃を実行（連続攻撃を防ぐ）
        if attack_key and not self.attack_pressed:
            if enemies:
                self.player.attack(enemies)

        # 攻撃ボタンの状態を更新
        self.attack_pressed = attack_key

        # バリケード設置入力 (Bキー)
        self.handle_barricade_input(game_map,keys)
    def is_attack_pressed(self):
        """攻撃ボタンが押されているかを返す"""
        return self.attack_pressed
    
    def handle_barricade_input(self, game_map,keys):
        barricade_key = keys[pygame.K_b]
        if barricade_key:
            if self.barricade_key_pressed_time == 0:
                self.barricade_key_pressed_time = pygame.time.get_ticks()
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.barricade_key_pressed_time > self.barricade_place_threshold:
                    if game_map:
                        self.player.place_barricade(game_map)
                    self.barricade_key_pressed_time = 0 # リセット
                    print("リセットしました")
                    
        else:
            self.barricade_key_pressed_time = 0
