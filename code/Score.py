import pygame


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, menu_return: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass
