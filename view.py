import pygame
"""
This class has been creating to handle all the input() and print() in order to make the readability of the game easier
"""
red_color = (250, 15, 30)


class View:

    def __init__(self):
        self.arial = pygame.font.SysFont("arial", 20, True, False)

    def rules_from_the_game(self):
        self.arial.font.render("Hi! Help McGyver to escape the maze. "
                               "Don't forget to collect all the 3 items before to arrive in front of the Guardian. "
                               "You need them to built a syringue to asleep the Guardian. "
                               "Otherwise you will no be abble to escape and he will kill you! Good luck!", True,
                               red_color)

    def game_over(self):
        self.arial.font.render(" Aouch, you arrived in front of the Guardian without all your items! You are dead!!",
                               True, red_color)

    def win(self):
        self.arial.font.render("Congratulation you saved McGyver!", True, red_color)

    def ask_user_direction(self):
        keyboard = self.arial.font.render("To move McGyver in the maze please use "
                                          "the directions arrow from your keyboard.", True, red_color)
        return keyboard

# Pas d'affichage sauf dans la classe view : from class characters


pygame.init()

window_resolution = (500, 500)
black_color = (0, 0, 0)
blue_color = (90, 124, 250)

pygame.display.set_caption("Maze : McGyver")
screen = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
strike = pygame.image.load("ressource/Gardien.png")
bg = pygame.image.load("ressource/structures.png")
x = 0
y = 0
width = 34
height = 36
velocity = 5
up = False
down = False
left = False
right = False
walkcount = 0
clock = pygame.time.Clock()


def game_window():
    global walkcount

    screen.blit(bg, [0, 0])
    if walkcount + 1 >= 27:
        walkcount = 0
    if up or down or left or right:
        screen.blit(strike, [x, y])
        walkcount += 1
    else:
        walkcount = 0

    pygame.display.update()


run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        if keys[pygame.K_DOWN] and y < 480 - width - velocity:
            y += velocity
        if keys[pygame.K_LEFT] and x > velocity:
            x -= velocity
            left = True
            right = False
        if keys[pygame.K_RIGHT] and x < 640 - width - velocity:
            x += velocity
            left = False
            right = True

    game_window()
