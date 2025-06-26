from character.character import Character
from character.playerable_charcter import PlayerableCharacter
class SordPlayer(Character):
    def __init__(self, name, health, attack_power, speed=1, image_path=None):
        super().__init__(name, health, attack_power, speed, image_path)
        self.playerable_character =  PlayerableCharacter(self) # プレイヤー操作クラスのインスタンスを後で設定
        self.set_playerable_character(self.playerable_character)

    def set_playerable_character(self, playerable_character):
        self.playerable_character = playerable_character