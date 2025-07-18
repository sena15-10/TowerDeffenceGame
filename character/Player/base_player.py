from character.character import Character
from character.Player.playerable_charcter import PlayerableCharacter
class BasePlayer(Character):
    def __init__(self, name, health, attack_power, speed=1, image_path=None):
        super().__init__(name, health, attack_power, speed, image_path)
        self.playerable_character = PlayerableCharacter(self)
        self.type = "player"
    

    def update(self, enemies=None, game_map=None):
        """
        キー入力に基づきキャラクターを更新し、障害物との衝突を処理します。
        """
        # 入力処理
        if self.playerable_character:
            self.playerable_character.handle_input(enemies, game_map)

        # 移動を試行
        new_x = self.rect.x + self.direction.x * self.speed
        new_y = self.rect.y + self.direction.y * self.speed

        # 障害物との衝突をチェック
        if game_map and not self._check_collision(new_x, new_y, game_map):
            self.rect.x = new_x
            self.rect.y = new_y
        # 衝突する場合は移動しない（元の位置を維持）
