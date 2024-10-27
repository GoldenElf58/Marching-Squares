import sys

import pygame

from grid import Grid


def main():
    show_fps = False
    scale = 10
    smooth = True
    resolution = 7  # Lower resolution value is more fine
    screen_width, screen_height = 1024, 1024
    animate = False
    debug = True

    pygame.init()
    pygame.font.init()
    
    font: pygame.font.Font = pygame.font.Font(None, 32)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Marching Squares")
    clock: pygame.time.Clock = pygame.time.Clock()
    
    grid: Grid = Grid(screen_width // resolution, screen_height // resolution, screen, font=font, smooth=smooth,
                      scale=scale, debug=debug)
    
    z = 0
    while True:
        if animate:
            dt = clock.tick(60) / 1000
            z += dt * .5
        else:
            clock.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                show_fps = not show_fps
        screen.fill((0, 0, 0))
        
        grid.set_corners(z)
        grid.draw()
        
        if show_fps:
            text = font.render(str(round(1 / dt)), True, (255, 255, 255))
            screen.blit(text, (0, 0))
        
        pygame.display.flip()
        # if (r := 1/dt) < 20:
        #     print(r)


if __name__ == "__main__":
    main()
