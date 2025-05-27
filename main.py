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

stranger_profile = {
    "skin_color": (220, 50, 50),
    "eye_color": (255, 255, 255),
    "pupil_color": (0, 0, 0),
    "is_vampire": True,
    "expression": "smirk",  # or "neutral", "grin"
    "has_fangs": True,
    "eye_shape": "slit",    # or "round"
}

questions_asked = 0
max_questions = 3
dialogue_responses = [
    "I just need a place to stay.",
    "I was walking all night.",
    "Is it so wrong to knock politely?"
]

# Stranger face colors (randomized later)
STRANGER_FACE_COLOR = (220, 50, 50)  # Red face as placeholder

def draw_stranger_face(surface, rect, profile):
    # Head
    pygame.draw.ellipse(surface, profile["skin_color"], rect)

    # Eyes
    eye_y = rect.y + 20
    eye_radius = 8
    eye_offset = 12
    left_eye = (rect.centerx - eye_offset, eye_y)
    right_eye = (rect.centerx + eye_offset, eye_y)

    if profile["eye_shape"] == "round":
        pygame.draw.circle(surface, profile["eye_color"], left_eye, eye_radius)
        pygame.draw.circle(surface, profile["eye_color"], right_eye, eye_radius)
    else:  # vampire slit eyes
        pygame.draw.ellipse(surface, profile["eye_color"], pygame.Rect(left_eye[0]-6, left_eye[1]-4, 12, 8))
        pygame.draw.ellipse(surface, profile["eye_color"], pygame.Rect(right_eye[0]-6, right_eye[1]-4, 12, 8))

    # Pupils
    pygame.draw.circle(surface, profile["pupil_color"], left_eye, 3)
    pygame.draw.circle(surface, profile["pupil_color"], right_eye, 3)

    # Mouth
    mouth_y = rect.bottom - 20
    if profile["has_fangs"]:
        pygame.draw.line(surface, (255, 255, 255), (rect.centerx - 8, mouth_y), (rect.centerx + 8, mouth_y), 2)
        pygame.draw.line(surface, (255, 255, 255), (rect.centerx - 3, mouth_y), (rect.centerx - 3, mouth_y + 8), 1)
        pygame.draw.line(surface, (255, 255, 255), (rect.centerx + 3, mouth_y), (rect.centerx + 3, mouth_y + 8), 1)
    else:
        pygame.draw.line(surface, (200, 0, 0), (rect.centerx - 8, mouth_y), (rect.centerx + 8, mouth_y), 2)

    # Eyebrows (adds expression)
    brow_y = eye_y - 10
    pygame.draw.line(surface, (0, 0, 0), (left_eye[0] - 6, brow_y), (left_eye[0] + 6, brow_y - 2), 2)
    pygame.draw.line(surface, (0, 0, 0), (right_eye[0] - 6, brow_y - 2), (right_eye[0] + 6, brow_y), 2)

clock = pygame.time.Clock()

while True:
    screen.fill((30, 30, 30))  # Background

    # Draw door
    pygame.draw.rect(screen, (139, 69, 19), door_rect)  # Main door
    pygame.draw.rect(screen, (80, 80, 80), window_rect)  # Window

    # Draw face in window
    if stranger_visible:
        draw_stranger_face(screen, window_rect.inflate(-10, -10), stranger_profile)

    # Dialogue box
    pygame.draw.rect(screen, (10, 10, 10), dialogue_box)
    pygame.draw.rect(screen, (255, 255, 255), dialogue_box, 2)
    if knock_active:
        dialogue_text = "There is a knock at the door. Click to respond."
    if dialogue_text:
        text_surface = font.render(dialogue_text, True, (255, 255, 255))
        screen.blit(text_surface, (dialogue_box.x + 20, dialogue_box.y + 30))

    # Ask a Question Button
    question_button = pygame.Rect(300, 560, 200, 30)
    pygame.draw.rect(screen, (60, 60, 60), question_button)
    pygame.draw.rect(screen, (255, 255, 255), question_button, 1)
    button_label = font.render("Ask a Question", True, (255, 255, 255))
    screen.blit(button_label, (question_button.x + 25, question_button.y + 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if door_rect.collidepoint(event.pos) and knock_active:
                knock_active = False
                stranger_visible = True
                dialogue_text = "Stranger: Good evening... may I come in?"
                questions_asked = 0  # reset for new encounter

            elif stranger_visible and question_button.collidepoint(event.pos):
                if questions_asked < max_questions:
                    dialogue_text = "Stranger: " + dialogue_responses[questions_asked]
                    questions_asked += 1
                else:
                    dialogue_text = "Stranger: I don’t have time for this. Goodbye."
                    stranger_visible = False
                    knock_active = True
                    questions_asked = 0

    pygame.display.flip()
    clock.tick(60)
