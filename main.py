import pygame
from player.character import Character

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Example")
player = Character("Hero", 100, 10, 5)  # speedを1に
clock = pygame.time.Clock()  # 追加

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.handle_input()  # Handle player input
    screen.fill((0, 0, 0))  # Clear screen with black
    player.draw(screen)  # Draw player character
    pygame.display.flip()   # Update display
    clock.tick(60)  # 追加

pygame.quit()