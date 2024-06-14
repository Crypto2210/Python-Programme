import pygame
import random
import math
import time


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Purple hunter")
        self.logo_img = pygame.image.load("Purple hunter Bilder/Purple hunter-logo.ico")
        pygame.display.set_icon(self.logo_img)
        self.clock = pygame.time.Clock()
        self.hunter = Hunter(self, 350, 704.7)
        self.korbs = RedBall(self)
        self.greenkorbs = GreenBall(self)
        self.score = 0
        self.run = True
        self.shot = True

        while self.run:
            self.clock.tick(360)
            self.screen.fill((0, 0, 0))
            if self.hunter.y == 704.7:
                self.shot = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.shot is True:
                        self.hunter.move(-2.4)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.shot = False

            self.hunter.draw()
            self.korbs.draw()
            self.korbs.draw2()
            self.korbs.draw3()
            self.korbs.draw4()
            self.korbs.draw5()
            self.greenkorbs.draw_green_ball()
            self.hunter.collision()
            self.print_score()
            self.hunter.red_ball_collision()
            pygame.display.update()

    def print_score(self):
        score_font = pygame.font.SysFont("vereda", 30)
        score_text = score_font.render("Punkte: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (8, 8))

    def game_over(self):
        over_font = pygame.font.SysFont("vereda", 150)
        over_text = over_font.render("Game over", True, (255, 255, 255))
        self.screen.blit(over_text, (270, 320))


class Hunter:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.Game = game
        self.bullet_img = pygame.image.load("Purple hunter Bilder/Purple hunter-hunter.png")
        self.change_y = 0
        self.change_x = 3
        self.value1 = 3
        self.value2 = -3
        self.movement = True

    def collision(self):
        distance = math.sqrt(math.pow(self.x - self.Game.greenkorbs.xg, 2)
                             + math.pow(self.y - self.Game.greenkorbs.yg, 2))
        if distance < 55:
            self.Game.score += 1
            self.y = 704.7
            self.change_y = False
            self.value1 += 0.2
            self.value2 -= 0.2
            self.Game.korbs.x = random.randint(0, 140)
            self.Game.korbs.y = random.randint(10, 20)
            self.Game.korbs.x2 = random.randint(200, 440)
            self.Game.korbs.y2 = random.randint(10, 20)
            self.Game.korbs.x3 = random.randint(510, 650)
            self.Game.korbs.y3 = random.randint(10, 20)
            self.Game.korbs.x4 = random.randint(710, 850)
            self.Game.korbs.y4 = random.randint(10, 20)
            self.Game.korbs.x5 = random.randint(890, 930)
            self.Game.korbs.y5 = random.randint(10, 20)
            listex = self.Game.korbs.x, self.Game.korbs.x2, self.Game.korbs.x3, self.Game.korbs.x4, self.Game.korbs.x5
            listey = self.Game.korbs.y, self.Game.korbs.y2, self.Game.korbs.y3, self.Game.korbs.y4, self.Game.korbs.y5
            self.Game.greenkorbs.xg = random.choice(listex)
            self.Game.greenkorbs.yg = random.choice(listey)

    def red_ball_collision(self):
        distance1 = math.sqrt(math.pow(self.x - self.Game.korbs.x, 2) + math.pow(self.y - self.Game.korbs.y, 2))
        distance2 = math.sqrt(math.pow(self.x - self.Game.korbs.x2, 2) + math.pow(self.y - self.Game.korbs.y2, 2))
        distance3 = math.sqrt(math.pow(self.x - self.Game.korbs.x3, 2) + math.pow(self.y - self.Game.korbs.y3, 2))
        distance4 = math.sqrt(math.pow(self.x - self.Game.korbs.x4, 2) + math.pow(self.y - self.Game.korbs.y4, 2))
        distance5 = math.sqrt(math.pow(self.x - self.Game.korbs.x5, 2) + math.pow(self.y - self.Game.korbs.y5, 2))

        if distance1 < 45:
            self.Game.screen.fill((0, 0, 0))
            self.Game.game_over()
            time.sleep(0.1)
            self.Game.score = 0
            self.value2 = -3
            self.value1 = 3

        if distance2 < 45:
            self.Game.screen.fill((0, 0, 0))
            self.Game.game_over()
            time.sleep(0.1)
            self.Game.score = 0
            self.value2 = -3
            self.value1 = 3

        if distance3 < 45:
            self.Game.screen.fill((0, 0, 0))
            self.Game.game_over()
            time.sleep(0.1)
            self.Game.score = 0
            self.value2 = -3
            self.value1 = 3

        if distance4 < 45:
            self.Game.screen.fill((0, 0, 0))
            self.Game.game_over()
            time.sleep(0.1)
            self.Game.score = 0
            self.value2 = -3
            self.value1 = 3

        if distance5 < 45:
            self.Game.screen.fill((0, 0, 0))
            self.Game.game_over()
            time.sleep(0.1)
            self.Game.score = 0
            self.value2 = -3
            self.value1 = 3

    def move(self, speed):
        self.change_y += speed

    def draw(self):
        self.y += self.change_y
        if self.movement:
            self.x += self.change_x
        if self.y < 0:
            self.y = 704.7
            self.Game.shot = False
            self.change_y = 0
        if self.x > 1050:
            self.change_x = self.value2
        if self.x < -31:
            self.change_x = self.value1
        if self.y < 704.7:
            self.movement = False
        if self.y == 704.7:
            self.movement = True
        self.Game.screen.blit(self.bullet_img, (self.x, self.y))


class RedBall:
    def __init__(self, game):
        self.Game = game
        self.x = random.randint(0, 140)
        self.y = random.randint(10, 20)
        self.x2 = random.randint(200, 440)
        self.y2 = random.randint(10, 20)
        self.x3 = random.randint(510, 650)
        self.y3 = random.randint(10, 20)
        self.x4 = random.randint(710, 850)
        self.y4 = random.randint(10, 20)
        self.x5 = random.randint(950, 1020)
        self.y5 = random.randint(10, 20)
        self.korbs_img = pygame.image.load("Purple hunter Bilder/Purple hunter-red ball.png")

    def draw(self):
        self.Game.screen.blit(self.korbs_img, (self.x, self.y))

    def draw2(self):
        self.Game.screen.blit(self.korbs_img, (self.x2, self.y2))

    def draw3(self):
        self.Game.screen.blit(self.korbs_img, (self.x3, self.y3))

    def draw4(self):
        self.Game.screen.blit(self.korbs_img, (self.x4, self.y4))

    def draw5(self):
        self.Game.screen.blit(self.korbs_img, (self.x5, self.y5))


class GreenBall:
    def __init__(self, game):
        self.Game = game
        self.lists = self.Game.korbs.x, self.Game.korbs.x2, self.Game.korbs.x3, self.Game.korbs.x4, self.Game.korbs.x5
        self.lists2 = self.Game.korbs.y, self.Game.korbs.y2, self.Game.korbs.y3, self.Game.korbs.y4, self.Game.korbs.y5
        self.xg = random.choice(self.lists)
        self.yg = random.choice(self.lists2)
        self.greenkorbs_img = pygame.image.load("Purple hunter Bilder/Purple hunter-green ball.png")

    def draw_green_ball(self):
        self.Game.screen.blit(self.greenkorbs_img, (self.xg, self.yg))


if __name__ == "__main__":
    Game = Game(1100, 800)
