import sys

import pygame

from grid import Grid


def main():
    smooth = True
    animate = True
    show_gradient = False
    show_fps = False
    debug = False
    scale = 5  # Higher scale is more zoomed out
    resolution = 8  # Lower resolution value is more fine
    anim_speed = 0.5  # Higher value is faster
    screen_width, screen_height = 1024, 1024

    pygame.init()
    pygame.font.init()
    
    small_font: pygame.font.Font = pygame.font.Font(None, 12)
    font: pygame.font.Font = pygame.font.Font(None, 32)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Marching Squares")
    clock: pygame.time.Clock = pygame.time.Clock()
    
    grid: Grid = Grid(screen_width // resolution, screen_height // resolution, screen, font=small_font, smooth=smooth,
                      scale=scale, debug=debug, show_gradient=show_gradient)
    
    z = 0
    while True:
        if animate:
            dt = clock.tick(60) / 1000
            z += dt * anim_speed
        else:
            dt = clock.tick(10) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    show_fps = not show_fps
                if event.key == pygame.K_SPACE:
                    smooth = not smooth
                    grid.set_smooth(smooth)
                if event.key == pygame.K_d:
                    debug = not debug
                    grid.set_debug(debug)
                if event.key == pygame.K_a:
                    animate = not animate
                if event.key == pygame.K_UP:
                    anim_speed += 0.1
                    print(f'anim_speed: {anim_speed:.2f}')
                if event.key == pygame.K_DOWN:
                    anim_speed -= 0.1
                    print(f'anim_speed: {anim_speed:.2f}')
                if event.key == pygame.K_g:
                    show_gradient = not show_gradient
                    grid.set_show_gradient(show_gradient)
                if event.key == pygame.K_s:
                    scale += 1
                    print(f'scale: {scale}')
                    grid.set_scale(scale)
                if event.key == pygame.K_w:
                    scale -= 1
                    print(f'scale: {scale}')
                    grid.set_scale(scale)
        
        screen.fill((0, 0, 0))
        
        grid.set_corners(z)
        grid.draw()
        
        if show_fps:
            text = font.render(str(round(1 / dt)), True, (255, 255, 255))
            screen.blit(text, (0, 0))
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
