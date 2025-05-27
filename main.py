import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vampire Door Game")

# Load assets (place your actual sprites in the assets folder)
door_img = pygame.Surface((100, 200))
door_img.fill((139, 69, 19))  # Brown door

font = pygame.font.SysFont(None, 32)
player_rect = pygame.Rect(350, 400, 32, 64)
door_rect = pygame.Rect(370, 200, 100, 200)

# Game state
knock = True
interaction_text = ""

clock = pygame.time.Clock()

while True:
    screen.fill((30, 30, 30))  # Dark background

    # Draw door and player
    screen.blit(door_img, door_rect)
    pygame.draw.rect(screen, (100, 200, 250), player_rect)

    # Text prompt
    if knock:
        prompt = font.render("There is a knock at the door.", True, (255, 255, 255))
        screen.blit(prompt, (240, 50))

    if interaction_text:
        msg = font.render(interaction_text, True, (255, 255, 255))
        screen.blit(msg, (200, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 3
    if keys[pygame.K_RIGHT]:
        player_rect.x += 3

    # Check interaction
    if keys[pygame.K_SPACE] and player_rect.colliderect(door_rect):
        knock = False
        interaction_text = "You hear a voice... Do you let them in?"

    pygame.display.flip()
    clock.tick(60)
