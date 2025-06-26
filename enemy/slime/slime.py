from enemy.base_enemy import BaseEnemy
class Slime(BaseEnemy):
    def __init__(self, name, health, attack_power, speed=1, player=None, image_path=None):
        super().__init__(name, health, attack_power, speed, player, image_path)
        self.is_aggressive = True  # スライムは攻撃的
        self.image_path = image_path if image_path else "enemy/slime/slime.png"  # デフォルトの画像パスを設定
