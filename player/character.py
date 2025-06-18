import pygame
class Character:
    def __init__(self, name, image_path,health,attack_power,speed):
        self.health = health
        self.attack_power = attack_power
        self.speed = speed
        self.name = name
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.direction = pygame.Vector2(0, 0)
    def update(self, dx, dy):
        #入力値をもとに動く
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
    def set_direction(self, x, y):
        self.direction = pygame.Vector2(x, y)
    def stop(self):
        self.direction = pygame.Vector2(0, 0)
    def draw(self,surface):
        #画面に描画
        surface.blit(self.image, self.rect)
    def attack(self,target):
        pass