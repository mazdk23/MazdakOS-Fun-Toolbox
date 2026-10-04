import pygame
import random
import math
import sys

pygame.init()

# ============================================================
# SONIC-INSPIRED MINI PLATFORMER
# No external assets required.
# Controls: A/D or arrows = move, SPACE/W/UP = jump, R = restart
# ============================================================

WIDTH, HEIGHT = 1100, 650
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blue Rush - Sonic Inspired")
clock = pygame.time.Clock()

# Colors
SKY = (92, 190, 255)
SKY2 = (170, 230, 255)
WHITE = (255, 255, 255)
BLUE = (30, 95, 235)
DARK_BLUE = (12, 45, 150)
RED = (225, 45, 55)
YELLOW = (255, 220, 40)
GREEN = (55, 190, 75)
BROWN = (125, 75, 35)
DARK = (25, 30, 45)

font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 76)

WORLD_W = 6200
GROUND_Y = 540

# Platforms / ground sections
platforms = [
    pygame.Rect(0, GROUND_Y, 1200, 110),
    pygame.Rect(1320, GROUND_Y, 1050, 110),
    pygame.Rect(2550, GROUND_Y, 1250, 110),
    pygame.Rect(3950, GROUND_Y, 1000, 110),
    pygame.Rect(5100, GROUND_Y, 1100, 110),
    pygame.Rect(650, 430, 230, 25),
    pygame.Rect(980, 350, 250, 25),
    pygame.Rect(1500, 420, 250, 25),
    pygame.Rect(1850, 330, 260, 25),
    pygame.Rect(2750, 400, 260, 25),
    pygame.Rect(3200, 310, 300, 25),
    pygame.Rect(4100, 390, 280, 25),
    pygame.Rect(4550, 300, 280, 25),
    pygame.Rect(5350, 410, 300, 25),
]

# Rings
rings = []
for x, y in [
    (250,470),(310,470),(370,470),(430,470),
    (720,390),(780,390),(1040,310),(1100,310),(1160,310),
    (1450,470),(1510,470),(1570,470),
    (1880,290),(1940,290),(2000,290),
    (2300,470),(2360,470),
    (2700,470),(2760,470),(2820,470),
    (3260,270),(3320,270),(3380,270),
    (3600,470),(3660,470),(3720,470),
    (4200,350),(4260,350),(4320,350),
    (4650,260),(4710,260),
    (5200,470),(5260,470),(5320,470),
    (5400,370),(5460,370),(5520,370),
    (5800,470),(5860,470),(5920,470)
]:
    rings.append(pygame.Rect(x, y, 22, 22))

# Enemies
enemies = [
    {"rect": pygame.Rect(560, 500, 34, 34), "min": 450, "max": 900, "speed": 2},
    {"rect": pygame.Rect(1600, 380, 34, 34), "min": 1450, "max": 1900, "speed": 2},
    {"rect": pygame.Rect(2200, 500, 34, 34), "min": 1900, "max": 2350, "speed": 2.4},
    {"rect": pygame.Rect(2920, 365, 34, 34), "min": 2750, "max": 3300, "speed": 2},
    {"rect": pygame.Rect(4300, 355, 34, 34), "min": 4100, "max": 4700, "speed": 2.2},
    {"rect": pygame.Rect(5550, 500, 34, 34), "min": 5250, "max": 6000, "speed": 2.5},
]

# Player
player = pygame.Rect(150, 450, 38, 50)
vel_x = 0.0
vel_y = 0.0
on_ground = False
rings_count = 0
score = 0
lives = 3
camera_x = 0.0
game_over = False
won = False
hurt_timer = 0


