import random
from obstacle.base_obstacle import BaseObstacle

class Tree(BaseObstacle):
    """
    Tree obstacle class - impassable for all character types.
    Trees are permanent obstacles that cannot be destroyed.
    """
    
    Z_ORDER = 1  # Trees appear above ground but below flying objects
    
    def __init__(self, x, y, tree_type=None, tile_size=64):
        # Tree images from map resources
        tree_images = {
            1: "resource/img/map/ki_01.png",
            2: "resource/img/map/ki_02.png"
        }
        # Random tree type if not specified
        if tree_type is None:
            tree_type = random.choice([1, 2])
        
        image_path = tree_images.get(tree_type, tree_images[1])
        # Trees are indestructible (very high HP)
        super().__init__(
            x=x, 
            y=y, 
            hp=999999,  # Effectively indestructible
            width=tile_size, 
            height=tile_size,
            image_path=image_path,
            color=(34, 139, 34),  # Forest green fallback color
            lv=1
        )
        self.type = "tree" # super()の後にtypeを設定
        self.target = False #オブジェクトが敵から狙われるかどうかの判定
        self.tree_type = tree_type
        
    def take_damage(self, damage):
        """Trees cannot be destroyed"""
        pass
    
    def destroy(self):
        """Trees cannot be destroyed"""
        pass
    
    def is_passable(self):
        """Trees are always impassable"""
        return False