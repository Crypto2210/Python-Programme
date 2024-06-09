import pygame
import random
import math


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ping Pong")
        self.run = True
        self.clock = pygame.time.Clock()
        self.ball = Ball(self)
        self.schlager = Schlager(self)
        self.count = 0
        while self.run:
            self.clock.tick(360)
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.schlager.move(-1)
                    if event.key == pygame.K_RIGHT:
                        self.schlager.move(1)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.schlager.move(1)
                    if event.key == pygame.K_RIGHT:
                        self.schlager.move(-1)

            self.schlager.update()
            self.schlager.rules()
            self.schlager.draw()
            self.ball.draw()
            self.schlager.collision()
            pygame.display.update()

    def game_over(self):
        over_font = pygame.font.SysFont("vereda", 100)
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(over_text, (235, 300))

    def winner(self):
        win_font = pygame.font.SysFont("vereda", 100)
        win_text = win_font.render("WINNER", True, (255, 255, 255))
        self.screen.blit(win_text, (310, 310))


class Schlager:
    def __init__(self, game):
        self.Game = game
        self.x1 = 400
        self.x2 = 400
        self.y1 = -66
        self.y2 = 600
        self.x2_left_corner = self.x2 - 40
        self.y2_left_corner = 620
        self.x2_left_mittle = self.x2 - 30
        self.y2_left_mittle = 600
        self.x2_mittle = self.x2 - 12
        self.y2_mittle = 600
        self.x2_rigth_mittle = self.x2 + 25
        self.y2_rigth_mittle = 600
        self.x2_rigth_corner = self.x2 + 50
        self.y2_rigth_corner = 620
        self.x1_left_corner = self.x1 - 45
        self.y1_left_corner = -33
        self.x1_left_mittle = self.x1 - 30
        self.y1_left_mittle = -28
        self.x1_mittle = self.x1 - 12
        self.y1_mittle = -28
        self.x1_rigth_mittle = self.x1 + 10
        self.y1_rigth_mittle = -28
        self.x1_rigth_corner = self.x1 + 50
        self.y1_rigth_corner = -33
        self.change_x1 = 0
        self.change_x2 = 0
        self.schlager_img = pygame.image.load("Ping Pong Bilder/Ping Pong-bet.png")
        self.left_schlager_img = pygame.image.load("Ping Pong Bilder/Ping Pong-pixel.png")
        self.score = 0

    def update(self):
        self.x2_left_corner = self.x2 - 45
        self.x2_left_mittle = self.x2 - 30
        self.x2_mittle = self.x2 - 12
        self.x2_rigth_corner = self.x2 + 50
        self.x2_rigth_mittle = self.x2 + 25
        self.x1_left_corner = self.x1 - 45
        self.x1_left_mittle = self.x1 - 30
        self.x1_mittle = self.x1 - 12
        self.x1_rigth_corner = self.x1 + 50
        self.x1_rigth_mittle = self.x1 + 10

    def restart(self):
        self.Game.ball.y = 50
        self.Game.ball.change_y = 1
        self.Game.ball.x = random.randint(60, 700)
        self.Game.ball.change_x = 0
        self.x1 = 400
        self.x2 = 400
        self.update()

    def collision(self):
        distance1 = math.sqrt(
            math.pow(self.x2_left_corner - self.Game.ball.x, 2) + math.pow(self.y2_left_corner - self.Game.ball.y, 2))
        distance2 = math.sqrt(
            math.pow(self.x2_left_mittle - self.Game.ball.x, 2) + math.pow(self.y2_left_mittle - self.Game.ball.y, 2))
        distance3 = math.sqrt(
            math.pow(self.x2_mittle - self.Game.ball.x, 2) + math.pow(self.y2_mittle - self.Game.ball.y, 2))
        distance4 = math.sqrt(
            math.pow(self.x2_rigth_corner - self.Game.ball.x, 2) + math.pow(self.y2_rigth_corner - self.Game.ball.y, 2))
        distance5 = math.sqrt(
            math.pow(self.x2_rigth_mittle - self.Game.ball.x, 2) + math.pow(self.y2_rigth_mittle - self.Game.ball.y, 2))
        distance6 = math.sqrt(
            math.pow(self.x1_left_corner - self.Game.ball.x, 2) + math.pow(self.y1_left_corner - self.Game.ball.y, 2))
        distance7 = math.sqrt(
            math.pow(self.x1_left_mittle - self.Game.ball.x, 2) + math.pow(self.y1_left_mittle - self.Game.ball.y, 2))
        distance8 = math.sqrt(
            math.pow(self.x1_mittle - self.Game.ball.x, 2) + math.pow(self.y1_mittle - self.Game.ball.y, 2))
        distance9 = math.sqrt(
            math.pow(self.x1_rigth_corner - self.Game.ball.x, 2) + math.pow(self.y1_rigth_corner - self.Game.ball.y, 2))
        distance10 = math.sqrt(
            math.pow(self.x1_rigth_mittle - self.Game.ball.x, 2) + math.pow(self.y1_rigth_mittle - self.Game.ball.y, 2))

        if distance1 < 25:
            self.Game.ball.change_y = -1
            self.Game.ball.change_x = -1

        if distance2 < 20:
            self.Game.ball.change_y = -1
            self.Game.ball.change_x = -0.2

        if distance3 < 20:
            self.Game.ball.change_y = -1
            self.Game.ball.change_x = -0.05

        if distance4 < 25:
            self.Game.ball.change_y = -1
            self.Game.ball.change_x = 1

        if distance5 < 20:
            self.Game.ball.change_y = -1
            self.Game.ball.change_x = 0.2

        if distance6 < 25:
            self.Game.ball.change_y = 1
            self.Game.ball.change_x = -1

        if distance7 < 20:
            self.Game.ball.change_y = 1
            self.Game.ball.change_x = -0.2

        if distance8 < 20:
            self.Game.ball.change_y = 1
            self.Game.ball.change_x = -0.05

        if distance9 < 25:
            self.Game.ball.change_y = 1
            self.Game.ball.change_x = 1

        if distance10 < 20:
            self.Game.ball.change_y = 1
            self.Game.ball.change_x = 0.2

        if self.Game.ball.x < -22 and self.Game.ball.change_y == -1:
            self.Game.ball.change_y = -1
            self.Game.ball.change_x = 1

        if self.Game.ball.x < -22 and self.Game.ball.change_y == 1:
            self.Game.ball.change_y = 1
            self.Game.ball.change_x = 1

        if self.Game.ball.x > 840 and self.Game.ball.change_y == -1:
            self.Game.ball.change_y = -1
            self.Game.ball.change_x = -1

        if self.Game.ball.x > 840 and self.Game.ball.change_y == 1:
            self.Game.ball.change_y = 1
            self.Game.ball.change_x = -1

        if self.Game.ball.y > 660:
            self.Game.screen.fill((0, 0, 0))
            self.Game.game_over()

        if self.Game.ball.y > 1700:
            self.restart()

        if self.Game.ball.y < -60:
            self.Game.screen.fill((0, 0, 0))
            self.Game.winner()

        if self.Game.ball.y < -1100:
            self.restart()

    def move(self, speed):
        self.change_x2 += speed

    def rules(self):
        self.x1 += self.change_x1
        self.x2 += self.change_x2

        if self.Game.ball.y < 500 and self.x1_left_corner < self.Game.ball.x and self.Game.ball.x < self.x1_rigth_corner:
            self.change_x1 = 0

        if self.Game.ball.y < 500 and self.x1_rigth_corner < self.Game.ball.x:
            self.change_x1 = 1

        if self.Game.ball.y < 500 and self.x1_left_corner > self.Game.ball.x:
            self.change_x1 = -1

        if self.x1_left_corner == self.Game.ball.x:
            self.change_x1 = 0
        if self.x1_rigth_corner == self.Game.ball.x:
            self.change_x1 = 0

        if (self.x1 > 600 and self.x2 > 600 and self.Game.ball.change_y == -1 and self.Game.ball.change_x == -1 and
                self.Game.ball.y > 597):
            self.change_x1 = -1

        if (self.x1 < 300 and self.x2 < 300 and self.Game.ball.change_y == -1 and self.Game.ball.change_x == 1 and
                self.Game.ball.y > 597):
            self.change_x1 = 1

        if self.x2 < 0:
            self.x2 = 0

        if self.x2 > 800:
            self.x2 = 800

        if self.x1 < 0:
            self.x1 = 0

        if self.x1 > 800:
            self.x1 = 800

    def draw(self):
        self.Game.screen.blit(self.schlager_img, (self.x1, self.y1))
        self.Game.screen.blit(self.schlager_img, (self.x2, self.y2))


class Ball:
    def __init__(self, game):
        self.Game = game
        self.x = random.randint(60, 700)
        self.y = 50
        self.change_y = 1
        self.change_x = 0
        self.ball_img = pygame.image.load("Ping Pong Bilder/Ping Pong-ball.png")

    def draw(self):
        self.y += self.change_y
        self.x += self.change_x
        self.Game.screen.blit(self.ball_img, (self.x, self.y))


if __name__ == "__main__":
    game = Game(900, 700)
