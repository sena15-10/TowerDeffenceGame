import pygame
class BaseObstacle:
    """
    Base class for obstacles in the environment.
    This class should be inherited by all specific obstacle types.
    """

    def __init__(self,x,y,hp,width,height,image_path=None,color=(100,100,100),lv=1):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = hp
        self.width = width
        self.height = height
        self.image_path = image_path
        self.color = color
        self.lv = lv
        self.timer = 300 # 破壊されたオブジェクトを描画する時間
        self.is_destroyed = False  # ← 属性名を変更
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
        if self.image_path:
            image = pygame.image.load(self.image_path)
            image = pygame.transform.scale(image, (self.width, self.height))
            screen.blit(image, (self.x - camera.left, self.y - camera.top))
        else:
            pygame.draw.rect(screen, self.color, (self.x - camera.left, self.y - camera.top, self.width, self.height))
    def update(self):
        #攻撃する障害物のみ
        pass
    def take_damage(self, damage):
        """障害物がダメージを受けるメソッド"""
        if self.is_destroyed:  # ← ここも修正
            return
        self.hp -= damage
        if self.hp <= 0:
            self.destroy()  # ← メソッド名も修正
            self.hp = 0  # HPが0以下にならないようにする
    
    def destroy(self):  # ← メソッド名を変更
        """障害物を破壊するメソッド"""
        self.hp = 0
        self.is_destroyed = True  # ← ここも修正
        # ここで必要な後処理を行う（例: オブジェクトの削除、アニメーションの再生など）
        # 例えば、障害物をマップから削除する場合は、マップのオブジェクトリスト
    def lv_up(self):
        """障害物のレベルを上げるメソッド"""
        self.lv += 1
        self.hp = int(self.hp * self.lv * 0.2)
        self.max_hp = self.hp
        # レベルアップに伴う他の属性の変更があればここで行う
        # 例えば、攻撃力や防御力の増加など
    
    #一定期間壊れたオブジェクトを描画するメソッド
    def draw_destroyed(self, screen, camera):
        """破壊されたオブジェクトを描画するメソッド"""
        if self.is_destroyed:  # ← ここも修正
            # 破壊されたオブジェクトの画像やアニメーションを描画
            # ここでは単純に色を変えて表示する例
            pygame.draw.rect(screen, (255, 0, 0), (self.x - camera.left, self.y - camera.top, self.width, self.height))
            #壊れた場合self.timer秒描画してからマップから削除する
            self.timer -= 1
            if self.timer <= 0:
                print("オブジェクトが削除されました")
                pass