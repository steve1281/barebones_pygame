import logging
import os
import pygame

from game.rgb import DARK_SLATE_GRAY, BLUE, RED, WHITE


class Game:
    def __init__(self, width=900, height=500, caption="-- Provide a Caption --"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.image = pygame.image.load(os.path.dirname(__file__) + "/resources/pygame-head-party.png")
        self.myfont = pygame.font.SysFont("monospace", 18, bold=True)

    def run(self):
        logging.info("Starting")
        clock = pygame.time.Clock()
        running = True
        screen = self.screen
        myfont = self.myfont

        screen.fill(DARK_SLATE_GRAY)
        while running:
            for event in pygame.event.get():
                # check for window close exit
                if event.type == pygame.QUIT:
                    running = False
                if event.type==pygame.KEYDOWN:
                    # check for ESC key press, and exit
                    if event.key == pygame.K_ESCAPE:
                        running = False
            # draw stuff here.
            # image
            rect = self.image.get_rect()
            rect.center = (140, 120)
            screen.blit(self.image, rect)
            # circle
            pygame.draw.circle(screen, BLUE, (140, 120), 100, 5)
            # line
            pygame.draw.line(screen, RED, (20,120), (260,120))
            pygame.draw.line(screen, RED, (140,0), (140,240))
            # text
            label = myfont.render("Target: Pygame!", 1, WHITE)
            screen.blit(label, (50,300))
            # and update. 
            pygame.display.flip()
            clock.tick(60)

        logging.info("Finishing")
        pygame.quit()
