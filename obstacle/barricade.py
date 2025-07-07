
from obstacle.base_obstacle import BaseObstacle
class Barricade(BaseObstacle):
    def __init__(self,x, y, hp, width, height, image_path=None, destroyed_image_path=None, color=(100,100,100), lv=1):
        super().__init__(x, y, hp, width, height, image_path, destroyed_image_path, color, lv)
        self.type = "barricade"  # バリケードのタイプを設定
                
    
    