def reset():
    global player, vel_x, vel_y, on_ground, rings_count
    global score, lives, camera_x, game_over, won, hurt_timer

    player.topleft = (150, 450)
    vel_x = 0
    vel_y = 0
    on_ground = False
    rings_count = 0
    score = 0
    lives = 3
    camera_x = 0
    game_over = False
    won = False
    hurt_timer = 0

    for enemy, original in zip(enemies, [
        (560,500),(1600,380),(2200,500),(2920,365),(4300,355),(5550,500)
    ]):
        enemy["rect"].topleft = original

    # Restore rings
    rings.clear()
    for x, y in [
        (250,470),(310,470),(370,470),(430,470),
        (720,390),(780,390),(1040,310),(1100,310),(1160,310),
        (1450,470),(1510,470),(1570,470),
        (1880,290),(1940,290),(2000,290),
        (2300,470),(2360,470),
        (2700,470),(2760,470),(2820,470),
        (3260,270),(3320,270),(3380,270),
        (3600,470),(3660,470),(3720,470),
        (4200,350),(4260,350),(4320,350),
        (4650,260),(4710,260),
        (5200,470),(5260,470),(5320,470),
        (5400,370),(5460,370),(5520,370),
        (5800,470),(5860,470),(5920,470)
    ]:
        rings.append(pygame.Rect(x, y, 22, 22))


def draw_background():
    # Sky gradient-ish bands
    screen.fill(SKY)
    for y in range(0, HEIGHT, 10):
        t = y / HEIGHT
        color = (
            int(92 + 45 * t),
            int(190 + 35 * t),
            int(255)
        )
        pygame.draw.rect(screen, color, (0, y, WIDTH, 10))

    # Clouds
    for wx, wy in [(250,110),(900,150),(1750,90),(3000,130),(4500,100),(5600,150)]:
        x = int(wx - camera_x * 0.25)
        pygame.draw.circle(screen, WHITE, (x, wy), 30)
        pygame.draw.circle(screen, WHITE, (x+35, wy-10), 40)
        pygame.draw.circle(screen, WHITE, (x+75, wy), 30)
        pygame.draw.rect(screen, WHITE, (x-5, wy, 85, 30))

    # Distant hills
    points = []
    for x in range(-200, WIDTH + 400, 100):
        world_x = x + camera_x * 0.45
        y = 420 + int(45 * math.sin(world_x / 250))
        points.append((x, y))
    points += [(WIDTH+300, HEIGHT), (-200, HEIGHT)]
    pygame.draw.polygon(screen, (70, 175, 100), points)


def draw_world():
    # Platforms
    for p in platforms:
        r = pygame.Rect(int(p.x-camera_x), p.y, p.width, p.height)
        if r.right < 0 or r.left > WIDTH:
            continue

        pygame.draw.rect(screen, GREEN, r)
        pygame.draw.rect(screen, BROWN, (r.x, r.y+18, r.width, r.height-18))

        # grass stripes
        for x in range(r.x, r.right, 28):
            pygame.draw.rect(screen, (40, 145, 55), (x, r.y+18, 12, 10))

    # Rings
    for ring in rings:
        r = pygame.Rect(int(ring.x-camera_x), ring.y, ring.width, ring.height)
        pygame.draw.circle(screen, YELLOW, r.center, 10, 4)

    # Enemies
    for e in enemies:
        r = e["rect"].move(-int(camera_x), 0)
        pygame.draw.ellipse(screen, RED, r)
        pygame.draw.circle(screen, WHITE, (r.x+10, r.y+12), 5)
        pygame.draw.circle(screen, WHITE, (r.x+24, r.y+12), 5)
        pygame.draw.circle(screen, DARK, (r.x+10, r.y+12), 2)
        pygame.draw.circle(screen, DARK, (r.x+24, r.y+12), 2)

    # Finish flag
    fx = int(6050 - camera_x)
    pygame.draw.rect(screen, DARK, (fx, 350, 8, 190))
    pygame.draw.polygon(screen, RED, [(fx+8,350),(fx+90,380),(fx+8,410)])


def draw_player():
    r = player.move(-int(camera_x), 0)

    # Simple blue character
    pygame.draw.ellipse(screen, BLUE, r)

    # spikes
    pygame.draw.polygon(screen, DARK_BLUE, [
        (r.x+5,r.y+12),(r.x-14,r.y+2),(r.x+5,r.y+25),
        (r.x-10,r.y+25),(r.x+8,r.y+35)
    ])

    # face / eye
    pygame.draw.ellipse(screen, WHITE, (r.x+20,r.y+8,12,18))
    pygame.draw.circle(screen, DARK, (r.x+27,r.y+14), 4)

    # shoes
    pygame.draw.ellipse(screen, RED, (r.x-2,r.bottom-10,22,12))
    pygame.draw.ellipse(screen, RED, (r.x+18,r.bottom-10,22,12))


