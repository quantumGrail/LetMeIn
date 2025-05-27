import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vampire Door Game")

# Font
font = pygame.font.SysFont(None, 32)

# Door
door_img = pygame.Surface((150, 250))
door_img.fill((139, 69, 19))  # Brown color
door_rect = door_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Game state
knock_active = True
interaction_text = ""

clock = pygame.time.Clock()

while True:
    screen.fill((30, 30, 30))  # Background color

    # Draw door
    screen.blit(door_img, door_rect)

    # Draw prompt
    if knock_active:
        prompt = font.render("There is a knock at the door. Click to respond.", True, (255, 255, 255))
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 50))

    if interaction_text:
        msg = font.render(interaction_text, True, (255, 255, 255))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if door_rect.collidepoint(event.pos) and knock_active:
                interaction_text = "You hear a voice... Do you let them in?"
                knock_active = False  # remove knock until next round

    pygame.display.flip()
    clock.tick(60)
