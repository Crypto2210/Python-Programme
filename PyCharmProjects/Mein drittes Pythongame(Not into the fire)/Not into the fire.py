import random
import math
import pygame


class Game:
    def __init__(self, width, heigth):
        pygame.init()
        self.width = width
        self.heigth = heigth
        self.screen = pygame.display.set_mode((self.width, self.heigth))
        pygame.display.set_caption("Not into the fire")
        self.logo_img = pygame.image.load("Not into the fire Bilder/Not into the fire-logo.ico")
        pygame.display.set_icon(self.logo_img)
        self.player = Player(self)
        self.jatpack = Jatpack(self)
        self.fps = pygame.time.Clock()
        self.run = True
        self.idee = True
        self.live = 5
        self.fire = Fire(self)
        self.death = False
        self.points = Points(self)
        self.Points = 0
        while self.run:
            self.fps.tick(360)
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.player.idee2 is False:
                            self.player.change_y = -0.35
                            self.idee = False

                    if event.key == pygame.K_LEFT:
                        self.player.move(-0.35)

                    if event.key == pygame.K_RIGHT:
                        self.player.move(0.35)

                    if event.key == pygame.K_RETURN:
                        self.death = False
                        self.live = 5
                        self.fire.x1 = 900
                        self.fire.x2 = 900
                        self.fire.x3 = 900
                        self.fire.x4 = 900
                        self.fire.x5 = 1400
                        self.fire.x6 = 1400
                        self.fire.x7 = 1400
                        self.fire.x8 = 1400
                        self.player.x = 70
                        self.player.y = 300
                        self.player.x2 = 70
                        self.player.y2 = 340
                        self.jatpack.x = 66
                        self.jatpack.y = 350
                        self.fire.change_x1_and_3_and_5_and_7 = random.uniform(-0.7, -1.6)
                        self.fire.change_x2_and_4_and_6_8 = random.uniform(-0.7, -1.6)
                        self.fire.y1 = random.randint(0, 100)
                        self.fire.y2 = random.randint(150, 300)
                        self.fire.y3 = random.randint(350, 500)
                        self.fire.y4 = random.randint(550, 600)
                        self.fire.y5 = random.randint(50, 150)
                        self.fire.y6 = random.randint(200, 300)
                        self.fire.y7 = random.randint(350, 450)
                        self.fire.y8 = random.randint(500, 600)
                        self.points.x1 = random.randint(1600, 3000)
                        self.points.x2 = random.randint(1600, 3000)
                        self.points.x3 = random.randint(1600, 3000)
                        self.points.x4 = random.randint(1600, 3000)
                        self.points.y1 = random.randint(0, 150)
                        self.points.y2 = random.randint(200, 350)
                        self.points.y3 = random.randint(400, 550)
                        self.points.y4 = random.randint(600, 700)
                        self.Points = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.player.idee2 = False
                        self.player.change_y = 0.35
                        self.idee = True

                    if event.key == pygame.K_LEFT:
                        self.player.move(0.35)

                    if event.key == pygame.K_RIGHT:
                        self.player.move(-0.35)

            self.player.draw()

            if self.idee is False:
                self.jatpack.draw()

            self.fire.draw()
            self.player.collision()
            self.print_live()
            self.points.draw_points()
            self.print_points()
            if self.death is True:
                self.screen.fill((0, 0, 0))
                self.game_over()

            pygame.display.update()

    def print_live(self):
        go_font = pygame.font.SysFont("freesansbold.ttf", 25)
        go_text = go_font.render("Leben: " + str(self.live), True, (255, 255, 255))
        self.screen.blit(go_text, (700, 8))

    def print_points(self):
        go_font = pygame.font.SysFont("vereda", 25)
        go_text = go_font.render("POINTS: " + str(self.Points), True, (255, 255, 255))
        self.screen.blit(go_text, (20, 8))

    def game_over(self):
        go_font = pygame.font.SysFont("vereda", 100)
        go_text = go_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(go_text, (185, 290))