def text_center(text, y, fnt, color=WHITE):
    surf = fnt.render(text, True, color)
    screen.blit(surf, surf.get_rect(center=(WIDTH//2, y)))


# Main loop
while True:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_r and (game_over or won):
                reset()

            if event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
                if on_ground and not game_over and not won:
                    vel_y = -15

    if not game_over and not won:
        keys = pygame.key.get_pressed()

        # Acceleration
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            vel_x -= 0.65
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            vel_x += 0.65

        # Friction
        if not (keys[pygame.K_a] or keys[pygame.K_LEFT] or
                keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            vel_x *= 0.82

        vel_x = max(-12, min(12, vel_x))

        # Gravity
        vel_y += 0.65
        vel_y = min(vel_y, 18)

        # Horizontal movement
        player.x += int(vel_x)

        if player.left < 0:
            player.left = 0

        # Vertical movement
        old_bottom = player.bottom
        player.y += int(vel_y)
        on_ground = False

        # Platform collision
        for p in platforms:
            if player.colliderect(p) and vel_y >= 0 and old_bottom <= p.top + 10:
                player.bottom = p.top
                vel_y = 0
                on_ground = True

        # Fell into pit
        if player.top > HEIGHT + 100:
            lives -= 1
            if lives <= 0:
                game_over = True
            else:
                player.topleft = (max(100, int(camera_x)+100), 350)
                vel_x = vel_y = 0

        # Collect rings
        for ring in rings[:]:
            if player.colliderect(ring):
                rings.remove(ring)
                rings_count += 1
                score += 100

        # Enemy movement + collision
        for e in enemies:
            e["rect"].x += e["speed"]

            if e["rect"].x <= e["min"] or e["rect"].x >= e["max"]:
                e["speed"] *= -1

            if player.colliderect(e["rect"]) and hurt_timer <= 0:
                if vel_y > 2:
                    score += 250
                    e["rect"].x = e["min"]
                    vel_y = -10
                elif rings_count > 0:
                    rings_count = 0
                    hurt_timer = 90
                    vel_x = -8 if player.centerx < e["rect"].centerx else 8
                    vel_y = -9
                else:
                    lives -= 1
                    hurt_timer = 90
                    player.topleft = (max(100, int(camera_x)+100), 350)
                    vel_x = vel_y = 0
                    if lives <= 0:
                        game_over = True

        if hurt_timer > 0:
            hurt_timer -= 1

        # Score for distance
        score = max(score, int(player.x / 5) + rings_count * 100)

        # Camera
        target_camera = player.centerx - WIDTH * 0.38
        camera_x += (target_camera - camera_x) * 0.12
        camera_x = max(0, min(WORLD_W - WIDTH, camera_x))

        # Finish
        if player.x >= 6000:
            won = True

    draw_background()
    draw_world()

    # HUD
    hud = font.render(
        f"RINGS: {rings_count:02d}   SCORE: {score:05d}   LIVES: {lives}",
        True, WHITE
    )
    screen.blit(hud, (20, 18))

    speed_text = font.render(
        f"SPEED: {abs(vel_x):.1f}",
        True, WHITE
    )
    screen.blit(speed_text, (20, 52))

    draw_player()

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,165))
        screen.blit(overlay, (0,0))
        text_center("GAME OVER", 245, big_font, RED)
        text_center("Press R to restart", 325, font)
        text_center("ESC to quit", 365, font)

    if won:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,130))
        screen.blit(overlay, (0,0))
        text_center("ZONE CLEAR!", 245, big_font, YELLOW)
        text_center(f"Score: {score}   Rings: {rings_count}", 325, font)
        text_center("Press R to play again", 365, font)

    pygame.display.flip()
