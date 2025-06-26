import pygame
from character.Player.sord_player import SordPlayer
from enemy.slime.slime import Slime
# Pygame initialization
pygame.init()
#パソコンの画面サイズに合わせてウィンドウを作成
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame Example")
player = SordPlayer("Hero", 100, 10, 5)  # speedを1に
enemy = Slime("Slime", 50, 5, 2,player)  # スライムのインスタンスを作成
clock = pygame.time.Clock()  # 追加
enemy.set_target(player)  # スライムのターゲットをプレイヤーに設定
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update()  # Update player character based on input
    enemy.update()  # Update enemy character
    screen.fill((0, 0, 0))  # Clear screen with black
    player.draw(screen)  # Draw player character
    enemy.draw(screen)   # Draw enemy character
    pygame.display.flip()   # Update display
    clock.tick(60)  # 追加

pygame.quit()