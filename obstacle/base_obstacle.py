import pygame
class BaseObstacle:
    """
    Base class for obstacles in the environment.
    This class should be inherited by all specific obstacle types.
    """

    def __init__(self,x,y,hp,width,height,image_path=None, destroyed_image_path=None, color=(100,100,100),lv=1):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = hp
        self.width = width
        self.height = height
        self.image_path = image_path
        self.destroyed_image_path = destroyed_image_path # 破壊後の画像
        self.color = color
        self.lv = lv
        self.timer = 0 # タイマーを0で初期化
        self.is_destroyed = False
        self.type = "obstacle"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def is_colliding(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )
    def draw(self, screen, camera):
        # 破壊されていて、破壊後の画像がある場合
        if self.is_destroyed and self.destroyed_image_path:
            image = pygame.image.load(self.destroyed_image_path)
            image = pygame.transform.scale(image, (self.width, self.height))
            screen.blit(image, (self.x - camera.left, self.y - camera.top))
        # 通常の画像がある場合
        elif self.image_path:
            image = pygame.image.load(self.image_path)
            image = pygame.transform.scale(image, (self.width, self.height))
            screen.blit(image, (self.x - camera.left, self.y - camera.top))
        # 画像がない場合
        else:
            # 破壊されている場合は赤色で描画
            if self.is_destroyed:
                pygame.draw.rect(screen, (255, 90, 90), (self.x - camera.left, self.y - camera.top, self.width, self.height))
            else:
                pygame.draw.rect(screen, self.color, (self.x - camera.left, self.y - camera.top, self.width, self.height))

    def update(self):
        # 破壊されている場合
        if self.is_destroyed:
            self.timer -= 1
            if self.timer <= 0:
                return True # 削除を通知
        return False # 通常は削除しない

    def take_damage(self, damage):
        """障害物がダメージを受けるメソッド"""
        if self.is_destroyed:
            return
        self.hp -= damage
        if self.hp <= 0:
            self.destroy()
            self.hp = 0

    def destroy(self):
        """障害物を破壊するメソッド"""
        self.hp = 0
        self.is_destroyed = True
        self.timer = 300 # 破壊されたときにタイマーをセット

    def lv_up(self):
        """障害物のレベルを上げるメソッド"""
        self.lv += 1
        self.hp = int(self.hp * self.lv * 0.2)
        self.max_hp = self.hp