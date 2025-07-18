import pygame
import random
from character.Player.sord_player import SordPlayer
from enemy.slime.slime import Slime
from obstacle.barricade import Barricade
from map.water_map import WaterMap
from spawner.slime_spanner import SlimeSpawner

# Pygame initialization
pygame.init()

#パソコンの画面サイズに合わせてウィンドウを作成
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame Example")

# マップを作成
game_map = WaterMap(2500, 2500, width, height)

player = SordPlayer("Hero", 100, 10, 5)  # speedを1に
enemies = []

# スポナーを配置
spawners = []
for _ in range(random.randint(4, 20)):
    spawner_x = random.randint(0, game_map.width - 50)
    spawner_y = random.randint(0, game_map.height - 50)
    spawner = SlimeSpawner(spawner_x, spawner_y, 5000, game_map, enemies, player) # 5秒ごとにスライムを生成
    spawners.append(spawner)
    game_map.add_object(spawner)

# バリケードを配置
for _ in range(random.randint(3, 4)):
    barricade_x = random.randint(0, game_map.width - 100)
    barricade_y = random.randint(0, game_map.height - 50)
    barricade = Barricade(barricade_x, barricade_y, 100, 100, 50)
    game_map.add_object(barricade)

# オブジェクトをマップに追加
game_map.add_object(player)

clock = pygame.time.Clock()  # 追加

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # ターゲットリストを動的に作成
    targets = []
    for obj in game_map.objects:
        if isinstance(obj, Barricade) and not obj.is_destroyed: # バリケードが破壊されていない場合
            targets.append(obj) if obj not in targets else None
        
    for enemy in enemies:
        enemy.set_target(targets + [player]) # 敵のターゲットを更新
        enemy.game_map = game_map  # 敵にマップ情報を提供

    player.update(enemies,game_map)  # 敵のリストを渡す
    for spawner in spawners:
        spawner.update()
    for enemy in enemies:
        enemy.update()  # Update enemy character
    game_map.update(player) #プレイヤーに合わせてカメラを更新

    # 6. 画面更新
    screen.fill((0, 0, 0))  # Clear screen
    game_map.draw(screen)   # Draw map and objects
    pygame.display.flip()  # Update the full display Surface to the screen

    clock.tick(60)  # 60 FPSに制限
