import pygame
import random
class Character:
    def __init__(self, name,health,attack_power,speed=1,image_path=None):
        self.health = health
        self.attack_power = attack_power
        # speedをデフォルト1に
        self.speed = speed
        self.name = name
        self.current_health = health
        self.lv = 1
        self.exp = 0
        self.exp_to_next_lv = 100
        # self.image = pygame.image.load(image_path).convert_alpha()
        # self.rect = self.image.get_rect()
        #テスト用の画像
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # 赤色の四角形を代用
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.direction = pygame.Vector2(0, 0)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.set_direction(dx, dy)
        self.update()

    def set_direction(self, x, y):
        self.direction = pygame.Vector2(x, y)
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()


    def update(self):
        #入力値をもとに動く
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def draw(self,surface):
        #画面に描画
        surface.blit(self.image, self.rect)
    def is_alive(self):
        return self.current_health > 0
    def take_damage(self, damage):
        self.current_health -= damage
        print(f"{self.name}は{damage}のダメージを受けた。残りの体力: {self.current_health}")
        if self.current_health < 0:
            self.current_health = 0
        return self.current_health
    def attack(self,target):
        #エンターキーを押したときに攻撃
        pass


