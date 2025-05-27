import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vampire Door Game")

font = pygame.font.SysFont(None, 32)

# Door properties
door_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 125, 150, 250)
window_rect = pygame.Rect(door_rect.centerx - 32, door_rect.y + 30, 64, 64)

# Dialogue
dialogue_box = pygame.Rect(100, 450, 600, 100)
dialogue_text = ""
knock_active = True
stranger_visible = False

# Stranger face colors (randomized later)
STRANGER_FACE_COLOR = (220, 50, 50)  # Red face as placeholder

clock = pygame.time.Clock()

while True:
    screen.fill((30, 30, 30))  # Background

    # Draw door
    pygame.draw.rect(screen, (139, 69, 19), door_rect)  # Main door
    pygame.draw.rect(screen, (80, 80, 80), window_rect)  # Window

    # Draw face in window
    if stranger_visible:
        pygame.draw.ellipse(screen, STRANGER_FACE_COLOR, window_rect.inflate(-10, -10))

    # Dialogue box
    pygame.draw.rect(screen, (10, 10, 10), dialogue_box)
    pygame.draw.rect(screen, (255, 255, 255), dialogue_box, 2)
    if knock_active:
        dialogue_text = "There is a knock at the door. Click to respond."
    if dialogue_text:
        text_surface = font.render(dialogue_text, True, (255, 255, 255))
        screen.blit(text_surface, (dialogue_box.x + 20, dialogue_box.y + 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if door_rect.collidepoint(event.pos) and knock_active:
                knock_active = False
                stranger_visible = True
                dialogue_text = "Stranger: Good evening... may I come in?"

    pygame.display.flip()
    clock.tick(60)
