import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

CELL = 30

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > WIDTH // CELL - 1:
            self.body[0].x = 0
        # checks the left border
        if self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL - 1:
            self.body[0].y = 0
        # checks the top border
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1


    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            if isinstance(food, SuperFood):
                food.generate_random_pos(self, food)
            else:
                food.generate_random_pos(self)
            return True  # Вернём True, чтобы увеличить счёт
        return False

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            
            # Проверим, что (x, y) не занято телом змейки
            overlap = False
            for segment in snake.body:
                if segment.x == x and segment.y == y:
                    overlap = True
                    break
            
            if not overlap:
                self.pos = Point(x, y)
                break

class SuperFood:
    def __init__(self):
        self.pos = Point(1, 3)
        self.timer = 0
        self.max_time = 60  # Time in frames

    def draw(self):
        # Change color based on remaining time
        remaining_time = self.max_time - self.timer
        if remaining_time > self.max_time // 2:
            color = colorPURPLE
        else:
            color = colorPINK

        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake, food):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            
            # Проверим, что (x, y) не занято телом змейки и не совпадает с позицией обычной еды
            overlap = False
            for segment in snake.body:
                if segment.x == x and segment.y == y:
                    overlap = True
                    break
            if x == food.pos.x and y == food.pos.y:
                overlap = True
            
            if not overlap:
                self.pos = Point(x, y)
                self.timer = 0  # Reset timer when new position is generated
                break

FPS = 5
clock = pygame.time.Clock()

food = Food()
super_food = SuperFood()
snake = Snake()

score = 0          # Счёт
level = 1          # Уровень
score_for_next_level = 3  # каждые 3 очка -> следующий уровень

# шрифт, чтобы выводить счёт и уровень
font = pygame.font.SysFont("Verdana", 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)

    draw_grid_chess()

    snake.move()
    if snake.check_collision(food):
        # Если еда съедена, повышаем счёт, генерируем еду в новом месте
        score += 1
        food.generate_random_pos(snake)

        # Проверяем, не пора ли перейти на новый уровень (каждые 3 очка)
    if score >= level * score_for_next_level:
        level += 1
        # Увеличим скорость
        FPS += 2

    # Check collision with SuperFood
    if snake.check_collision(super_food):
        score += 5  # SuperFood gives more points
        super_food.generate_random_pos(snake, food)

    # Update and draw SuperFood
    super_food.timer += 1
    if super_food.timer >= super_food.max_time:
        super_food.generate_random_pos(snake, food)
    super_food.draw()

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}   Level: {level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()