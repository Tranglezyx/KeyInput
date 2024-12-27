import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 游戏对象
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, 50, 50)
obstacle = pygame.Rect(random.randint(0, SCREEN_WIDTH - 50), 0, 50, 50)
player_speed = 5
obstacle_speed = 5

# 游戏时钟
clock = pygame.time.Clock()

# 游戏主循环
while True:
    screen.fill(WHITE)  # 清屏

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 玩家控制
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
        player.move_ip(player_speed, 0)

    # 更新障碍物位置
    obstacle.move_ip(0, obstacle_speed)
    if obstacle.top > SCREEN_HEIGHT:
        obstacle.x = random.randint(0, SCREEN_WIDTH - 50)
        obstacle.y = 0

    # 检测碰撞
    if player.colliderect(obstacle):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # 绘制玩家和障碍物
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, obstacle)

    # 刷新屏幕
    pygame.display.flip()
    clock.tick(60)
