import pygame
import math


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Basketball")
        self.logo_img = pygame.image.load("Basketball Bilder/Basketball-logo.ico")
        pygame.display.set_icon(self.logo_img)
        self.run = True
        self.clock = pygame.time.Clock()
        self.ball = Ball(self, 360, 690)
        self.korb = Korb(self, 440, 4)
        self.score = 0
        self.throw = True

        while self.run:
            self.clock.tick(360)
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ball.move_key_r_l(-3)
                    if event.key == pygame.K_RIGHT:
                        self.ball.move_key_r_l(3)
                    if event.key == pygame.K_SPACE and self.throw is True:
                        self.ball.move_space(-3)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.ball.move_key_r_l(3)
                    if event.key == pygame.K_RIGHT:
                        self.ball.move_key_r_l(-3)
                    if event.key == pygame.K_SPACE:
                        self.throw = False


            self.ball.draw()
            self.ball.colision()
            self.ball.rules()
            self.korb.draw()
            self.korb.rules()
            self.print_score()
            pygame.display.update()

    def print_score(self):
        score_font = pygame.font.SysFont("vereda", 25)
        score_text = score_font.render("POINTS: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (8, 8))


class Ball:
    def __init__(self, game, x, y):
        self.Game = game
        self.x = x
        self.y = y
        self.ball_img = pygame.image.load("Basketball Bilder/Basketball-ball.png")
        self.change_y = 0
        self.change_x = 0

    def draw(self):
        self.y += self.change_y
        self.x += self.change_x
        self.Game.screen.blit(self.ball_img, (self.x, self.y))

    def move_key_r_l(self, speed):
        self.change_x += speed

    def move_space(self, speed):
        self.change_y += speed

    def colision(self):
        distance = math.sqrt(math.pow(self.x - self.Game.korb.x, 2) + math.pow(self.y - (self.Game.korb.y - 10), 2))
        if distance < 65:
            self.Game.score += 1
            self.Game.korb.speed += 0.05
            self.y = 690
            self.change_y = 0
            self.Game.throw = True

    def rules(self):
        if self.x < 0:
            self.x = 0
        if self.x > 700:
            self.x = 700
        if self.y < 0:
            self.y = 690
            self.change_y = 0
            self.Game.throw = True
        if self.y == 690:
            self.Game.throw = True


class Korb:
    def __init__(self, game, x, y):
        self.Game = game
        self.x = x
        self.y = y
        self.korb_img = pygame.image.load("Basketball Bilder/Basketball-korb.png")
        self.change_x = 2
        self.speed = 0

    def rules(self):
        self.x += self.change_x
        if self.x >= 710:
            self.change_x = -2 + -self.speed
        if self.x < 0:
            self.change_x = 2 + self.speed


    def draw(self):
        self.Game.screen.blit(self.korb_img, (self.x, self.y))


if __name__ == "__main__":
    Game = Game(800, 800)
