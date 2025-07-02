import pygame

#マップクラスの基底クラス
"""
BaseMapクラスは、2Dゲームのマップを表現するための基底クラスです。
1. マップの幅と高さを指定して初期化します。
2. マップ上のオブジェクトを管理するためのメソッドを
3.マップの大きさは各マップによって異なります。
"""
class BaseMap:
    def __init__(self, width, height, screen_width, screen_height):
        self.width = width
        self.height = height
        self.objects = []  # マップ上のオブジェクトを格納するリスト
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255)) # 仮に白い背景にする
        self.rect = self.image.get_rect()
        self.camera = pygame.Rect(0, 0, screen_width, screen_height)

    def add_object(self, obj):
        """マップにオブジェクトを追加します。"""
        self.objects.append(obj)

    def remove_object(self, obj):
        """マップからオブジェクトを削除します。"""
        if obj in self.objects:
            self.objects.remove(obj)

    def update(self, target):
        """ターゲット（プレイヤー）に合わせてカメラを更新します。"""
        self.camera.center = target.rect.center
        # カメラがマップの範囲外に出ないようにする
        if self.camera.left < 0:
            self.camera.left = 0
        if self.camera.right > self.width:
            self.camera.right = self.width
        if self.camera.top < 0:
            self.camera.top = 0
        if self.camera.bottom > self.height:
            self.camera.bottom = self.height

    def draw(self, screen):
        """マップとマップ上のオブジェクトをカメラ視点で描画します。"""
        # 背景を描画
        screen.blit(self.image, (0, 0), self.camera)
        # オブジェクトを描画
        for obj in self.objects:
            # オブジェクトがカメラに写っているか判定
            if self.camera.colliderect(obj.rect):
                # カメラからの相対位置を渡してオブジェクトを描画
                obj.draw(screen, self.camera)