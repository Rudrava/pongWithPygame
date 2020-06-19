import pygame


#varialbles
HEIGHT = 600
WIDTH = 800
BORDER = 5
BORDER_COLOUR = pygame.Color("white")
CIRCLE_COLOUR = pygame.Color("pink")
PADDLE_COLOUR = pygame.Color("Red")
BG_COLOUR = pygame.Color("black")
clock = pygame.time.Clock()
FRAMERATE = 200
RUN = True
PADDLEWIDTH = 20
PADDLEHEIGHT = 80



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
    VELOCITY_X = -1
    VELOCITY_Y = 1
    OFFSET_X = PADDLEWIDTH + RADIUS


    def __init__(self, x, y):
        self.x = (x - self.RADIUS) - self.OFFSET_X
        self.y = y
        # print("Starts at : ",self.x)


    def draw(self, color = CIRCLE_COLOUR):
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)

    def move(self):
        self.draw(BG_COLOUR)
        # if BORDER >= self.x + (2 * (self.RADIUS)):
        self.x += self.VELOCITY_X
        self.y += self.VELOCITY_Y
        if self.x <= self.RADIUS + BORDER:
            self.VELOCITY_X = 1
        if self.y <= self.RADIUS + BORDER:
            self.VELOCITY_Y = 1
        if self.y > HEIGHT - (self.RADIUS + BORDER) :
            self.VELOCITY_Y = -1
        # print(self.x)
        self.draw()

    def outOfBounds(self):
        if self.x > WIDTH + self.RADIUS:
            return True
        return False

# PADDLE
class Paddle:
    paddleWidth = PADDLEWIDTH
    paddleHeight = PADDLEHEIGHT
    paddleVelocity = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y//2

    def draw(self, color = PADDLE_COLOUR):
        pygame.draw.line(screen, color, ((self.x - self.paddleWidth),(self.y - self.paddleHeight//2)) , ((self.x - self.paddleWidth),(self.y + self.paddleHeight//2)), self.paddleWidth)

    def move(self, event):
        self.draw(BG_COLOUR)
        print("y: ",self.y," x :",self.x)
        if event == pygame.K_UP and (self.y > (self.paddleHeight // 2 + BORDER)):
            self.y -= self.paddleVelocity
        elif event == pygame.K_DOWN and ((self.y + self.paddleHeight//2) + BORDER < HEIGHT):
            self.y += self.paddleVelocity
        else:
            print("Limit Reached")
        self.draw()


paddle = Paddle(WIDTH, HEIGHT)
ball = Ball(WIDTH, HEIGHT//2)
paddle.draw()

def contact():
    if ball.y > (paddle.y - PADDLEHEIGHT // 2) and ball.y < (paddle.y + PADDLEHEIGHT // 2) and ball.x > (WIDTH - ball.OFFSET_X - ball.RADIUS):

        ball.VELOCITY_X = -1

while RUN:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(FRAMERATE)
    if event.type == pygame.KEYDOWN:
        paddle.move(event.key)
    if ball.outOfBounds():
        print("You Loose!!!")
        RUN = False
    else:
        contact()
        ball.move()

    pygame.display.flip()

pygame.quit()
