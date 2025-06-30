import pygame

class BaseObstacle:
    """
    障害物の基底クラス。
    静的なオブジェクトで、衝突判定を持つことを想定しています。
    """
    def __init__(self, x, y,hp, width, height, image_path=None, color=(100, 100, 100),lv=1,power=0):
        self.x = x
        self.y = y
        self.hp = hp * lv
        self.max_hp = hp
        self.width = width
        self.height = height
        self.lv = lv
        self.image = None
        self.color = color
        self.image_path = image_path
        self.destroyed = False #破壊されたかどうかのフラグ
        if image_path:
            try:
                # 画像を読み込み、指定されたサイズにスケーリング
                self.image = pygame.image.load(image_path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (width, height))
            except pygame.error as e:
                print(f"画像の読み込みに失敗しました: {image_path} - {e}")
                # 失敗した場合は色で塗りつぶした四角形を作成
                self.image = pygame.Surface([width, height])
                self.image.fill(color)
        else:
            # 画像パスが指定されていない場合は、色で塗りつぶした四角形を作成
            self.image = pygame.Surface([width, height])
            self.image.fill(color)

        # 障害物の矩形(rect)を設定
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        """
        障害物の状態を更新します。
        静的な障害物の場合、このメソッドは通常何もしません。
        アニメーションや移動する障害物のためにオーバーライドできます。
        """
        pass

    def draw(self, screen):
        """
        障害物を画面に描画します。

        Args:
            screen (pygame.Surface): 描画対象の画面。
        """
        if not self.destroyed:
            screen.blit(self.image, self.rect)
            
    def get_current_hp(self):
        return int(self.hp)
    def get_lv(self):
        return self.lv
    def is_destroyed(self):
        return self.hp <= 0
    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.is_destroyed():
            self.vanish()
            
    def vanish(self):
        self.destroyed = True
        print(f"{self.__class__.__name__}は破壊されました。")
