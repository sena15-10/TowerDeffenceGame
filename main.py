import pygame
from character.Player.sord_player import SordPlayer
from enemy.slime.slime import Slime
from obstacle.barricade import Barricade

# Pygame initialization
pygame.init()
#パソコンの画面サイズに合わせてウィンドウを作成
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame Example")
player = SordPlayer("Hero", 100, 10, 5)  # speedを1に
barricade = Barricade(400, 300, 100, 50, 100)  # 障害物を作成
enemy = Slime("Slime", 50, 5, 2,player)  # スライムのインスタンスを作成
enemies = [enemy]
clock = pygame.time.Clock()  # 追加

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ターゲットリストを動的に作成
    targets = [player]
    if not barricade.destroyed:
        targets.append(barricade)
    enemy.set_target(targets)

    player.update(enemies)  # 敵のリストを渡す
    enemy.update()  # Update enemy character
    screen.fill((0, 0, 0))  # Clear screen with black
    player.draw(screen)  # Draw player character
    barricade.draw(screen)  # Draw barricade
    enemy.draw(screen)   # Draw enemy character
    pygame.display.flip()   # Update display
    clock.tick(60)  # 追加

pygame.quit()