class Player:
    def __init__(self, game):
        self.distance_points8 = None
        self.distance_points7 = None
        self.distance_points6 = None
        self.distance_points5 = None
        self.distance16 = None
        self.distance15 = None
        self.distance14 = None
        self.distance13 = None
        self.distance12 = None
        self.distance11 = None
        self.distance10 = None
        self.distance9 = None
        self.distance_points4 = None
        self.distance_points3 = None
        self.distance_points2 = None
        self.distance_points1 = None
        self.distance8 = None
        self.distance7 = None
        self.distance6 = None
        self.distance5 = None
        self.distance4 = None
        self.distance3 = None
        self.distance2 = None
        self.distance1 = None
        self.Game = game
        self.x = 70
        self.y = 300
        self.y2 = 360
        self.range = 25
        self.wenn = True
        self.player_img = pygame.image.load("Not into the fire Bilder/Not into the fire-player.png")
        self.pixel_img = pygame.image.load("Not into the fire Bilder/Not into the fire-pixel.png")
        self.idee2 = False
        if self.idee2 is False:
            self.change_y = 0.35
        self.change_x = 0

    def collision(self):
        if self.wenn is True:
            self.distance1 = math.sqrt(
                math.pow(self.x - self.Game.fire.x1, 2) + math.pow(self.y - self.Game.fire.y1, 2))
            self.distance2 = math.sqrt(
                math.pow(self.x - self.Game.fire.x2, 2) + math.pow(self.y - self.Game.fire.y2, 2))
            self.distance3 = math.sqrt(
                math.pow(self.x - self.Game.fire.x3, 2) + math.pow(self.y - self.Game.fire.y3, 2))
            self.distance4 = math.sqrt(
                math.pow(self.x - self.Game.fire.x4, 2) + math.pow(self.y - self.Game.fire.y4, 2))
            self.distance5 = math.sqrt(
                math.pow(self.x - self.Game.fire.x5, 2) + math.pow(self.y - self.Game.fire.y5, 2))
            self.distance6 = math.sqrt(
                math.pow(self.x - self.Game.fire.x6, 2) + math.pow(self.y - self.Game.fire.y6, 2))
            self.distance7 = math.sqrt(
                math.pow(self.x - self.Game.fire.x7, 2) + math.pow(self.y - self.Game.fire.y7, 2))
            self.distance8 = math.sqrt(
                math.pow(self.x - self.Game.fire.x8, 2) + math.pow(self.y - self.Game.fire.y8, 2))
            self.distance_points1 = math.sqrt(
                math.pow(self.x - self.Game.points.x1, 2) + math.pow(self.y - self.Game.points.y1, 2))
            self.distance_points2 = math.sqrt(
                math.pow(self.x - self.Game.points.x2, 2) + math.pow(self.y - self.Game.points.y2, 2))
            self.distance_points3 = math.sqrt(
                math.pow(self.x - self.Game.points.x3, 2) + math.pow(self.y - self.Game.points.y3, 2))
            self.distance_points4 = math.sqrt(
                math.pow(self.x - self.Game.points.x4, 2) + math.pow(self.y - self.Game.points.y4, 2))
            self.distance9 = math.sqrt(
                math.pow(self.x - self.Game.fire.x1, 2) + math.pow(self.y2 - self.Game.fire.y1, 2))
            self.distance10 = math.sqrt(
                math.pow(self.x - self.Game.fire.x2, 2) + math.pow(self.y2 - self.Game.fire.y2, 2))
            self.distance11 = math.sqrt(
                math.pow(self.x - self.Game.fire.x3, 2) + math.pow(self.y2 - self.Game.fire.y3, 2))
            self.distance12 = math.sqrt(
                math.pow(self.x - self.Game.fire.x4, 2) + math.pow(self.y2 - self.Game.fire.y4, 2))
            self.distance13 = math.sqrt(
                math.pow(self.x - self.Game.fire.x5, 2) + math.pow(self.y2 - self.Game.fire.y5, 2))
            self.distance14 = math.sqrt(
                math.pow(self.x - self.Game.fire.x6, 2) + math.pow(self.y2 - self.Game.fire.y6, 2))
            self.distance15 = math.sqrt(
                math.pow(self.x - self.Game.fire.x7, 2) + math.pow(self.y2 - self.Game.fire.y7, 2))
            self.distance16 = math.sqrt(
                math.pow(self.x - self.Game.fire.x8, 2) + math.pow(self.y2 - self.Game.fire.y8, 2))
            self.distance_points5 = math.sqrt(
                math.pow(self.x - self.Game.points.x1, 2) + math.pow(self.y2 - self.Game.points.y1, 2))
            self.distance_points6 = math.sqrt(
                math.pow(self.x - self.Game.points.x2, 2) + math.pow(self.y2 - self.Game.points.y2, 2))
            self.distance_points7 = math.sqrt(
                math.pow(self.x - self.Game.points.x3, 2) + math.pow(self.y2 - self.Game.points.y3, 2))
            self.distance_points8 = math.sqrt(
                math.pow(self.x - self.Game.points.x4, 2) + math.pow(self.y2 - self.Game.points.y4, 2))

        if (self.distance1 < self.range or self.distance2 < self.range or self.distance3 < self.range or
                self.distance4 < self.range or self.distance5 < self.range or self.distance6 < self.range or
                self.distance7 < self.range or self.distance8 < self.range or self.distance9 < self.range or
                self.distance10 < self.range or self.distance11 < self.range or
                self.distance12 < self.range or self.distance13 < self.range or self.distance14 < self.range or
                self.distance15 < self.range or self.distance16 < self.range):
            self.Game.live -= 1
            self.weniger_leben()

        if self.distance_points1 < 30:
            self.Game.Points += 1
            self.Game.points.x1 = random.randint(1600, 3000)
            self.Game.points.y1 = random.randint(0, 150)

        if self.distance_points2 < 45:
            self.Game.Points += 1
            self.Game.points.x2 = random.randint(1600, 3000)
            self.Game.points.y2 = random.randint(200, 350)

        if self.distance_points3 < 45:
            self.Game.Points += 1
            self.Game.points.x3 = random.randint(1600, 3000)
            self.Game.points.y3 = random.randint(400, 550)

        if self.distance_points4 < 45:
            self.Game.Points += 1
            self.Game.points.x4 = random.randint(1600, 3000)
            self.Game.points.y4 = random.randint(600, 700)

        if self.Game.live < 1:
            self.Game.death = True

    def weniger_leben(self):
        self.black_screen()
        self.Game.fire.x1 = 900
        self.Game.fire.x2 = 900
        self.Game.fire.x3 = 900
        self.Game.fire.x4 = 900
        self.Game.fire.x5 = 1400
        self.Game.fire.x6 = 1400
        self.Game.fire.x7 = 1400
        self.Game.fire.x8 = 1400
        self.x = 70
        self.y = 300
        self.y2 = 340
        self.Game.jatpack.x = 66
        self.Game.jatpack.y = 350
        self.Game.fire.change_x1_and_3_and_5_and_7 = random.uniform(-0.7, -1.6)
        self.Game.fire.change_x2_and_4_and_6_8 = random.uniform(-0.7, -1.6)
        self.Game.fire.y1 = random.randint(0, 100)
        self.Game.fire.y2 = random.randint(150, 300)
        self.Game.fire.y3 = random.randint(350, 500)
        self.Game.fire.y4 = random.randint(550, 600)
        self.Game.fire.y5 = random.randint(50, 150)
        self.Game.fire.y6 = random.randint(200, 300)
        self.Game.fire.y7 = random.randint(350, 450)
        self.Game.fire.y8 = random.randint(500, 600)
        self.Game.points.x1 = random.randint(1600, 3000)
        self.Game.points.x2 = random.randint(1600, 3000)
        self.Game.points.x3 = random.randint(1600, 3000)
        self.Game.points.x4 = random.randint(1600, 3000)
        self.Game.points.y1 = random.randint(0, 150)
        self.Game.points.y2 = random.randint(200, 350)
        self.Game.points.y3 = random.randint(400, 550)
        self.Game.points.y4 = random.randint(600, 700)

    def black_screen(self):
        self.Game.screen.fill((0, 0, 0))

    def move(self, speed):
        self.change_x += speed

    def draw(self):
        self.y += self.change_y
        self.x += self.change_x
        self.x += self.change_x
        self.y2 += self.change_y
        if self.y > 600:
            self.y = 600
            self.y2 = 640

        if self.y < 0:
            self.y = 0
            self.y2 = 40

        if self.x > 730:
            self.x = 730

        if self.x < 0:
            self.x = 0

        self.Game.screen.blit(self.player_img, (self.x, self.y))
        self.Game.screen.blit(self.pixel_img, (self.x, self.y2))


