import pygame


#varialbles
HEIGHT = 400
WIDTH = 600
BORDER = 5
BORDER_COLOUR = pygame.Color("white")
CIRCLE_COLOUR = pygame.Color("pink")
BG_COLOUR = pygame.Color("black")
clock = pygame.time.Clock()
FRAMERATE = 100
#initialize screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Draw Border
pygame.draw.line(screen, BORDER_COLOUR, (0, 0), (WIDTH, 0), BORDER)
pygame.draw.line(screen, BORDER_COLOUR, (0, 0), (0, HEIGHT), BORDER)
pygame.draw.line(screen, BORDER_COLOUR, (0, HEIGHT), (WIDTH, HEIGHT), BORDER)


#BALL
class Ball:
    RADIUS = 10
    VELOCITY_X = 0
    VELOCITY_Y = 0
    def __init__(self, x, y):
        self.x = x - self.RADIUS
        self.y = y

    def draw(self, color = CIRCLE_COLOUR):
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)

    def move(self):
        self.draw(BG_COLOUR)
        # if BORDER >= self.x + (2 * (self.RADIUS)):
        if BORDER < self.x - (self.RADIUS) and BORDER < self.y - (self.RADIUS) and HEIGHT-BORDER > self.y + (self.RADIUS):
            self.VELOCITY_X = -1
            self.VELOCITY_Y = 1

        else:
            self.VELOCITY_X = 0
            self.VELOCITY_Y = 0

        self.x += self.VELOCITY_X
        self.y += self.VELOCITY_Y

        self.draw()

ball = Ball(WIDTH, HEIGHT//2)

while True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(FRAMERATE)
    ball.move()
    pygame.display.flip()
