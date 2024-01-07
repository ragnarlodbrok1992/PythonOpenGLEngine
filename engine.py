import pygame
from entities.cube import Cube

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

CLOCK = pygame.time.Clock()
ENGINE_QUIT = False

# HD Resolution
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Cube test object
CUBE = Cube()


def main():
    global ENGINE_QUIT, CLOCK
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Load shaders files
    with open('shaders/vertex_default.glsl') as f:
        VERTEX_SHADER = f.read()
    with open('shaders/fragment_default.glsl') as f:
        FRAGMENT_SHADER = f.read()

    print(f"Vertex shader:\n{VERTEX_SHADER}")
    print(f"Fragment shader:\n{FRAGMENT_SHADER}")

    while not ENGINE_QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ENGINE_QUIT = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ENGINE_QUIT = True

        screen.fill((255, 255, 255))

        pygame.display.flip()

        # Cap the framerate at 60 FPS
        CLOCK.tick(60)

    # Ending the engine
    pygame.quit()


if __name__ == '__main__':
    main()