class Jatpack:
    def __init__(self, game):
        self.Game = game
        self.x = 66
        self.y = 350
        self.jatpack_img = pygame.image.load("Not into the fire Bilder/Not into the fire-jatpack.png")
        self.jatpack_img1 = pygame.image.load("Not into the fire Bilder/Not into the fire-jatpack2.png")

    def draw(self):
        self.x = self.Game.player.x - 4
        self.y = self.Game.player.y + 50

        if self.y < 50:
            self.y = 50

        if self.y > 650:
            self.y = 650

        if self.x > 730:
            self.x = 730

        if self.x < 0:
            self.x = 0
        self.Game.screen.blit(self.jatpack_img, (self.x, self.y))


class Fire:
    def __init__(self, game):
        self.Game = game
        self.x1 = 900
        self.x2 = 900
        self.x3 = 900
        self.x4 = 900
        self.x5 = 1400
        self.x6 = 1400
        self.x7 = 1400
        self.x8 = 1400
        self.y1 = random.randint(0, 100)
        self.y2 = random.randint(150, 300)
        self.y3 = random.randint(350, 500)
        self.y4 = random.randint(550, 600)
        self.y5 = random.randint(50, 150)
        self.y6 = random.randint(200, 300)
        self.y7 = random.randint(350, 450)
        self.y8 = random.randint(500, 600)
        self.fire_img = pygame.image.load("Not into the fire Bilder/Not into the fire-fire.png")
        self.change_x1_and_3_and_5_and_7 = random.uniform(-0.7, -1.6)
        self.change_x2_and_4_and_6_8 = random.uniform(-0.7, -1.6)

    def draw(self):
        self.x1 += self.change_x1_and_3_and_5_and_7
        self.x2 += self.change_x2_and_4_and_6_8
        self.x3 += self.change_x1_and_3_and_5_and_7
        self.x4 += self.change_x2_and_4_and_6_8
        self.x5 += self.change_x1_and_3_and_5_and_7
        self.x6 += self.change_x2_and_4_and_6_8
        self.x7 += self.change_x1_and_3_and_5_and_7
        self.x8 += self.change_x2_and_4_and_6_8
        if self.x1 and self.x3 < 0:
            self.x1 = 900
            self.x3 = 900
            self.y1 = random.randint(0, 100)
            self.y3 = random.randint(350, 500)

        if self.x2 and self.x4 < 0:
            self.x2 = 900
            self.x4 = 900
            self.y2 = random.randint(150, 300)
            self.y4 = self.y4 = random.randint(550, 600)

        if self.x5 and self.x7 < 0:
            self.x5 = 1400
            self.x7 = 1400
            self.y5 = random.randint(0, 100)
            self.y7 = random.randint(350, 500)

        if self.x6 and self.x8 < 0:
            self.x6 = 1400
            self.x8 = 1400
            self.y6 = random.randint(150, 300)
            self.y8 = random.randint(550, 600)

        self.Game.screen.blit(self.fire_img, (self.x1, self.y1))
        self.Game.screen.blit(self.fire_img, (self.x2, self.y2))
        self.Game.screen.blit(self.fire_img, (self.x3, self.y3))
        self.Game.screen.blit(self.fire_img, (self.x4, self.y4))
        self.Game.screen.blit(self.fire_img, (self.x5, self.y5))
        self.Game.screen.blit(self.fire_img, (self.x6, self.y6))
        self.Game.screen.blit(self.fire_img, (self.x7, self.y7))
        self.Game.screen.blit(self.fire_img, (self.x8, self.y8))


class Points:
    def __init__(self, game):
        self.Game = game
        self.x1 = random.randint(1600, 3000)
        self.x2 = random.randint(1600, 3000)
        self.x3 = random.randint(1600, 3000)
        self.x4 = random.randint(1600, 3000)
        self.y1 = random.randint(0, 150)
        self.y2 = random.randint(200, 350)
        self.y3 = random.randint(400, 550)
        self.y4 = random.randint(600, 700)
        self.points_img = pygame.image.load("Not into the fire Bilder/Not into the fire-points.png")
        self.change_x = -1

    def draw_points(self):
        self.x1 += self.change_x
        self.x2 += self.change_x
        self.x3 += self.change_x
        self.x4 += self.change_x
        if self.x1 < 0:
            self.x1 = random.randint(1600, 3000)

        if self.x2 < 0:
            self.x2 = random.randint(1600, 3000)

        if self.x3 < 0:
            self.x3 = random.randint(1600, 3000)

        if self.x4 < 0:
            self.x4 = random.randint(1600, 3000)

        self.Game.screen.blit(self.points_img, (self.x1, self.y1))
        self.Game.screen.blit(self.points_img, (self.x2, self.y2))
        self.Game.screen.blit(self.points_img, (self.x3, self.y3))
        self.Game.screen.blit(self.points_img, (self.x4, self.y4))


if __name__ == "__main__":
    Game = Game(800, 700)
